from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

DSCALE = 3

class T10P1(Scene):
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

    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Diagram objects
        spool = Circle(
            radius=1,
            color=GOLD,
            fill_color=GOLD_DARK,
            fill_opacity=1
        )
        spool_center = Dot(
            radius=0.15,
            color=GOLD
        )
        spool_group = Group(spool, spool_center)

        lift_arm1 = Rectangle(
            width=DSCALE*0.7+2*0.25,
            height=0.25,
            color=BLUE,
            fill_color=BLUE_DARK,
            fill_opacity=1
        )
        lift_arm1.shift(spool_center.get_edge_center(DOWN)-lift_arm1.get_corner(UP+LEFT)+0.25*LEFT)
        lift_arm2 = Rectangle(
            width=0.5,
            height=0.5,
            color=BLUE,
            fill_color=BLUE_DARK,
            fill_opacity=1
        )
        lift_arm2.move_to(lift_arm1.get_edge_center(RIGHT)+0.25*LEFT)
        lift_arm = Group(lift_arm1, lift_arm2)

        column = Rectangle(
            width=0.3,
            height=4,
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1
        ).move_to(lift_arm2.get_center())
        base = Rectangle(
            width=DSCALE*1.25,
            height=0.3,
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1
        ).next_to(column.get_edge_center(DOWN), LEFT, buff=0)

        wheel_A = Circle(
            radius=0.5,
            color=GREY,
            fill_color=DARK_GREY,
            fill_opacity=1
        ).move_to(base.get_edge_center(LEFT))
        wheel_A_center = Dot(
            radius=0.15,
            color=GREY
        ).move_to(wheel_A.get_center())
        wheel_A_group = Group(wheel_A, wheel_A_center)
        wheel_B_group = wheel_A_group.copy().move_to(base.get_edge_center(RIGHT))

        lift = Group(
            base,
            column,
            lift_arm,
            wheel_A_group,
            wheel_B_group
        )
        diagram = Group(
            spool_group,
            lift
        ).move_to(ORIGIN)
        self.add(diagram)
        self.wait()
        #endregion

        #region Label dimensions
        b_arrow = DoubleArrow(
            start=base.get_edge_center(LEFT),
            end=base.get_edge_center(LEFT)+DSCALE*0.75*RIGHT,
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(0.25*DOWN)
        b_label = MathTex('b', color=YELLOW).scale(0.7).next_to(b_arrow, DOWN, buff=0.15)
        c_arrow = DoubleArrow(
            start=base.get_edge_center(RIGHT),
            end=base.get_edge_center(RIGHT)+DSCALE*0.5*LEFT,
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(0.25*DOWN)
        c_label = MathTex('c', color=YELLOW).scale(0.7).next_to(c_arrow, DOWN, buff=0.15)
        G_dot = Dot(
            color=YELLOW
        ).move_to(b_arrow.get_end()+UP)
        G_label = MathTex('G', color=YELLOW).scale(0.7).next_to(G_dot, RIGHT, buff=0.15)
        e_arrow = DoubleArrow(
            start=lift_arm1.get_edge_center(LEFT)+0.25*RIGHT,
            end=lift_arm1.get_edge_center(RIGHT)+0.25*LEFT,
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(0.25*DOWN)
        e_label = MathTex('e', color=YELLOW).scale(0.7).next_to(e_arrow, DOWN, buff=0.15)

        self.play(
            Write(b_arrow),
            Write(b_label),
            Write(c_arrow),
            Write(c_label),
            Write(e_arrow),
            Write(e_label),
            FadeIn(G_dot),
            Write(G_label)
        )
        self.wait()
        #endregion

        #region Cleanup
        lift = Group(
            lift,
            b_arrow,
            b_label,
            c_arrow,
            c_label,
            e_arrow,
            e_label,
            G_dot,
            G_label
        )
        self.play(
            Transform(spool_group, spool_group.copy().scale(0.75).to_corner(UP+RIGHT, buff=1).shift(LEFT)),
            Transform(lift, lift.copy().scale(0.75).to_corner(DOWN+RIGHT, buff=1).shift(0.25*UP))
        )
        self.wait()
        #endregion

        #region Draw FBD arrows
        fbd1_grav = Arrow(
            start=spool.get_center()+1*UP,
            end=spool.get_center(),
            color=TEAL,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd1_grav_label = MathTex('m_sg', color=TEAL).scale(0.6).next_to(fbd1_grav, UP, buff=0.15)
        fbd1_N_C = Arrow(
            start=spool.get_center()+1*DOWN,
            end=spool.get_center(),
            color=RED,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd1_N_C_label = MathTex('N_C', color=RED).scale(0.6).next_to(fbd1_N_C.get_start(), RIGHT, buff=0.15)
        self.play(
            Write(fbd1_grav),
            Write(fbd1_grav_label),
            Write(fbd1_N_C),
            Write(fbd1_N_C_label)
        )
        self.wait()

        fbd2_grav = Arrow(
            start=G_dot.get_center(),
            end=G_dot.get_center()+1*DOWN,
            color=TEAL,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd2_grav_label = MathTex('m_tg', color=TEAL).scale(0.6).next_to(fbd2_grav, DOWN, buff=0.15)
        fbd2_N_C = Arrow(
            start=lift_arm1.get_edge_center(UP+LEFT)+0.25*0.75*RIGHT+UP,
            end=lift_arm1.get_edge_center(UP+LEFT)+0.25*0.75*RIGHT,
            color=RED,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd2_N_C_label = MathTex('N_C', color=RED).scale(0.6).next_to(fbd2_N_C.get_start(), LEFT, buff=0.15)
        fbd2_N_A = Arrow(
            start=wheel_A_group.get_edge_center(DOWN)+0.75*DOWN,
            end=wheel_A_group.get_edge_center(DOWN),
            color=RED,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd2_N_A_label = MathTex('2N_A', color=RED).scale(0.6).next_to(fbd2_N_A, LEFT, buff=0.15)
        fbd2_N_B = Arrow(
            start=wheel_B_group.get_edge_center(DOWN)+0.75*DOWN,
            end=wheel_B_group.get_edge_center(DOWN),
            color=RED,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd2_N_B_label = MathTex('2N_B', color=RED).scale(0.6).next_to(fbd2_N_B, RIGHT, buff=0.15)

        self.play(
            Write(fbd2_grav),
            Write(fbd2_grav_label),
            Write(fbd2_N_C),
            Write(fbd2_N_C_label),
            Write(fbd2_N_A),
            Write(fbd2_N_A_label),
            Write(fbd2_N_B),
            Write(fbd2_N_B_label)
        )
        self.wait()
        #endregion

        #region Math
        fbd1_eq = MathTex(
            'N_C - m_sg = m_sa'
        ).scale(0.6).to_corner(UP+LEFT)
        fbd1_eq_sub = MathTex(
            'N_C = m_s(a + g)'
        ).scale(0.6).next_to(fbd1_eq, DOWN, aligned_edge=LEFT)
        self.play(Write(fbd1_eq)),
        self.wait()
        self.play(Write(fbd1_eq_sub))
        self.number_equation(fbd1_eq_sub, 1)
        self.wait()

        fbd2_eq = MathTex(
            '2N_A + 2N_B - m_tg - N_C =',
            'm_t(0)'
        ).scale(0.6).next_to(fbd1_eq_sub, DOWN, aligned_edge=LEFT, buff=0.5)
        fbd2_eq_sub = MathTex(
            '2N_A + 2N_B - m_tg - N_C =',
            '0'
        ).scale(0.6).next_to(fbd1_eq_sub, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(fbd2_eq))
        self.wait()
        self.play(*[ReplacementTransform(fbd2_eq[i], fbd2_eq_sub[i]) for i in range(len(fbd2_eq))])
        self.number_equation(fbd2_eq, 2)
        self.wait()

        fbd2_eqM = MathTex(
            '2N_A(b+c) - N_C(e) - m_tg(c) = 0'
        ).scale(0.6).next_to(fbd2_eq_sub, DOWN, aligned_edge=LEFT)
        self.play(Write(fbd2_eqM))
        self.number_equation(fbd2_eqM, 3)
        self.wait()

        assume_text = Tex('assume $N_A=F_{max}$:').scale(0.5).next_to(fbd2_eqM, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(assume_text))
        self.wait()

        ans = MathTex(
            'N_A = 600\\,\\mathrm{N}',
            'N_B = 569.5\\,\\mathrm{N}',
            'a = 3.96\\,\\mathrm{m/s^2}'
        ).scale(0.6).next_to(assume_text, DOWN, aligned_edge=LEFT)
        ans[1:].next_to(ans[0], DOWN, aligned_edge=LEFT)
        ans[2:].next_to(ans[1], DOWN, aligned_edge=LEFT)
        ans.shift(0.15*RIGHT)
        ansbox = SurroundingRectangle(ans[2], buff=0.15)

        self.play(*[Write(ans[i]) for i in range(len(ans))])
        self.play(ShowCreation(ansbox))
        self.wait()

        ansexpl1 = Tex(
            '$N_A > N_B$, so the assumption is valid'
        ).scale(0.6).next_to(ansbox, DOWN, aligned_edge=LEFT, buff=0.5)
        ansexpl2 = Tex(
            '(wheels at A are the limiting factor)'
        ).scale(0.6).next_to(ansexpl1, DOWN, aligned_edge=LEFT)
        self.play(Write(ansexpl1))
        self.play(Write(ansexpl2))
        self.wait()
        #endregion