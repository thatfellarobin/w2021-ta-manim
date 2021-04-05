from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

BALL_RADIUS = 0.75
BALL_HEIGHT = 2
BALL_OFFSET = 0.5

class T11P2(Scene):
    def number_equation(self, eq, n, color=YELLOW_B):
        num = MathTex('\\textbf{' + str(n) + '}', color=color).scale(0.5)
        circle = Circle(
            color=color,
            radius=0.225,
            arc_center=num.get_center()
        )
        line = Line(
            start=circle.get_edge_center(LEFT),
            end=circle.get_edge_center(LEFT)+0.6*LEFT,
            color=color
        )
        group = Group(num, circle, line)
        group.next_to(eq, RIGHT, buff=0.25)
        self.play(FadeIn(group))
        return group

    def recursive_set_opacity(self, mobj, opacity=0):
        for item in mobj:
            if len(item) > 1:
                self.recursive_set_opacity(mobj=item, opacity=opacity)
            else:
                item.set_opacity(opacity)
        return mobj

    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Diagram objects
        corner_upper = Line(
            start=ORIGIN,
            end=2.5*LEFT
        )
        corner_upper.set_color([GREY, GREY, BLACK])
        corner_right = Line(
            start=ORIGIN,
            end=2.5*DOWN
        )
        corner_right.set_color([BLACK, GREY, GREY]) # Unknown why it needs to be reversed here, feels like a manim bug
        corner = Group(
            corner_upper,
            corner_right
        )

        ball = Circle(
            arc_center=BALL_OFFSET*RIGHT + BALL_HEIGHT*UP,
            radius=BALL_RADIUS,
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1,
            stroke_width=5
        )

        diagram = Group(
            corner,
            ball
        )

        self.add(diagram)
        self.wait()
        #endregion

        #region Animate falling
        contact_theta = (PI/2) - np.arccos(BALL_OFFSET/BALL_RADIUS)
        print(contact_theta)
        contact_height = BALL_RADIUS * np.cos(contact_theta)
        def generate_path():
            v1 = 0.5
            v2 = 0.4
            v_down = 0
            tstep = 0.01
            finished = False
            bounced = False
            pos = ball.get_center() # keep track of where the ball centre is
            path = VMobject()
            path.set_points_as_corners([pos, pos])
            while not finished:
                if not bounced:
                    pos += v1*tstep*DOWN
                    path.add_points_as_corners([pos])
                    if pos[1] <= contact_height:
                        bounced = True
                else:
                    pos += v2*tstep*RIGHT
                    v_down += tstep * 0.02 # TODO: Tune the gravity here.
                    pos += tstep * v_down*DOWN
                    path.add_points_as_corners([pos])
                if pos[0] >=3:
                    finished = True
            return path
        path = generate_path()

        for _ in range(3):
            self.play(MoveAlongPath(ball, path, rate_func=linear, run_time=2.5))
            self.play(FadeOut(ball, run_time=0.5))
            ball.move_to(path.get_start())
            self.play(FadeIn(ball, run_time=0.5))
        self.wait()
        #endregion

        #region Annotate diagram and math it out
        self.play(Transform(ball, ball.copy().shift((ball.get_center()[1] - contact_height)*DOWN )))
        self.play(Transform(diagram, diagram.copy().to_corner(DOWN+RIGHT, buff=1).shift(0.5*DOWN+0.5*LEFT)))
        self.wait()

        refline_vert = Line(
            start=corner_upper.get_start(),
            end=corner_upper.get_start()+(BALL_RADIUS/np.cos(contact_theta))*UP,
            color=YELLOW,
            stroke_width=2
        )
        refline_horiz = Line(
            start=corner_upper.get_start(),
            end=corner_upper.get_start()+(BALL_RADIUS/np.cos((PI/2)-contact_theta))*RIGHT,
            color=YELLOW,
            stroke_width=2
        )
        refline_radius = Line(
            start=corner_upper.get_start(),
            end=ball.get_center(),
            color=YELLOW,
            stroke_width=2
        )
        refline_tan1 = Line(
            start=refline_vert.get_end(),
            end=refline_radius.get_end(),
            color=YELLOW,
            stroke_width=2
        )
        refline_tan2 = Line(
            start=refline_horiz.get_end(),
            end=refline_radius.get_end(),
            color=YELLOW,
            stroke_width=2
        )
        arcbuff = 7 * (PI/180)
        theta_arrow = Arc(
            start_angle=PI/2-arcbuff,
            angle=-(contact_theta-2*arcbuff),
            radius=0.85,
            color=YELLOW
        ).add_tip(tip_length=0.15)
        theta_arrow.move_arc_center_to(corner_upper.get_start())
        theta_annot = MathTex('\\theta', color=YELLOW).scale(0.7).next_to(theta_arrow.get_start(), LEFT, buff=0.15)
        self.play(Create(refline_radius))
        self.play(
            Write(theta_arrow),
            Write(theta_annot)
        )
        self.wait()

        # Show arrows
        v1_arrow = Arrow(
            start=refline_vert.get_end(),
            end=refline_vert.get_start(),
            color=RED,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        v1_arrow.shift(ball.get_center()-v1_arrow.get_end())
        v1_annot = MathTex(
            'v_1',
            color=RED
        ).scale(0.7).next_to(v1_arrow, UP, buff=0.15)
        v1_decomp = Group(
            v1_arrow.copy().shift(refline_radius.get_start()-v1_arrow.get_end()),
            v1_annot.copy().shift(refline_radius.get_start()-v1_arrow.get_end()),
            refline_radius.copy(),
            refline_tan1.copy(),
            theta_arrow.copy(),
            theta_annot.copy()
        ).scale(1.3).to_corner(UP+RIGHT, buff=1)
        self.play(
            Write(v1_arrow),
            Write(v1_annot)
        )
        self.wait()
        self.play(
            FadeIn(v1_decomp)
        )

        theta_arrow_comp = Arc(
            start_angle=arcbuff,
            angle=((PI/2)-contact_theta-2*arcbuff),
            radius=0.85,
            color=YELLOW
        ).add_tip(tip_length=0.15)
        theta_arrow_comp.move_arc_center_to(corner_upper.get_start())
        theta_annot_comp = MathTex('\\frac{\\pi}{2}-\\theta', color=YELLOW).scale(0.7/1.3).next_to(theta_arrow_comp.get_start(), DOWN, buff=0.15)
        v2_arrow = Arrow(
            start=refline_horiz.get_start(),
            end=refline_horiz.get_end(),
            color=GREEN,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        v2_arrow.shift(ball.get_center()-v2_arrow.get_start())
        v2_annot = MathTex(
            'v_2',
            color=GREEN
        ).scale(0.7).next_to(v2_arrow, RIGHT, buff=0.15)
        v2_decomp = Group(
            v2_arrow.copy().shift(refline_radius.get_start()-v2_arrow.get_start()),
            v2_annot.copy().shift(refline_radius.get_start()-v2_arrow.get_start()),
            refline_radius.copy(),
            refline_tan2.copy(),
            theta_arrow_comp,
            theta_annot_comp
        ).scale(1.3).next_to(v1_decomp, LEFT, buff=1.5, aligned_edge=UP)
        self.play(
            Write(v2_arrow),
            Write(v2_annot),
            FadeIn(v2_decomp)
        )
        self.wait()

        # No slip condition
        omega_arrow = Arc(
            start_angle=-PI/2,
            angle=-3*TAU/4,
            radius=0.3,
            color=PURPLE
        ).add_tip(tip_length=0.15)
        omega_arrow.move_arc_center_to(ball.get_center())
        omega_annot = MathTex('\\omega', color=PURPLE).scale(0.6).next_to(omega_arrow.get_start(), DOWN, buff=0.15)
        self.play(
            Write(omega_arrow),
            Write(omega_annot)
        )
        self.wait()
        noslip_title = Tex('No-slip condition:', color=BLUE).scale(0.5).to_corner(UP+LEFT, buff=0.5)
        self.play(Write(noslip_title))
        self.wait()
        noslip = MathTex(
            '\\omega r = v_2 \\sin((\\pi/2)-\\theta)'
        ).scale(0.5).next_to(noslip_title, DOWN, aligned_edge=LEFT)
        self.play(
            Write(noslip)
        )
        self.number_equation(noslip, 1)
        self.wait()

        # Momentum - Show relevant initial and final momentum arrows
        momentum_title = Tex('Conservation of angular momentum about the impact point:', color=BLUE).scale(0.5).next_to(noslip, DOWN, aligned_edge=LEFT)
        self.play(Write(momentum_title))
        self.wait()
        momentum = MathTex(
            'mv_1 r\\sin(\\theta)',
            '=',
            'mv_2 r\\cos(\\theta)',
            '+',
            'I\\omega'
        ).scale(0.5).next_to(momentum_title, DOWN, buff=0.4, aligned_edge=LEFT)
        momentum_sub = MathTex(
            'mv_1 r\\sin(\\theta)',
            '=',
            'mv_2 r\\cos(\\theta)',
            '+',
            '\\frac{2}{5}mr^2\\omega'
        ).scale(0.5)
        momentum_sub.shift(momentum[1].get_center()-momentum_sub[1].get_center())
        self.play(Write(momentum))
        self.wait()
        self.play(*[Transform(momentum[i], momentum_sub[i]) for i in range(len(momentum))])
        self.number_equation(momentum, 2)
        self.wait()

        # Apply restitution
        restitution_title = Tex('Collision restitution:', color=BLUE).scale(0.5).next_to(momentum, DOWN, aligned_edge=LEFT)
        self.play(Write(restitution_title))
        self.wait()
        restitution = MathTex(
            'ev_1\\cos(\\theta) = v_2\\cos((\\pi/2)-\\theta)'
        ).scale(0.5).next_to(restitution_title, DOWN, aligned_edge=LEFT)
        self.play(Write(restitution))
        self.number_equation(restitution, 3)
        self.wait()

        # Answer
        ans = MathTex(
            '\\theta = \\tan^{-1}\\sqrt{\\frac{7e}{5}}'
        ).scale(0.5).next_to(restitution, DOWN, buff=0.5, aligned_edge=LEFT).shift(0.15*RIGHT)
        ansbox = SurroundingRectangle(ans, buff=0.15)
        self.play(Write(ans))
        self.play(Create(ansbox))
        self.wait()