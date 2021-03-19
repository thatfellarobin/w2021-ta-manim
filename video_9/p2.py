from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

DSCALE = 1/3
IMGSCALE = 5/500




class T9P2(Scene):
    def number_equation(self, eq, n, color=YELLOW_B):
        num = MathTex('\\textbf{' + str(n) + '}', color=color).scale(0.5)
        circle = Circle(
            color=color,
            radius=0.225,
            arc_center=num.get_center()
        )
        line = Line(
            start=circle.get_edge_center(LEFT),
            end=circle.get_edge_center(LEFT)+0.5*LEFT,
            color=color
        )
        group = Group(num, circle, line)
        group.next_to(eq, RIGHT, buff=0.25)
        self.play(FadeIn(group))
        return group


    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Diagram objects
        ground = Line(
            start=2*LEFT,
            end=2*RIGHT,
            color=GREY
        )
        block = Rectangle(
            height=0.5,
            width=3,
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1
        ).next_to(ground, UP, buff=0)
        spool = Circle(
            radius=0.7,
            color=GOLD,
            fill_color=GOLD_DARK,
            fill_opacity=1
        ).next_to(block, UP, buff=0)
        spool_line1 = Line(
            start=spool.get_edge_center(DOWN),
            end=spool.get_edge_center(UP),
            color=GOLD
        )
        spool_line2 = Line(
            start=spool.get_edge_center(LEFT),
            end=spool.get_edge_center(RIGHT),
            color=GOLD
        )
        spool_group = Group(spool, spool_line1, spool_line2)

        diagram = Group(
            ground,
            block,
            spool_group
        ).move_to(ORIGIN)
        self.add(diagram)
        self.wait()
        #endregion

        #region Annotate diagram
        r_arrow = Arrow(
            start=spool.get_center(),
            end=spool.point_at_angle(PI/4),
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        r_label = MathTex('r=0.9\\,\\mathrm{m}', color=YELLOW).scale(0.6).next_to(r_arrow.get_end(), UP+RIGHT, buff=0.1)
        point_A = Dot(
            point=spool.get_edge_center(DOWN),
            color=YELLOW
        )
        point_A_label = MathTex('A', color=YELLOW).scale(0.6).next_to(point_A, DOWN, buff=0.1)
        point_G = Dot(
            point=spool.get_center(),
            color=YELLOW
        )
        point_G_label = MathTex('G', color=YELLOW).scale(0.6).next_to(point_G, UP+LEFT, buff=0.05)
        self.play(
            FadeIn(r_arrow),
            Write(r_label),
            FadeIn(point_A),
            Write(point_A_label),
            FadeIn(point_G),
            Write(point_G_label)
        )
        self.wait()
        diagram = Group(
            diagram,
            r_arrow,
            r_label,
            point_A,
            point_A_label,
            point_G,
            point_G_label
        )
        #endregion


        spool_group_fbd = spool_group.copy()
        for item in spool_group_fbd:
            item.set_opacity(0)
        spool_group_fbdpos = spool_group.copy().to_corner(UP+RIGHT, buff=2)
        self.play(
            Transform(diagram, diagram.copy().scale(1).to_corner(DOWN+RIGHT, buff=1)),
            Transform(spool_group_fbd, spool_group_fbdpos)
        )
        self.wait()


        #region Draw FBD arrows
        fbd_mg_arrow = Arrow(
            start=spool_group_fbd.get_edge_center(UP)+0.75*UP,
            end=spool_group_fbd.get_edge_center(UP),
            color=BLUE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_mg_label = MathTex('W', color=BLUE).scale(0.6).next_to(fbd_mg_arrow, UP, buff=0.1)
        fbd_FN_arrow = Arrow(
            start=spool_group_fbd.get_edge_center(DOWN)+0.75*DOWN,
            end=spool_group_fbd.get_edge_center(DOWN),
            color=PURPLE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_FN_label = MathTex('F_N', color=PURPLE).scale(0.6).next_to(fbd_FN_arrow, DOWN, buff=0.1)
        fbd_Ff_arrow = Arrow(
            start=spool_group_fbd.get_edge_center(DOWN),
            end=spool_group_fbd.get_edge_center(DOWN)+0.75*RIGHT,
            color=MAROON,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_Ff_label = MathTex('F_f', color=MAROON).scale(0.6).next_to(fbd_Ff_arrow, RIGHT, buff=0.1)

        self.play(
            FadeIn(fbd_mg_arrow),
            Write(fbd_mg_label),
            FadeIn(fbd_FN_arrow),
            Write(fbd_FN_label),
            FadeIn(fbd_Ff_arrow),
            Write(fbd_Ff_label)
        )
        self.wait()
        #endregion

        fbd_y_eq = MathTex('W=F_N=900\\,\\mathrm{N}').scale(0.65).to_corner(UP+LEFT, buff=0.75)
        self.play(Write(fbd_y_eq))
        self.wait()
        fbd_x_eq = MathTex('F_f = \\frac{W}{g}a_G').scale(0.65).next_to(fbd_y_eq, DOWN, aligned_edge=LEFT)
        self.play(Write(fbd_x_eq))
        self.number_equation(fbd_x_eq, 1)
        self.wait()
        fbd_rot_eq = MathTex(
            '\\Sigma M = I\\alpha'
        ).scale(0.65).next_to(fbd_x_eq, DOWN, aligned_edge=LEFT)
        fbd_rot_eq_subbed = MathTex(
            'F_f r = \\frac{W}{g}k_G^2 \\alpha'
        ).scale(0.65).next_to(fbd_rot_eq, DOWN, aligned_edge=LEFT).shift(0.5*RIGHT)
        self.play(Write(fbd_rot_eq))
        self.wait()
        self.play(Write(fbd_rot_eq_subbed))
        self.number_equation(fbd_rot_eq_subbed, 2)
        self.wait()
        accel_relate_eq = MathTex(
            'a_G = a_{At} - \\alpha r'
        ).scale(0.65).next_to(Group(fbd_rot_eq, fbd_rot_eq_subbed), DOWN, aligned_edge=LEFT)
        self.play(Write(accel_relate_eq))
        self.number_equation(accel_relate_eq, 3)
        self.wait()

        # Answers
        ans_eqs = MathTex(
            'F_f = 42.4\\,\\mathrm{N}',
            'a_G = 0.462\\,,\\mathrm{m/s^2}',
            '\\alpha = 1.15\\,\\mathrm{rad/s^2}'
        ).scale(0.65).next_to(accel_relate_eq, DOWN, aligned_edge=LEFT)
        ans_eqs[1:].next_to(ans_eqs[0], DOWN, aligned_edge=LEFT)
        ans_eqs[2:].next_to(ans_eqs[1], DOWN, aligned_edge=LEFT)
        ansbox = SurroundingRectangle(ans_eqs[2], buff=0.15)
        self.play(
            *[Write(ans_eqs[i]) for i in range(len(ans_eqs))]
        )
        self.play(ShowCreation(ansbox))
        self.wait()


        fric_max_eq = MathTex('F_{fs,max} = \\mu_s F_N = 135\\,\\mathrm{N}').scale(0.65).next_to(ans_eqs, DOWN, aligned_edge=LEFT)
        self.play(Write(fric_max_eq))
        self.wait()

        # TODO: add equation numbers