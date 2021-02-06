from manim import *
import numpy as np

class T4P3(Scene):
    def construct(self):
        def path_function(x):
            scale_y = 4
            scale_x = 2
            y = scale_y * ((np.cos(x) + 0.5) / 2)
            return np.array([scale_x * x, y, 0])

        path_1 = ParametricFunction(path_function, t_min=0, t_max=PI, fill_opacity=0)
        path_2 = Arc(
            start_angle=-PI/2,
            angle=PI,
            radius=1.5
        )
        path_2.shift(path_1.get_end() - path_2.get_start())
        path_3 = Arc(
            start_angle=PI/2,
            angle=PI,
            radius=1.5
        )
        path_3.shift(path_2.get_end() - path_3.get_start())

        path = path_1.copy()
        path.add_points_as_corners(path_2.get_all_points())
        path.add_points_as_corners(path_3.get_all_points())
        path.set_color(PURPLE_A)
        path.shift(5*LEFT+2*DOWN)

        ground = Line(
            start=path.get_start()+4*DOWN+0.25*LEFT,
            end=path.get_end()+LEFT,
            color=GREY
        )
        h_arrow = DoubleArrow(
            start=path.get_start(),
            end=path.get_start()+4*DOWN,
            color=GREEN,
            buff=0.1,
            stroke_width=6,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        h_annot = MathTex('h', color=GREEN).scale(0.7).next_to(h_arrow, LEFT, buff=0.15)
        rho_arrow = Arrow(
            start=path.get_end()+1.5*UP,
            end=path.get_end()+1.5*UP+1.5*np.array([np.cos(PI/4), np.sin(PI/4), 0]),
            color=GREEN,
            buff=0,
            stroke_width=6,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        rho_annot = MathTex('\\rho', color=GREEN).scale(0.7).next_to(rho_arrow.get_end(), np.array([np.cos(PI/4), np.sin(PI/4), 0]), buff=0.15)

        self.play(ShowCreation(ground))
        self.play(ShowCreation(path), run_time=3)
        self.wait()
        self.play(
            Write(h_arrow),
            Write(h_annot),
            Write(rho_arrow),
            Write(rho_annot)
        )
        self.wait()

        car = Dot(
            point=path.get_end()+3*UP,
            radius=0.15,
            color=GREEN
        )
        self.play(FadeIn(car))
        for _ in range(2):
            self.play(Flash(car))

        pass