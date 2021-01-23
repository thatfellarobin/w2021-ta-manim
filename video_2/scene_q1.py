from manim import *
import numpy as np


class P1(Scene):

    def construct(self):
        # Scene imagery
        diagram_scale = 0.04
        d = 100 * diagram_scale
        rho = 80 * diagram_scale
        path_1 = Line(start=ORIGIN, end=d*LEFT, color=GREY).shift(2.5*UP + 2*RIGHT)
        path_2 = Arc(radius=rho, start_angle=TAU/4, angle=TAU/4, color=GREY).next_to(path_1, direction=LEFT, buff=0, aligned_edge=UP)
        car = Dot(point=ORIGIN, color=YELLOW).move_to(path_1.get_start())
        path = path_1.copy()
        path.append_vectorized_mobject(path_2)

        # Annotations
        starting_line = Line(start=ORIGIN, end=0.4*DOWN, color=GREEN).next_to(path_1.get_start(), DOWN)
        s_arrow = Arrow(start=path.get_start(), end=path.get_start(), buff=0, color=GREEN)
        s_arrow_label = MathTex('s', color=GREEN).next_to(starting_line, RIGHT)

        # time functions
        a = MathTex("a_t(t)", "=", "0.015t^2", color=RED).scale(0.9).shift(1.5*UP)
        v = MathTex("v(t)", "=", "\\int a_t(t)\\,dt", "=", "0.005t^3 + v_0", color=BLUE).scale(0.9).next_to(a, DOWN, aligned_edge=LEFT)
        s = MathTex("s(t)", "=", "\\int v(t)\\,dt", "=", "0.00125t^4 + v_0t + s_0", color=GREEN).scale(0.9).next_to(v, DOWN, aligned_edge=LEFT)
        # time functions after solving init conditions
        v_final = MathTex("v(t)", "=", "0.005t^3", color=BLUE).scale(0.9)
        v_final.shift(v[0].get_center() - v_final[0].get_center())
        s_final = MathTex("s(t)", "=", "0.00125t^4", color=GREEN).scale(0.9)
        s_final.shift(s[0].get_center() - s_final[0].get_center())
        # time functions after substitution
        s_subbed = MathTex("s(18)", "=", "131.22\\,\\mathrm{m}", color=GREEN).scale(0.9).align_to(s_final, direction=LEFT, alignment_vect=UP)
        v_subbed = MathTex("v(t)", "=", "29.16\\,\\mathrm{m/s^2}", color=BLUE).scale(0.9).align_to(v_final, direction=LEFT, alignment_vect=UP)

        # Initial conditions
        initcond_prose = Tex('"Originally at rest at $s=0$"', color=YELLOW).scale(0.8).next_to(s_final, DOWN, aligned_edge=LEFT, buff=2*DEFAULT_MOBJECT_TO_MOBJECT_BUFFER)
        initcond = Tex("$s(0)=0$, $v(0)=0$", color=YELLOW).scale(0.8).next_to(initcond_prose, DOWN, aligned_edge=LEFT)


        # Updater Functions
        def s_arrow_updater(s_arrow):
            # Warning: only works in the straight part of the path.
            start = starting_line.get_center()
            end = (car.get_center() - path.get_start()) + start
            # New arrow
            new_s_arrow = Arrow(
                start=start,
                end=end,
                buff=0,
                max_stroke_width_to_length_ratio=999,
                max_tip_length_to_length_ratio=1,
                color=GREEN
            )
            s_arrow.become(new_s_arrow)



        # set up
        self.add(path, car)
        self.wait()

        # Explain diff parts of the scene
        self.play(Flash(car))
        self.play(Flash(car))
        self.wait()
        self.play(ShowPassingFlash(path.copy().set_color(YELLOW)))
        self.play(ShowPassingFlash(path.copy().set_color(YELLOW)))
        self.wait()

        # Explain how s is measured
        self.play(
            FadeIn(starting_line),
            FadeIn(s_arrow_label)
        )
        s_arrow.add_updater(s_arrow_updater)
        self.add(s_arrow)
        self.play(MoveAlongPath(car, path_1), run_time=4, rate_func=there_and_back)
        s_arrow.clear_updaters()
        self.remove(s_arrow)
        self.wait(0.5)
        self.play(
            FadeOut(starting_line),
            FadeOut(s_arrow_label)
        )
        self.wait()

        # Go through math for time functions
        self.play(Write(a))
        self.wait()
        self.play(Write(v))
        self.wait()
        self.play(Write(s))
        self.wait()

        # Go through initial conditions
        self.play(Write(initcond_prose))
        self.wait()
        self.play(Write(initcond))
        self.wait()
        self.play(
            FadeOut(v[2]),
            FadeOut(v[3]),
            FadeOut(s[2]),
            FadeOut(s[3])
        )
        self.play(
            ReplacementTransform(v[0], v_final[0]),
            ReplacementTransform(v[1], v_final[1]),
            ReplacementTransform(v[4], v_final[2]),
            ReplacementTransform(s[0], s_final[0]),
            ReplacementTransform(s[1], s_final[1]),
            ReplacementTransform(s[4], s_final[2])
        )
        self.wait()

        # Figure out where it is at t1


