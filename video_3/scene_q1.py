from manim import *
import numpy as np

TEAL_DARK = '#1c4037'
GREEN_DARK = '#2b4022'

class PartA(Scene):
    def construct(self):
        ## Diagram imagery
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
            color=YELLOW_A
        ).move_to(B.get_edge_center(RIGHT))
        rope_tie_2 = Dot(
            color=YELLOW_A
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

        # Need to copy before the diagram transformation to preserve the scale
        A_fbd = A.copy().move_to(ORIGIN).scale(0.55).shift(3.5*LEFT+1.5*UP)
        B_fbd = B.copy().move_to(ORIGIN).scale(0.55).shift(3.5*RIGHT+1.5*UP)

        self.add(diagram)
        self.wait()

        dividing_line = Line(start=3*DOWN, end=3*UP, color=GREY)

        self.play(Transform(diagram, diagram.copy().scale(0.3).shift(5*LEFT+3*UP)))
        self.play(ShowCreation(dividing_line))
        self.wait()

        # Animate free body diagram for block A
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
        self.play(Write(normal_A_1), Write(normal_A_1_label))
        self.wait()
        self.play(Write(normal_A_2), Write(normal_A_2_label))
        self.wait()
        self.play(Write(fric_A_1), Write(fric_A_1_label))
        self.wait()
        self.play(Write(fric_A_2), Write(fric_A_2_label))
        self.wait()

        # Animate free body diagram for block B
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

class PartB(Scene):
    def construct(self):
        pass
        # Scene imagery