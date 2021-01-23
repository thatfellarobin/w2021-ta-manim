from manim import *
import numpy as np
import cv2


class RHR(Scene):
    def construct(self):
        title = Tex('\\textbf{The Right Hand Rule}').scale(1.2).shift(3 * UP)

        text = Tex('How do we describe a', 'rotation as a vector?')
        text[1].next_to(text[0], direction=DOWN, aligned_edge=LEFT).set_color(YELLOW)
        text.shift(5 * RIGHT + 1 * UP)

        text2 = Tex('How do we know the resulting', 'direction of a cross product?').next_to(text, direction=DOWN, aligned_edge=LEFT)
        text2[1].next_to(text2[0], direction=DOWN, aligned_edge=LEFT).set_color(YELLOW)
        text2.shift(0.5 * DOWN)

        rhr = ImageMobject('assets/rhr.png', invert=True).scale(0.25).shift(0.5 * DOWN + 3 * LEFT)

        self.play(Write(title))
        self.wait()
        self.play(Write(text))
        self.wait()
        self.play(Write(text2))
        self.wait()
        self.play(FadeIn(rhr))
        self.wait()
