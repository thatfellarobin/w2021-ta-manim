from manim import *
import numpy as np

TEAL_DARK = '#1c4037'
GREEN_DARK = '#2b4022'

class PartA(Scene):
    def construct(self):
        # Scene imagery
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
        force_label = MathTex("P", color=RED).scale(1.4).next_to(pull_force, LEFT)

        diagram = Group(floor, wall, rope, rope_tie_1, rope_tie_2, A, B, pull_force, force_label).move_to(ORIGIN)



        self.add(diagram)
        self.wait()


class PartB(Scene):
    def construct(self):
        pass
        # Scene imagery