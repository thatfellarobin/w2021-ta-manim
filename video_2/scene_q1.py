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
        a_cent = MathTex("a_c(t)", "=", "\\frac{v^2}{\\rho}", color=PURPLE).scale(0.9).next_to(a, DOWN, aligned_edge=LEFT)
        # time functions after solving init conditions
        v_final = MathTex("v(t)", "=", "0.005t^3", color=BLUE).scale(0.9)
        v_final.shift(v[0].get_center() - v_final[0].get_center())
        s_final = MathTex("s(t)", "=", "0.00125t^4", color=GREEN).scale(0.9)
        s_final.shift(s[0].get_center() - s_final[0].get_center())
        # time functions after substitution
        a_subbed = MathTex("a_t(18\\,\\mathrm{s})", "=", "4.86\\,\\mathrm{m/s^2}", color=RED).scale(0.9)
        a_subbed.shift(a[0].get_center() - a_subbed[0].get_center()).align_to(a, LEFT)
        s_subbed = MathTex("s(18\\,\\mathrm{s})", "=", "131.22\\,\\mathrm{m}", color=GREEN).scale(0.9)
        s_subbed.shift(s_final[0].get_center() - s_subbed[0].get_center()).align_to(s_final, LEFT)
        v_subbed = MathTex("v(18\\,\\mathrm{s})", "=", "29.16\\,\\mathrm{m/s^2}", color=BLUE).scale(0.9)
        v_subbed.shift(v_final[0].get_center() - v_subbed[0].get_center()).align_to(v_final, LEFT)
        a_cent_subbed = MathTex("a_c(18\\,\\mathrm{s})", "=", "10.629\\,\\mathrm{m/s^2}", color=PURPLE).scale(0.9)
        a_cent_subbed.shift(a_cent[0].get_center() - a_cent_subbed[0].get_center()).align_to(a_cent, LEFT)
        a_tot = MathTex("|a|=\\sqrt{a_t^2 + a_c^2}", "=11.687\\,\\mathrm{m/s^2}", color=MAROON).scale(0.9).next_to(a_cent_subbed, direction=DOWN, aligned_edge=LEFT)

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
        self.add_foreground_mobject(car)
        self.add(path)
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
        self.play(
            FadeOut(initcond_prose),
            FadeOut(initcond),
            Transform(a, a.copy().set_opacity(0.25)),
            Transform(v_final, v_final.copy().set_opacity(0.25)),
            ReplacementTransform(s_final[0], s_subbed[0]),
            ReplacementTransform(s_final[1], s_subbed[1]),
            ReplacementTransform(s_final[2], s_subbed[2])
        )
        self.wait()
        t1_arc_angle = 31.22 / 80
        t1_arc = Arc(radius = rho, start_angle=TAU/4, angle=t1_arc_angle).move_arc_center_to(path_2.get_arc_center())
        t1_joinedpath = path_1.copy()
        t1_joinedpath.append_vectorized_mobject(t1_arc)
        t1_joinedpath.set_opacity(0)
        self.add(t1_joinedpath)
        self.play(MoveAlongPath(car, t1_joinedpath, run_time=2))
        self.play(Flash(car))

        # Find velocity magnitude at t1
        self.play(
            Transform(v_final, v_final.copy().set_opacity(1)),
            FadeOut(s_subbed)
        )
        self.wait()
        self.play(
            ReplacementTransform(v_final[0], v_subbed[0]),
            ReplacementTransform(v_final[1], v_subbed[1]),
            ReplacementTransform(v_final[2], v_subbed[2])
        )
        self.wait()

        # Show the two components of acceleration and the result
        self.play(
            FadeOut(v_subbed)
        )
        a_vect_scale = 0.2
        a_tan_value = 4.86 * a_vect_scale
        a_cent_value = 10.629 * a_vect_scale
        tan_angle = PI + t1_arc_angle
        a_tan_vect = a_tan_value * np.array([np.cos(tan_angle), np.sin(tan_angle), 0])
        a_cent_vect = a_cent_value * np.array([np.cos(tan_angle + PI/2), np.sin(tan_angle + PI/2), 0])
        a_tan_arrow = Line(
            start=car.get_center(),
            end=car.get_center()+a_tan_vect,
            buff=0,
            stroke_width=3,
            color=RED,
            max_stroke_width_to_length_ratio=999
        ).add_tip(tip_length=0.2)
        a_cent_arrow = Line(
            start=car.get_center(),
            end=car.get_center()+a_cent_vect,
            buff=0,
            stroke_width=3,
            color=PURPLE,
            max_stroke_width_to_length_ratio=999
        ).add_tip(tip_length=0.2)
        a_tot_arrow = Line(
            start=car.get_center(),
            end=car.get_center()+a_tan_vect+a_cent_vect,
            buff=0,
            stroke_width=3,
            color=MAROON,
            max_stroke_width_to_length_ratio=999
        ).add_tip(tip_length=0.2)
        self.play(
            ShowCreation(a_tan_arrow),
            Transform(a, a.copy().set_opacity(1)),
            )
        self.wait()
        self.play(
            ReplacementTransform(a[0], a_subbed[0]),
            ReplacementTransform(a[1], a_subbed[1]),
            ReplacementTransform(a[2], a_subbed[2])
        )
        self.wait()
        self.play(ShowCreation(a_cent_arrow))
        self.play(Write(a_cent))
        self.wait()
        self.play(
            ReplacementTransform(a_cent[0], a_cent_subbed[0]),
            ReplacementTransform(a_cent[1], a_cent_subbed[1]),
            ReplacementTransform(a_cent[2], a_cent_subbed[2])
        )
        self.wait()

        # Show the final acceleration
        self.play(
            Transform(a_tan_arrow, a_tan_arrow.copy().set_opacity(0.25)),
            Transform(a_cent_arrow, a_cent_arrow.copy().set_opacity(0.25)),
            Transform(a_subbed, a_subbed.copy().set_opacity(0.5)),
            Transform(a_cent_subbed, a_cent_subbed.copy().set_opacity(0.5)),
            ShowCreation(a_tot_arrow)
        )
        self.wait()
        self.play(Write(a_tot[0]))
        self.wait()
        self.play(Write(a_tot[1]))
        self.wait()





