from manim import *
import numpy as np

class PartA(Scene):
    def construct(self):
        # Scene imagery
        BlockA = Rectangle(
            color=TEAL,
            height=2.0,
            width=4.0,
            mark_paths_closed=True,
            close_new_points=True,
        ).shift(2*LEFT + 1*UP)
        BlockB = Rectangle(
            color=GREEN,
            height=2.0,
            width=4.0,
            mark_paths_closed=True,
            close_new_points=True,
        ).shift(2*LEFT + 1*DOWN)


        self.add(BlockA, BlockB)
        self.wait()


class PartB(Scene):
    def construct(self):
        # Scene imagery