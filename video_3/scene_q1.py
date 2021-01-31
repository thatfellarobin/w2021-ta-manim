from manim import *
import numpy as np

TEAL_DARK = '#1c4037'
GREEN_DARK = '#2b4022'
BLUE_E_DARK = '#0c343d'
GREY_BLUE = '#465778'
GREY_BLUE_DARK = '#2d384d'

class PartA(Scene):
    def construct(self):
        #region Diagram imagery
        block_A = Rectangle(
            color=TEAL,
            height=1.5,
            width=2.5,
            mark_paths_closed=True,
            close_new_points=True,
            stroke_width=4,
            fill_color=TEAL_DARK,
            fill_opacity=1
        ).shift(1*LEFT + 0.75*DOWN)
        block_B = Rectangle(
            color=GREEN,
            height=1.5,
            width=2.5,
            mark_paths_closed=True,
            close_new_points=True,
            stroke_width=4,
            fill_color=GREEN_DARK,
            fill_opacity=1
        ).next_to(block_A, UP, buff=0.02)
        text_A = Tex("A", color=WHITE).move_to(block_A.get_center()).scale(1.4)
        text_B = Tex("B", color=WHITE).move_to(block_B.get_center()).scale(1.4)

        A = Group(block_A, text_A)
        B = Group(block_B, text_B)

        floor = Line(start=3.5*LEFT, end=2.5*RIGHT, color=GREY).shift(A.get_edge_center(DOWN)[1]*UP)
        wall = Line(start=ORIGIN, end=3.5*UP, color=GREY).shift(floor.get_end())

        rope_tie_1 = Dot(
            color=YELLOW_A,
            radius=0.16
        ).move_to(B.get_edge_center(RIGHT))
        rope_tie_2 = Dot(
            color=YELLOW_A,
            radius=0.16
        ).move_to(wall.get_center()).align_to(rope_tie_1, UP)
        rope = Line(
            start=rope_tie_1.get_center(),
            end=rope_tie_2.get_center(),
            color=YELLOW_E
        )

        pull_force = Arrow(
            color=RED,
            buff=0,
            start=ORIGIN,
            end=2*LEFT
        ).next_to(A, LEFT, buff=0)
        force_label = MathTex("P", color=pull_force.get_color()).scale(1.4).next_to(pull_force, LEFT)

        diagram = Group(floor, wall, rope, rope_tie_1, rope_tie_2, A, B, pull_force, force_label).move_to(ORIGIN)
        #endregion

        # Need to copy before the diagram transformation to preserve the scale
        A_fbd = A.copy().move_to(ORIGIN).scale(0.55).shift(3.5*LEFT+1.5*UP)
        B_fbd = B.copy().move_to(ORIGIN).scale(0.55).shift(3.5*RIGHT+1.5*UP)

        self.add(diagram)
        self.wait()

        dividing_line = Line(start=3*DOWN, end=3*UP, color=GREY)

        self.play(Transform(diagram, diagram.copy().scale(0.3).shift(5.5*LEFT+3*UP)))
        self.play(ShowCreation(dividing_line))
        self.wait()

        #region Animate free body diagram for block A
        self.play(FadeIn(A_fbd))
        self.wait()
        P = Arrow(
            color=RED,
            buff=0,
            start=ORIGIN,
            end=1.5*LEFT,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).next_to(A_fbd, LEFT, buff=0)
        P_label = MathTex("P", color=P.get_color()).scale(0.8).next_to(P, LEFT)
        A_mg = Arrow(
            color=BLUE,
            buff=0,
            start=ORIGIN,
            end=1.0*DOWN,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(A_fbd.get_center()+0.1*LEFT)
        A_mg_label = MathTex("mg", color=A_mg.get_color()).scale(0.8).next_to(A_mg, LEFT, aligned_edge=DOWN)
        normal_A_1 = Arrow(
            color=PURPLE,
            buff=0,
            start=ORIGIN,
            end=0.8*UP,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).next_to(A_fbd, DOWN, buff=0).shift(0.1*RIGHT)
        normal_A_1_label = MathTex("N_1", color=normal_A_1.get_color()).scale(0.8).next_to(normal_A_1, RIGHT, buff=0, aligned_edge=DOWN)
        normal_A_2 = Arrow(
            color=PURPLE,
            buff=0,
            start=ORIGIN,
            end=0.8*DOWN,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).next_to(A_fbd, UP, buff=0)
        normal_A_2_label = MathTex("N_2", color=normal_A_2.get_color()).scale(0.8).next_to(normal_A_2, RIGHT, buff=0, aligned_edge=UP)
        fric_A_1 = Arrow(
            color=MAROON,
            buff=0,
            start=ORIGIN,
            end=1.5*RIGHT,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(A_fbd.get_edge_center(DOWN))
        fric_A_1_label = MathTex("F_{f1}", color=fric_A_1.get_color()).scale(0.8).next_to(fric_A_1, RIGHT)
        fric_A_2 = Arrow(
            color=MAROON,
            buff=0,
            start=ORIGIN,
            end=1.5*RIGHT,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(A_fbd.get_edge_center(UP))
        fric_A_2_label = MathTex("F_{f2}", color=fric_A_2.get_color()).scale(0.8).next_to(fric_A_2, RIGHT)

        self.play(Write(P), Write(P_label))
        self.wait()
        self.play(Write(A_mg), Write(A_mg_label))
        self.wait()
        self.play(Write(normal_A_1), Write(normal_A_1_label), Write(normal_A_2), Write(normal_A_2_label))
        self.wait()
        self.play(Write(fric_A_1), Write(fric_A_1_label), Write(fric_A_2), Write(fric_A_2_label))
        self.wait()
        #endregion

        #region 2nd law for block A
        sum_fx_A = MathTex(
            '\\Sigma F_x',
            '=',
            'ma_A',
            '=',
            '\\mu N_1',
            '+',
            '\\mu N_2',
            '-',
            'P',
        ).scale(0.7).to_edge(LEFT).shift(0.25*DOWN)
        sum_fx_A[0].set_color(YELLOW)
        sum_fx_A[4].set_color(MAROON)
        sum_fx_A[6].set_color(MAROON)
        sum_fx_A[8].set_color(RED)
        sum_fy_A = MathTex(
            '\\Sigma F_y',
            '=',
            '0',
            '=',
            'N_1',
            '-',
            'N_2',
            '-',
            'mg',
        ).scale(0.7).next_to(sum_fx_A, DOWN, aligned_edge=LEFT)
        sum_fy_A[0].set_color(YELLOW)
        sum_fy_A[4].set_color(PURPLE)
        sum_fy_A[6].set_color(PURPLE)
        sum_fy_A[8].set_color(BLUE)
        self.play(Write(sum_fx_A[0]))
        self.play(Write(sum_fx_A[1:3]))
        self.wait()
        self.play(Write(sum_fx_A[3:]))
        self.wait()
        self.play(Write(sum_fy_A[0]))
        self.play(Write(sum_fy_A[1:3]))
        self.wait()
        self.play(Write(sum_fy_A[3:]))
        self.wait()
        #endregion

        #region Animate free body diagram for block B
        self.play(FadeIn(B_fbd))
        self.wait()
        B_mg = Arrow(
            color=BLUE,
            buff=0,
            start=ORIGIN,
            end=1.0*DOWN,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(B_fbd.get_center()+0.1*LEFT)
        B_mg_label = MathTex("mg", color=B_mg.get_color()).scale(0.8).next_to(B_mg, LEFT, aligned_edge=DOWN)
        normal_B_2 = Arrow(
            color=PURPLE,
            buff=0,
            start=ORIGIN,
            end=0.8*UP,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).next_to(B_fbd, DOWN, buff=0).shift(0.1*RIGHT)
        normal_B_2_label = MathTex("N_2", color=normal_B_2.get_color()).scale(0.8).next_to(normal_B_2, RIGHT, buff=0, aligned_edge=DOWN)
        fric_B_2 = Arrow(
            color=MAROON,
            buff=0,
            start=ORIGIN,
            end=1.5*LEFT,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(B_fbd.get_edge_center(DOWN))
        fric_B_2_label = MathTex("F_{f2}", color=fric_B_2.get_color()).scale(0.8).next_to(fric_B_2, LEFT)
        T = Arrow(
            color=RED,
            buff=0,
            start=ORIGIN,
            end=1.5*RIGHT,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).next_to(B_fbd, RIGHT, buff=0)
        T_label = MathTex("T", color=T.get_color()).scale(0.8).next_to(T, RIGHT)

        self.play(Write(B_mg), Write(B_mg_label))
        self.wait()
        self.play(Write(normal_B_2), Write(normal_B_2_label))
        self.wait()
        self.play(Write(fric_B_2), Write(fric_B_2_label))
        self.wait()
        self.play(Write(T), Write(T_label))
        self.wait()
        #endregion

        #region 2nd law for block B
        sum_fx_B = MathTex(
            '\\Sigma F_x',
            '=',
            '0',
            '=',
            'T',
            '-',
            '\\mu N_2',
        ).scale(0.7).next_to(dividing_line, RIGHT).shift(0.25*DOWN + 0.25*RIGHT)
        sum_fx_B[0].set_color(YELLOW)
        sum_fx_B[4].set_color(RED)
        sum_fx_B[6].set_color(MAROON)
        sum_fy_B = MathTex(
            '\\Sigma F_y',
            '=',
            '0',
            '=',
            'N_2',
            '-',
            'mg',
        ).scale(0.7).next_to(sum_fx_B, DOWN, aligned_edge=LEFT)
        sum_fy_B[0].set_color(YELLOW)
        sum_fy_B[4].set_color(PURPLE)
        sum_fy_B[6].set_color(BLUE)
        self.play(Write(sum_fx_B[0]))
        self.play(Write(sum_fx_B[1:3]))
        self.wait()
        self.play(Write(sum_fx_B[3:]))
        self.wait()
        self.play(Write(sum_fy_B[0]))
        self.play(Write(sum_fy_B[1:3]))
        self.wait()
        self.play(Write(sum_fy_B[3:]))
        self.wait()
        #endregion

        #region Math it out
        # solve y axis of block B
        self.play(FadeOut(sum_fy_B[:2]))
        self.wait()
        self.play(FadeOut(sum_fy_B[2]), FadeOut(sum_fy_B[5]))
        self.play(Transform(sum_fy_B[-1], sum_fy_B[-1].copy().set_color(WHITE).next_to(sum_fy_B[3], LEFT).shift(0.05*DOWN)))
        self.wait()
        # solve x axis of block B
        # Well we actually don't care about what the tension is.
        cross_out = Line(start=sum_fx_B.get_edge_center(LEFT), end=sum_fx_B.get_edge_center(RIGHT), color=YELLOW)
        self.play(ShowCreation(cross_out))
        self.wait()
        # solve y axis of block A
        self.play(FadeOut(sum_fy_A[:2]))
        self.wait()
        self.play(
            FadeOut(sum_fy_A[2]),
            FadeOut(sum_fy_A[5]),
            FadeOut(sum_fy_A[7])
        )
        two_mg = MathTex('2mg').scale(0.7).next_to(sum_fy_A[3], LEFT)
        self.play(
            Transform(sum_fy_A[6], two_mg),
            Transform(sum_fy_A[8], two_mg),
        )
        self.wait()
        # solve x axis of block A
        sum_fx_A_solved = MathTex(
            '\\Sigma F_x',
            '=',
            'ma_A',
            '=',
            '3\\mu mg',
            '-',
            'P'
        ).scale(0.7).to_edge(LEFT).shift(0.25*DOWN)
        sum_fx_A_solved[6].set_color(RED)
        self.play(
            ReplacementTransform(sum_fx_A[:4], sum_fx_A_solved[:4]),
            ReplacementTransform(sum_fx_A[4:7], sum_fx_A_solved[4]),
            ReplacementTransform(sum_fx_A[7], sum_fx_A_solved[5]),
            ReplacementTransform(sum_fx_A[8], sum_fx_A_solved[6])
        )
        self.wait()
        final_equation = MathTex(
            'a_A',
            '=',
            '3\\mu g',
            '-',
            '\\frac{P}{m}'
        ).scale(1.0).shift(2.1*DOWN)
        dividing_line_short = Line(start=1*DOWN, end=3*UP, color=GREY)
        self.play(
            Transform(dividing_line, dividing_line_short),
            Transform(sum_fx_A_solved, sum_fx_A_solved.copy().scale(1.0/0.7).shift(final_equation[1].get_center() - sum_fx_A_solved[3].get_center()))
        )
        self.play(FadeOut(sum_fx_A_solved[:2]))
        self.wait()
        self.play(
            *[Transform(sum_fx_A_solved[i+2], final_equation[i]) for i in range(5)]
        )
        self.wait()
        ansbox = SurroundingRectangle(final_equation, buff=0.25)
        self.play(ShowCreation(ansbox))
        self.wait()
        #endregion


class PartB(Scene):
    def construct(self):

        #region Diagram imagery
        block_A = Rectangle(
            color=TEAL,
            height=1.5,
            width=2.5,
            mark_paths_closed=True,
            close_new_points=True,
            stroke_width=4,
            fill_color=TEAL_DARK,
            fill_opacity=1
        ).shift(1*LEFT + 0.75*DOWN)
        block_B = Rectangle(
            color=GREEN,
            height=1.5,
            width=2.5,
            mark_paths_closed=True,
            close_new_points=True,
            stroke_width=4,
            fill_color=GREEN_DARK,
            fill_opacity=1
        ).next_to(block_A, UP, buff=0.02)
        text_A = Tex("A", color=WHITE).move_to(block_A.get_center()).scale(1.4)
        text_B = Tex("B", color=WHITE).move_to(block_B.get_center()).scale(1.4)

        A = Group(block_A, text_A)
        B = Group(block_B, text_B)

        floor = Line(start=3.5*LEFT, end=4.25*RIGHT, color=GREY).shift(A.get_edge_center(DOWN)[1]*UP)
        wall = Line(start=ORIGIN, end=3.5*UP, color=GREY).shift(floor.get_end())

        rope_tie_1 = Dot(
            color=YELLOW_A,
            radius=0.16
        ).move_to(B.get_edge_center(RIGHT))
        rope_tie_2 = Dot(
            color=YELLOW_A,
            radius=0.16
        ).move_to(A.get_edge_center(RIGHT))

        blockmid = (A.get_center() + B.get_center()) / 2
        pulley = Circle(
            radius=0.77,
            stroke_width=10.0,
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1.0
        ).shift(blockmid + 4*RIGHT)

        pulley_mount_points = [
            pulley.get_center(),
            np.array([wall.get_center()[0], blockmid[1]+0.4, 0]),
            np.array([wall.get_center()[0], blockmid[1]-0.4, 0])
        ]
        pulley_mount = Polygon(
            *pulley_mount_points,
            color=GREY_BLUE,
            fill_color=GREY_BLUE_DARK,
            fill_opacity=1.0,
            stroke_width=5.0
        )
        pulley_axle = Circle(
            arc_center=pulley.get_center(),
            radius=0.2,
            stroke_width=8.0,
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1.0
        )

        rope_1 = Line(
            start=rope_tie_1.get_center(),
            end=pulley.get_edge_center(UP),
            color=YELLOW_E,
            stroke_width=5.0
        )
        rope_2 = Line(
            start=rope_tie_2.get_center(),
            end=pulley.get_edge_center(DOWN),
            color=YELLOW_E,
            stroke_width=5.0
        )

        pull_force = Arrow(
            color=RED,
            buff=0,
            start=ORIGIN,
            end=2*LEFT
        ).next_to(A, LEFT, buff=0)
        force_label = MathTex("P", color=pull_force.get_color()).scale(1.4).next_to(pull_force, LEFT)

        diagram = Group(floor, wall, rope_1, rope_2, rope_tie_1, rope_tie_2, A, B, pulley, pulley_mount, pulley_axle, pull_force, force_label).move_to(ORIGIN)
        self.add(diagram)
        self.wait()
        #endregion

        #region Talk about pulleys
        mask = Rectangle(height=10, width=14, fill_color=BLACK, fill_opacity=0.6, stroke_opacity=0)
        self.play(Transform(diagram, diagram.copy().shift(1.5*UP)))
        self.play(FadeIn(mask))
        s_A_arrow = Arrow(
            color=GREEN,
            buff=0,
            start=rope_1.get_end(),
            end=rope_1.get_start()
        ).shift(0.2*UP)
        s_B_arrow = Arrow(
            color=GREEN,
            buff=0,
            start=rope_2.get_end(),
            end=rope_2.get_start()
        ).shift(0.2*DOWN)
        s_A_label = MathTex('s_A', color=GREEN).next_to(s_A_arrow, UP, buff=0)
        s_B_label = MathTex('s_B', color=GREEN).next_to(s_B_arrow, DOWN, buff=0)
        self.play(ShowCreation(s_A_arrow), Write(s_A_label))
        self.play(ShowCreation(s_B_arrow), Write(s_B_label))
        self.wait()
        cons_of_string_expr = MathTex('s_A', '+', 's_B', '=', 'L_{tot}').shift(DOWN)
        cons_of_string_expr[0].set_color(GREEN)
        cons_of_string_expr[2].set_color(GREEN)
        cons_of_string = Tex('"Conservation of string"', color=YELLOW).scale(0.75).next_to(cons_of_string_expr, DOWN)
        taking_the_double_deriv = Tex('Take the 2nd derivative $\\frac{d^2}{dt^2}$...', color=YELLOW).scale(0.75).next_to(cons_of_string_expr, DOWN)
        self.play(Write(cons_of_string_expr))
        self.play(Write(cons_of_string, run_time=1.0))
        self.wait()
        self.play(ReplacementTransform(cons_of_string, taking_the_double_deriv))
        dd_cons_of_string_expr = MathTex('a_A', '+', 'a_B', '=', '0').next_to(taking_the_double_deriv, DOWN, buff=0.4)
        highlight_box = SurroundingRectangle(dd_cons_of_string_expr, buff=0.2)
        self.play(Write(dd_cons_of_string_expr))
        self.play(ShowCreation(highlight_box))
        self.wait()
        self.play(
            FadeOut(mask),
            FadeOut(s_A_arrow),
            FadeOut(s_A_label),
            FadeOut(s_B_arrow),
            FadeOut(s_B_label),
            FadeOut(taking_the_double_deriv),
            FadeOut(cons_of_string_expr),
            FadeOut(highlight_box)
        )
        #endregion

        # Put the diagram away and prepare to work on the free body diagrams.
        # Need to copy before the diagram transformation to preserve the scale
        A_fbd = A.copy().move_to(ORIGIN).scale(0.55).shift(3.5*LEFT+0.5*UP)
        B_fbd = B.copy().move_to(ORIGIN).scale(0.55).shift(3.5*RIGHT+0.5*UP)
        dividing_line = Line(start=3*DOWN, end=2*UP, color=GREY)
        self.play(
            Transform(diagram, diagram.copy().scale(0.3).shift(2.0*LEFT+1.5*UP)),
            Transform(dd_cons_of_string_expr, dd_cons_of_string_expr.copy().scale(0.8).to_edge(UP, buff=0.5).shift(2*RIGHT))
        )
        self.play(ShowCreation(dividing_line))
        self.wait()

        #region Animate free body diagram for block A
        self.play(FadeIn(A_fbd))
        self.wait()
        P = Arrow(
            color=RED,
            buff=0,
            start=ORIGIN,
            end=1.5*LEFT,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).next_to(A_fbd, LEFT, buff=0)
        P_label = MathTex("P", color=P.get_color()).scale(0.8).next_to(P, LEFT)
        A_mg = Arrow(
            color=BLUE,
            buff=0,
            start=ORIGIN,
            end=1.0*DOWN,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(A_fbd.get_center()+0.1*LEFT)
        A_mg_label = MathTex("mg", color=A_mg.get_color()).scale(0.8).next_to(A_mg, LEFT, aligned_edge=DOWN)
        normal_A_1 = Arrow(
            color=PURPLE,
            buff=0,
            start=ORIGIN,
            end=0.8*UP,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).next_to(A_fbd, DOWN, buff=0).shift(0.1*RIGHT)
        normal_A_1_label = MathTex("N_1", color=normal_A_1.get_color()).scale(0.8).next_to(normal_A_1, RIGHT, buff=0, aligned_edge=DOWN)
        normal_A_2 = Arrow(
            color=PURPLE,
            buff=0,
            start=ORIGIN,
            end=0.8*DOWN,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).next_to(A_fbd, UP, buff=0)
        normal_A_2_label = MathTex("N_2", color=normal_A_2.get_color()).scale(0.8).next_to(normal_A_2, RIGHT, buff=0, aligned_edge=UP)
        fric_A_1 = Arrow(
            color=MAROON,
            buff=0,
            start=ORIGIN,
            end=1.5*RIGHT,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(A_fbd.get_edge_center(DOWN))
        fric_A_1_label = MathTex("F_{f1}", color=fric_A_1.get_color()).scale(0.8).next_to(fric_A_1, RIGHT)
        fric_A_2 = Arrow(
            color=MAROON,
            buff=0,
            start=ORIGIN,
            end=1.5*RIGHT,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(A_fbd.get_edge_center(UP))
        fric_A_2_label = MathTex("F_{f2}", color=fric_A_2.get_color()).scale(0.8).next_to(fric_A_2, RIGHT)
        tension_A = Arrow(
            color=RED,
            buff=0,
            start=ORIGIN,
            end=1.5*RIGHT,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(A_fbd.get_edge_center(RIGHT))
        tension_A_label = MathTex("T", color=tension_A.get_color()).scale(0.8).next_to(tension_A, RIGHT)

        # same as part A but with tension
        self.play(
            Write(P),
            Write(P_label),
            Write(A_mg),
            Write(A_mg_label),
            Write(normal_A_1),
            Write(normal_A_1_label),
            Write(normal_A_2),
            Write(normal_A_2_label),
            Write(fric_A_1),
            Write(fric_A_1_label),
            Write(fric_A_2),
            Write(fric_A_2_label)
        )
        self.wait()
        self.play(
            Write(tension_A),
            Write(tension_A_label)
        )
        #endregion

        #region 2nd law for block A
        sum_fx_A = MathTex(
            '\\Sigma F_x',
            '=',
            'ma_A',
            '=',
            '\\mu N_1',
            '+',
            '\\mu N_2',
            '-',
            'P',
            '+',
            'T'
        ).scale(0.7).to_edge(LEFT).shift(1.25*DOWN)
        sum_fx_A[0].set_color(YELLOW)
        sum_fx_A[4].set_color(MAROON)
        sum_fx_A[6].set_color(MAROON)
        sum_fx_A[8].set_color(RED)
        sum_fx_A[10].set_color(RED)
        sum_fy_A = MathTex(
            '\\Sigma F_y',
            '=',
            '0',
            '=',
            'N_1',
            '-',
            'N_2',
            '-',
            'mg',
        ).scale(0.7).next_to(sum_fx_A, DOWN, aligned_edge=LEFT)
        sum_fy_A[0].set_color(YELLOW)
        sum_fy_A[4].set_color(PURPLE)
        sum_fy_A[6].set_color(PURPLE)
        sum_fy_A[8].set_color(BLUE)
        self.play(Write(sum_fx_A))
        self.wait()
        self.play(Write(sum_fy_A))
        self.wait()
        #endregion

        #region Animate free body diagram for block B
        self.play(FadeIn(B_fbd))
        self.wait()
        B_mg = Arrow(
            color=BLUE,
            buff=0,
            start=ORIGIN,
            end=1.0*DOWN,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(B_fbd.get_center()+0.1*LEFT)
        B_mg_label = MathTex("mg", color=B_mg.get_color()).scale(0.8).next_to(B_mg, LEFT, aligned_edge=DOWN)
        normal_B_2 = Arrow(
            color=PURPLE,
            buff=0,
            start=ORIGIN,
            end=0.8*UP,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).next_to(B_fbd, DOWN, buff=0).shift(0.1*RIGHT)
        normal_B_2_label = MathTex("N_2", color=normal_B_2.get_color()).scale(0.8).next_to(normal_B_2, RIGHT, buff=0, aligned_edge=DOWN)
        fric_B_2 = Arrow(
            color=MAROON,
            buff=0,
            start=ORIGIN,
            end=1.5*LEFT,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(B_fbd.get_edge_center(DOWN))
        fric_B_2_label = MathTex("F_{f2}", color=fric_B_2.get_color()).scale(0.8).next_to(fric_B_2, LEFT)
        tension_B = Arrow(
            color=RED,
            buff=0,
            start=ORIGIN,
            end=1.5*RIGHT,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).next_to(B_fbd, RIGHT, buff=0)
        tension_B_label = MathTex("T", color=tension_B.get_color()).scale(0.8).next_to(tension_B, RIGHT)

        self.play(
            Write(B_mg),
            Write(B_mg_label),
            Write(normal_B_2),
            Write(normal_B_2_label),
            Write(fric_B_2),
            Write(fric_B_2_label),
            Write(tension_B),
            Write(tension_B_label)
        )
        self.wait()
        #endregion

        #region 2nd law for block B
        sum_fx_B = MathTex(
            '\\Sigma F_x',
            '=',
            'ma_B',
            '=',
            'T',
            '-',
            '\\mu N_2',
        ).scale(0.7).next_to(ORIGIN, RIGHT).shift(1.25*DOWN + 0.25*RIGHT)
        sum_fx_B[0].set_color(YELLOW)
        sum_fx_B[4].set_color(RED)
        sum_fx_B[6].set_color(MAROON)
        sum_fy_B = MathTex(
            '\\Sigma F_y',
            '=',
            '0',
            '=',
            'N_2',
            '-',
            'mg',
        ).scale(0.7).next_to(sum_fx_B, DOWN, aligned_edge=LEFT)
        sum_fy_B[0].set_color(YELLOW)
        sum_fy_B[4].set_color(PURPLE)
        sum_fy_B[6].set_color(BLUE)
        self.play(
            Write(sum_fx_B),
            Write(sum_fy_B)
        )
        self.wait()
        highlight_box = SurroundingRectangle(sum_fx_B[2], buff=0.1)
        self.play(ShowCreation(highlight_box))
        self.wait()
        self.play(FadeOut(highlight_box))
        self.wait()
        #endregion

        #region Math it out
        # solve y axis of block B
        self.play(
            FadeOut(sum_fy_B[:2]),
            FadeOut(sum_fy_B[2]),
            FadeOut(sum_fy_B[5])
        )
        self.play(Transform(sum_fy_B[-1], sum_fy_B[-1].copy().set_color(WHITE).next_to(sum_fy_B[3], LEFT).shift(0.05*DOWN)))
        sum_fy_B_result = Group(sum_fy_B[-1], sum_fy_B[3:5])
        self.wait()
        self.play(Transform(sum_fy_B_result, sum_fy_B_result.copy().next_to(dd_cons_of_string_expr, DOWN, aligned_edge=LEFT)))
        self.wait()
        # solve y axis of block A
        self.play(
            FadeOut(sum_fy_A[:2]),
            FadeOut(sum_fy_A[2]),
            FadeOut(sum_fy_A[5]),
            FadeOut(sum_fy_A[7])
        )
        two_mg = MathTex('2mg').scale(0.7).next_to(sum_fy_A[3], LEFT)
        self.play(
            ReplacementTransform(sum_fy_A[6], two_mg),
            ReplacementTransform(sum_fy_A[8], two_mg),
        )
        sum_fy_A_result = Group(two_mg, sum_fy_A[3:5])
        self.wait()
        self.play(Transform(sum_fy_A_result, sum_fy_A_result.copy().next_to(sum_fy_B_result, DOWN, aligned_edge=LEFT)))
        self.wait()
        # solve x axis of each.
        self.play(FadeOut(sum_fx_A[:2]), FadeOut(sum_fx_B[:2]))
        sum_fx_A = sum_fx_A[2:]
        sum_fx_B = sum_fx_B[2:]
        highlight_box = SurroundingRectangle(dd_cons_of_string_expr, buff=0.1)
        self.play(ShowCreation(highlight_box))
        self.wait()
        self.play(FadeOut(highlight_box))
        sum_fx_B_subbed = MathTex(
            'm(-a_A)',
            '=',
            'T',
            '-',
            '\\mu N_2',
        ).scale(0.7)
        sum_fx_B_subbed.shift(sum_fx_B[1].get_center() - sum_fx_B_subbed[1].get_center())
        sum_fx_B_subbed2 = MathTex(
            'ma_A',
            '=',
            '-T',
            '+',
            '\\mu N_2',
        ).scale(0.7)
        sum_fx_B_subbed2.shift(sum_fx_B[1].get_center() - sum_fx_B_subbed2[1].get_center())
        sum_fx_B_subbed[2].set_color(RED)
        sum_fx_B_subbed[4].set_color(MAROON)
        sum_fx_B_subbed2[2].set_color(RED)
        sum_fx_B_subbed2[4].set_color(MAROON)
        self.play(*[ReplacementTransform(sum_fx_B[i], sum_fx_B_subbed[i]) for i in range(5)])
        self.wait()
        self.play(*[ReplacementTransform(sum_fx_B_subbed[i], sum_fx_B_subbed2[i]) for i in range(5)])
        self.wait()

        dividing_line_short = Line(start=DOWN, end=2*UP, color=GREY)
        self.play(Transform(dividing_line, dividing_line_short))

        x_equated = MathTex(
            'ma_A',
            '=',
            '\\mu N_1',
            '+',
            '\\mu N_2',
            '-',
            'P',
            '+',
            'T',
            '=',
            '-T',
            '+',
            '\\mu N_2',
            '\\Rightarrow',
            'T=\\frac{P}{2}-\\mu mg'
        ).scale(0.8).shift(2*DOWN)
        x_equated[2].set_color(MAROON)
        x_equated[4].set_color(MAROON)
        x_equated[6].set_color(RED)
        x_equated[8].set_color(RED)
        x_equated[10].set_color(RED)
        x_equated[12].set_color(MAROON)
        x_equated[-1].set_color(YELLOW)

        x_equated_subbed = MathTex(
            'ma_A',
            '=',
            '2\\mu mg',
            '+',
            '\\mu mg',
            '-',
            'P',
            '+',
            'T',
            '=',
            '-T',
            '+',
            '\\mu mg',
            '\\Rightarrow',
            'T=\\frac{P}{2}-\\mu mg'
        ).scale(0.8).shift(2*DOWN)
        x_equated_subbed[2].set_color(MAROON)
        x_equated_subbed[4].set_color(MAROON)
        x_equated_subbed[6].set_color(RED)
        x_equated_subbed[8].set_color(RED)
        x_equated_subbed[10].set_color(RED)
        x_equated_subbed[12].set_color(MAROON)
        x_equated_subbed[-1].set_color(YELLOW)

        self.play(Write(x_equated[:-2]))
        self.wait()
        self.play(*[ReplacementTransform(x_equated[i], x_equated_subbed[i]) for i in range(len(x_equated)-2)])
        self.wait()
        self.play(FadeOut(x_equated_subbed[:2]))
        self.play(Write(x_equated_subbed[-2:]))
        self.wait()
        ans = MathTex('a_A=\\frac{-P}{2m}+2\\mu g').next_to(x_equated_subbed, DOWN)
        self.play(Write(ans))
        ansbox = SurroundingRectangle(ans, buff=0.2)
        self.play(ShowCreation(ansbox))
        self.wait()
        #endregion