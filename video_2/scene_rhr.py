from manim import *
import numpy as np
import cv2


class RHR(Scene):
    def construct(self):
        # TODO: need to make this animation a little richer.

        title = Tex('\\textbf{The Right Hand Rule}').scale(1.2).shift(3 * UP)

        text = Tex('How do we describe a', 'rotation as a vector?')
        text[1].next_to(text[0], direction=DOWN, aligned_edge=LEFT).set_color(YELLOW)
        text.shift(5 * RIGHT + 1 * UP)

        text2 = Tex('How do we know the resulting', 'direction of a cross product?').next_to(text, direction=DOWN, aligned_edge=LEFT)
        text2[1].next_to(text2[0], direction=DOWN, aligned_edge=LEFT).set_color(YELLOW)
        text2.shift(0.5 * DOWN)

        rhr = ImageMobject('assets/rhr.png', invert=True).scale(0.25).shift(0.5*DOWN + 3*LEFT)

        self.play(Write(title))
        self.play(FadeIn(rhr))
        self.wait()
        self.play(Write(text))
        self.wait()
        self.play(Write(text2))
        self.wait()

class RHR3D(ThreeDScene):
    # Wow, manim sucks for 3D animations. give up on this.

    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        x = Vector(direction=[1, 0, 0], color=BLUE).set_shade_in_3d()
        x_label = MathTex('x', color=x.get_color()).next_to(x, direction=x.get_unit_vector()).set_shade_in_3d()
        y = Vector(direction=[0, 1, 0], color=GREEN).set_shade_in_3d()
        y_label = MathTex('y', color=y.get_color()).next_to(y, direction=y.get_unit_vector()).set_shade_in_3d()
        z = Vector(direction=[0, 0, 1], color=BLUE).set_shade_in_3d()
        z_label = MathTex('z', color=z.get_color()).next_to(z, direction=z.get_unit_vector()).set_shade_in_3d()

        self.begin_ambient_camera_rotation(rate=0.08)
        self.play(FadeIn(axes))
        self.play(
            ShowCreation(x),
            ShowCreation(y),
            ShowCreation(z)
            )
        self.play(
            ShowCreation(x_label),
            ShowCreation(y_label),
            ShowCreation(z_label)
            )
        self.wait(3)
