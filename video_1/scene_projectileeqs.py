from manim import *
import numpy as np


class PM_Equations(Scene):
    def construct(self):
        # Table
        title = Tex("\\textbf{Helpful Projectile Motion Equations}", color=YELLOW).shift(3 * UP).scale(1.1)
        header_x = Tex("\\textbf{Horizontal Axis}").shift(3.5 * LEFT + 2 * UP)
        header_y = Tex("\\textbf{Vertical Axis}").shift(3.5 * RIGHT + 2 * UP)
        divline = Line(2.25 * UP, 1.75 * DOWN)
        divline2 = Line(1.75 * DOWN - 3 * LEFT, 1.75 * DOWN + 3 * LEFT)

        eq_x_1 = MathTex("x = x_0 + v_{x0}t").shift(3.5 * LEFT + 1 * UP)

        eq_y_1 = MathTex("y = y_0 + v_{y0}t + \\frac{1}{2}gt^2").shift(3.5 * RIGHT + 1 * UP)
        eq_y_2 = MathTex("v_{y} = v_{y0} + gt").shift(3.5 * RIGHT + 0 * UP)
        eq_y_3 = MathTex("v_{y}^2 = v_{y0}^2 + 2g(y-y_0)").shift(3.5 * RIGHT + -1 * UP)

        # List Assumptions
        assumptions = Tex("\\textbf{Key Assumptions:}", color=RED).shift(3 * LEFT + 2.25 * DOWN).scale(0.9)
        assume_1 = MathTex("g=-9.8\\,\\mathrm{m/s^2}").shift(1.25 * RIGHT + 2.25 * DOWN)
        assume_2 = Tex("No forces other than gravity").shift(3 * DOWN).align_to(assume_1, LEFT)

        # Highlighting Boxes
        eq_x_1_box = SurroundingRectangle(eq_x_1, buff=.1)
        eq_y_1_box = SurroundingRectangle(eq_y_1, buff=.1)
        eq_y_2_box = SurroundingRectangle(eq_y_2, buff=.1)
        eq_y_3_box = SurroundingRectangle(eq_y_3, buff=.1)
        assume_box = SurroundingRectangle(Group(assume_1, assume_2), buff=.15)

        # Animate
        self.play(
            *[Write(i) for i in [
                title,
                header_x,
                header_y,
                divline,
                eq_x_1,
                eq_y_1,
                eq_y_2,
                eq_y_3,
                assumptions,
                assume_1,
                assume_2
                ]],
            GrowFromCenter(divline2)
        )
        self.wait()
        self.play(ShowCreation(eq_x_1_box))
        self.wait()
        self.play(ReplacementTransform(eq_x_1_box, eq_y_1_box))
        self.wait()
        self.play(ReplacementTransform(eq_y_1_box, eq_y_2_box))
        self.wait()
        self.play(ReplacementTransform(eq_y_2_box, eq_y_3_box))
        self.wait()
        self.play(ReplacementTransform(eq_y_3_box, assume_box))
        self.wait()
