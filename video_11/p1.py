from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

DSCALE = 2
DIM_A = 0.9
DIM_B = 0.5
DIM_C = 0.6

class T11P1(Scene):
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
        def create_A_frame():
            left = Line(
                start=0.4*LEFT+1.3*DOWN,
                end=ORIGIN,
                color=BROWN,
                stroke_width=12
            )
            right = left.copy().flip(axis=UP)
            right.shift(left.get_end()-right.get_end())
            horiz = Line(
                start=left.get_center(),
                end=right.get_center(),
                color=BROWN,
                stroke_width=12
            )
            pivot = Dot(
                point=left.get_end(),
                color=BROWN,
                radius=0.12
            )
            Aframe = Group(left, right, horiz, pivot)
            return Aframe

        ground = Line(
            start=3*LEFT,
            end=3*RIGHT,
            color=GREY
        )

        A_frame_left = create_A_frame().shift(DSCALE*DIM_B*LEFT).align_to(ground, DOWN)
        A_frame_right = create_A_frame().shift(DSCALE*DIM_B*RIGHT).align_to(ground, DOWN)

        beam = Rectangle(
            height=0.125,
            width=DSCALE*2*(DIM_A+DIM_B),
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1
        ).next_to(Group(A_frame_left, A_frame_right), UP, buff=0)

        diagram = Group(
            ground,
            A_frame_left,
            A_frame_right,
            beam
        ).move_to(ORIGIN)
        self.add(diagram)
        self.wait()
        #endregion

        #region Annotate diagram
        point_A = Dot(
            point=A_frame_left.get_edge_center(UP),
            radius=0.05,
            color=YELLOW
        ).shift((0.125/2)*UP) # shift up half of beams height. tried to use .align_to(), but it's broken >:(
        point_A_label = MathTex('A', color=YELLOW).scale(0.6).next_to(point_A, DOWN, buff=0.15)
        point_B = Dot(
            point=A_frame_right.get_edge_center(UP),
            radius=0.05,
            color=YELLOW
        ).shift((0.125/2)*UP) # shift up half of beams height. tried to use .align_to(), but it's broken >:(
        point_B_label = MathTex('B', color=YELLOW).scale(0.6).next_to(point_B, DOWN, buff=0.15)
        point_C = Dot(
            point=beam.get_edge_center(LEFT),
            radius=0.05,
            color=YELLOW
        )
        point_C_label = MathTex('C', color=YELLOW).scale(0.6).next_to(point_C, LEFT, buff=0.15)
        point_D = Dot(
            point=beam.get_edge_center(RIGHT),
            radius=0.05,
            color=YELLOW
        )
        point_D_label = MathTex('D', color=YELLOW).scale(0.6).next_to(point_D, RIGHT, buff=0.15)
        point_G = Dot(
            point=beam.get_center(),
            radius=0.05,
            color=YELLOW
        )
        point_G_label = MathTex('G', color=YELLOW).scale(0.6).next_to(point_G, UP, buff=0.15)

        b_arrow_left = DoubleArrow(
            start=point_A.get_center(),
            end=point_G.get_center(),
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(1.75*DOWN)
        b_arrow_label_left = MathTex('b', color=YELLOW).scale(0.6).next_to(b_arrow_left, DOWN, buff=0.1)
        b_arrow_right = DoubleArrow(
            start=point_G.get_center(),
            end=point_B.get_center(),
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(1.75*DOWN)
        b_arrow_label_right = MathTex('b', color=YELLOW).scale(0.6).next_to(b_arrow_right, DOWN, buff=0.1)

        a_arrow_left = DoubleArrow(
            start=point_C.get_center(),
            end=point_A.get_center(),
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(1.75*DOWN)
        a_arrow_label_left = MathTex('a', color=YELLOW).scale(0.6).next_to(a_arrow_left, DOWN, buff=0.1)
        a_arrow_right = DoubleArrow(
            start=point_B.get_center(),
            end=point_D.get_center(),
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(1.75*DOWN)
        a_arrow_label_right = MathTex('a', color=YELLOW).scale(0.6).next_to(a_arrow_right, DOWN, buff=0.1)

        self.play(
            FadeIn(point_A),
            Write(point_A_label),
            FadeIn(point_B),
            Write(point_B_label),
            FadeIn(point_C),
            Write(point_C_label),
            FadeIn(point_D),
            Write(point_D_label),
            FadeIn(point_G),
            Write(point_G_label),
            Write(b_arrow_left),
            Write(b_arrow_label_left),
            Write(b_arrow_right),
            Write(b_arrow_label_right),
            Write(a_arrow_left),
            Write(a_arrow_label_left),
            Write(a_arrow_right),
            Write(a_arrow_label_right),
        )
        self.wait()

        diagram = Group(
            diagram,
            point_A,
            point_A_label,
            point_B,
            point_B_label,
            point_C,
            point_C_label,
            point_D,
            point_D_label,
            point_G,
            point_G_label
        )
        annot_group = Group(
            b_arrow_left,
            b_arrow_label_left,
            b_arrow_right,
            b_arrow_label_right,
            a_arrow_left,
            a_arrow_label_left,
            a_arrow_right,
            a_arrow_label_right
        )
        labeled_beam = Group(
            beam,
            point_A,
            point_A_label,
            point_B,
            point_B_label,
            point_C,
            point_C_label,
            point_D,
            point_D_label,
            point_G,
            point_G_label
        )
        #endregion

        #region Animate the key points in time
        self.play(
            Transform(diagram, diagram.copy().shift(1*UP)),
            Transform(annot_group, annot_group.copy().shift(1*UP)),
        )
        self.play(
            Rotate(
                labeled_beam,
                angle=np.arcsin(DIM_C/(DIM_A+2*DIM_B)),
                about_point=point_A.get_center()
            ),
            FadeOut(b_arrow_left),
            FadeOut(b_arrow_label_left),
            FadeOut(b_arrow_right),
            FadeOut(b_arrow_label_right),
            FadeOut(a_arrow_left),
            FadeOut(a_arrow_label_left),
            FadeOut(a_arrow_right),
            FadeOut(a_arrow_label_right),
        )
        self.wait()
        c_arrow = DoubleArrow(
            start=point_D.get_center(),
            end=point_D.get_center()+DSCALE*DIM_C*DOWN,
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(0.6*RIGHT)
        c_arrow_label = MathTex('c', color=YELLOW).scale(0.6).next_to(c_arrow, RIGHT, buff=0.1)
        c_refline = Line(
            start=point_A.get_center(),
            end=c_arrow.get_end(),
            buff=0.25,
            color=GREY
        )
        triang1 = Polygon(
            *[point_D.get_center(), point_A.get_center(), np.array([point_D.get_center()[0], point_A.get_center()[1], 0])],
            color=GREEN,
            fill_opacity=0,
            stroke_width=5,
            stroke_opacity=0.7
        )
        triang2 = Polygon(
            *[point_G.get_center(), point_A.get_center(), np.array([point_G.get_center()[0], point_A.get_center()[1], 0])],
            color=RED,
            fill_opacity=0,
            stroke_width=3,
            stroke_opacity=0.7
        )
        self.play(
            Write(c_arrow),
            Write(c_arrow_label),
            Create(c_refline)
        )
        self.wait()
        self.play(Create(triang1))
        self.play(Create(triang2))
        self.wait()
        time1_group = Group(
            diagram,
            c_arrow,
            c_arrow_label,
            c_refline,
            triang1,
            triang2
        ).copy()
        time1_group_newpos = time1_group.copy().scale(0.65).to_corner(DOWN+LEFT, buff=0.5).shift(0.25*UP)
        time1_label = MathTex('t_0', color=BLUE).scale(0.7).next_to(time1_group_newpos, DOWN, buff=0.15)
        self.play(
            Transform(time1_group, time1_group_newpos),
            Write(time1_label)
        )
        self.wait()

        self.play(
            FadeOut(c_arrow),
            FadeOut(c_arrow_label),
            FadeOut(c_refline),
            FadeOut(triang1),
            FadeOut(triang2),
            Rotate(
                labeled_beam,
                angle=-np.arcsin(DIM_C/(DIM_A+2*DIM_B)),
                about_point=point_A.get_center()
            )
        )
        self.wait()
        time2_group = diagram.copy()
        time2_group_newpos = time2_group.copy().scale(0.65).to_edge(DOWN, buff=0.5).shift(0.25*UP)
        time2_label = MathTex('t_1', color=BLUE).scale(0.7).next_to(time2_group_newpos, DOWN, buff=0.15)
        self.play(
            Transform(time2_group, time2_group_newpos),
            Write(time2_label)
        )
        self.wait()

        self.play(
            Rotate(
                labeled_beam,
                angle=-0.063,
                about_point=point_B.get_center()
            )
        )
        self.wait()
        theta_arrow1 = Arc(
            start_angle=PI-0.063-(PI/13),
            angle=PI/15,
            radius=3,
            color=YELLOW,
            buff=0
        ).add_tip(tip_length=0.15)
        theta_arrow1.move_arc_center_to(point_B.get_center())
        theta_arrow2 = Arc(
            start_angle=PI+(PI/13),
            angle=-PI/15,
            radius=3,
            color=YELLOW,
            buff=0
        ).add_tip(tip_length=0.15)
        theta_arrow2.move_arc_center_to(point_B.get_center())
        theta_arrow = Group(theta_arrow1, theta_arrow2)
        theta_arrow_label = MathTex('\\theta', color=YELLOW).scale(0.6).next_to(theta_arrow1.get_start(), UP, buff=0.1)
        h_arrow1 = Arrow(
            start=point_C.get_center()+0.5*UP,
            end=point_C.get_center(),
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        h_arrow2 = Arrow(
            start=point_C.get_center()+DSCALE*0.12*DOWN+0.5*DOWN,
            end=point_C.get_center()+DSCALE*0.12*DOWN,
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        h_arrow = Group(h_arrow1, h_arrow2)
        h_arrow_label = MathTex('h', color=YELLOW).scale(0.6).next_to(h_arrow1.get_start(), UP, buff=0.1)
        theta_refline = Line(
            start = point_B.get_center(),
            end=h_arrow2.get_end(),
            buff=0.25,
            color=GREY
        )
        self.play(
            Write(theta_arrow1),
            Write(theta_arrow2),
            Write(theta_arrow_label),
            Write(h_arrow1),
            Write(h_arrow2),
            Write(h_arrow_label),
            Create(theta_refline)
        )
        self.wait()
        time3_group = Group(
            diagram,
            theta_arrow,
            theta_arrow_label,
            h_arrow,
            h_arrow_label,
            theta_refline
        ).copy()
        time3_group_newpos = time3_group.copy().scale(0.65).to_corner(DOWN+RIGHT, buff=0.5).shift(0.25*UP)
        time3_label = MathTex('t_2', color=BLUE).scale(0.7).next_to(time3_group_newpos, DOWN, buff=0.15)
        self.play(
            Transform(time3_group, time3_group_newpos),
            Write(time3_label)
        )
        self.wait()

        self.play(
            FadeOut(diagram),
            FadeOut(theta_arrow),
            FadeOut(theta_arrow_label),
            FadeOut(h_arrow),
            FadeOut(h_arrow_label),
            FadeOut(theta_refline)
        )
        self.wait()
        #endregion

        #region Moments of inertia
        I_g = MathTex(
            'I_G = \\frac{1}{12}mL^2',
            '= \\frac{1}{12}\\frac{W}{g}(2a+2b)^2 = 8.994\\,\\mathrm{kgm^2}'
        ).scale(0.5).to_corner(UP+LEFT, buff=0.5)
        self.play(Write(I_g[0]))
        self.wait(0.5)
        self.play(Write(I_g[1]))
        self.wait()
        I_b = MathTex(
            'I_B = I_G + md^2',
            '= I_G + \\frac{W}{g}b^2 = 12.435\\,\\mathrm{kgm^2} = I_A'
        ).scale(0.5).next_to(I_g, RIGHT, buff=1)
        self.play(Write(I_b[0]))
        self.wait(0.5)
        self.play(Write(I_b[1]))
        self.wait()
        #endregion

        # Time 0 to 1
        energy = MathTex(
            '\\Delta \\mathbb{W}',
            '=',
            '\\Delta E_{grav}',
            '+',
            '\\Delta E_{kin}'
        ).scale(0.5).next_to(I_g, DOWN, aligned_edge=LEFT)
        self.play(Write(energy))
        self.wait()
        time_01 = Tex('$t_0$ to $t_1$:', color=BLUE).scale(0.5).next_to(energy, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(time_01))
        self.wait()
        energy_01 = MathTex(
            '0',
            '=',
            '-W\\left(\\frac{b}{2b+a}\\right)c',
            '+',
            '\\frac{1}{2}I_A\\omega_1^2',
            '\\Rightarrow',
            '\\omega_1 = 1.852\\,\\mathrm{rad/s}'
        ).scale(0.5).next_to(time_01, RIGHT)
        self.play(Write(energy_01[:-2]))
        self.wait()
        self.play(Write(energy_01[-2:]))
        self.wait()

        # Time 1- to 1+
        time_1 = Tex(
            '$t_{1i}$ just before collision, $t_{1f}$ just after collision', color=BLUE
        ).scale(0.5).next_to(Group(time_01, energy_01), DOWN, aligned_edge=LEFT)
        self.play(Write(time_1))
        self.wait()
        mom_1 = MathTex(
            'H_{Bi} = H_{Bf}',
            '-I_G\\omega_1',
            '+',
            'mv_Gb',
            '=',
            '-I_B\\omega_2'
        ).scale(0.5).next_to(time_1, DOWN, aligned_edge=LEFT)
        mom_1[1:].next_to(mom_1[0], DOWN, aligned_edge=LEFT)
        self.play(Write(mom_1[0]))
        self.wait()
        self.play(Write(mom_1[1]))
        self.wait(0.5)
        self.play(Write(mom_1[2:4]))
        self.wait(0.5)
        self.play(Write(mom_1[4:]))
        self.wait()
        mom_1_sub = MathTex(
            '-I_G\\omega_1',
            '+',
            '\\frac{W}{g}(\\omega_1b)b',
            '=',
            '-I_B\\omega_2',
            '\\Rightarrow',
            '\\omega_2 = 0.827\\,\\mathrm{rad/s}'
        ).scale(0.5).move_to(mom_1[1:].get_center()).align_to(mom_1[1:], LEFT)
        self.play(*[ReplacementTransform(mom_1[i+1], mom_1_sub[i]) for i in range(5)])
        self.wait()
        self.play(Write(mom_1_sub[-2:]))
        self.wait()

        # Time 1 to 2
        time_12 = Tex('$t_1$ to $t_2$:', color=BLUE).scale(0.5).next_to(mom_1_sub, DOWN, buff=0.25, aligned_edge=LEFT)
        self.play(Write(time_12))
        self.wait()
        energy_12 = MathTex(
            '0',
            '=',
            'Wb\\sin(\\theta)',
            '-',
            '\\frac{1}{2}I_B\\omega_2^2',
            '\\Rightarrow',
            '\\theta = 0.063\\,\\mathrm{rad}'
        ).scale(0.5).next_to(time_12, RIGHT)
        self.play(Write(energy_12[:-2]))
        self.wait()
        self.play(Write(energy_12[-2:]))
        self.wait()

        # Find height h
        h = MathTex(
            'h = (a+2b)\\sin(\\theta) = 0.12\\,\\mathrm{m}'
        ).scale(0.5).next_to(energy_12, RIGHT, buff=1).shift(0.15*RIGHT)
        ansbox = SurroundingRectangle(h, buff=0.15)
        self.play(Write(h))
        self.play(Create(ansbox))
        self.wait()