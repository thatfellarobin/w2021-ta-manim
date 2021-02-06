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
        path_partial = path.copy()
        path.add_points_as_corners(path_3.get_all_points())
        path.set_color(PURPLE_A)
        path_partial.shift(5.5*LEFT+2*DOWN)
        path.shift(5.5*LEFT+2*DOWN)

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
        self.play(ShowCreation(path), run_time=2)
        self.wait()
        self.play(
            Write(h_arrow),
            Write(h_annot),
            Write(rho_arrow),
            Write(rho_annot)
        )
        self.wait()

        car = Dot(
            point=path.get_start(),
            radius=0.15,
            color=TEAL
        )
        vel_init_arrow = Arrow(
            start=car.get_center()+0.15*RIGHT,
            end=car.get_center()+1.25*RIGHT,
            color=RED,
            buff=0,
            stroke_width=7,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        vel_init_arrow_label = MathTex('v_0', color=RED).scale(0.8).next_to(vel_init_arrow.get_end(), RIGHT, buff=0.15)
        self.play(
            FadeIn(car),
            Write(vel_init_arrow),
            Write(vel_init_arrow_label)
        )
        self.wait()
        self.play(MoveAlongPath(car, path_partial, run_time=3))
        for _ in range(2):
            self.play(Flash(car))
        self.wait()

        vel_arrow = Arrow(
            start=car.get_center()+0.15*LEFT,
            end=car.get_center()+1.25*LEFT,
            color=RED,
            buff=0,
            stroke_width=7,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        vel_arrow_label = MathTex('v_1', color=RED).scale(0.8).next_to(vel_arrow.get_end(), LEFT, buff=0.15)
        self.play(
            Write(vel_arrow),
            Write(vel_arrow_label)
        )
        self.wait()

        # Free body diagram
        car_fbd = car.copy().move_to(5*RIGHT+1*DOWN)
        tan_dir = Line(
            start=car_fbd.get_center(),
            end=car_fbd.get_center()+LEFT,
            color=YELLOW_A,
            stroke_width=4,
        )
        tan_dir_label = MathTex('+t', color=YELLOW_A).scale(0.8).next_to(tan_dir.get_end(), LEFT, buff=0.1)
        norm_dir = Line(
            start=car_fbd.get_center(),
            end=car_fbd.get_center()+1.5*DOWN,
            color=YELLOW_A,
            stroke_width=4,
        )
        norm_dir_label = MathTex('+n', color=YELLOW_A).scale(0.8).next_to(norm_dir.get_end(), DOWN, buff=0.1)
        N_arrow = Arrow(
            start=car_fbd.get_center()+1.15*UP,
            end=car_fbd.get_center()+0.15*UP,
            color=PURPLE,
            buff=0,
            stroke_width=7,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        N_arrow_label = MathTex('N', color=PURPLE).scale(0.8).next_to(N_arrow.get_start(), UP, buff=0.1)
        mg_arrow = Arrow(
            start=car_fbd.get_center()+0.15*DOWN,
            end=car_fbd.get_center()+1.15*DOWN,
            color=BLUE,
            buff=0,
            stroke_width=7,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        mg_arrow_label = MathTex('mg', color=BLUE).scale(0.8).next_to(mg_arrow.get_end(), RIGHT, buff=0.2)
        self.play(
            ShowCreation(tan_dir),
            ShowCreation(norm_dir),
            Write(tan_dir_label),
            Write(norm_dir_label),
            FadeIn(car_fbd),
            Write(N_arrow),
            Write(N_arrow_label),
            Write(mg_arrow),
            Write(mg_arrow_label)
        )
        self.wait()

        # normal acceleration
        accel = MathTex(
            'ma_n',
            '=',
            'm',
            '\\frac{v_1^2}{\\rho}',
            '=',
            'N',
            '+',
            'm',
            'g'
        ).scale(0.8).to_corner(UP+LEFT, buff=0.75)
        contact_def = Tex('Contact is lost if $N=0$', color=YELLOW).scale(0.7).next_to(accel, DOWN, aligned_edge=LEFT)

        self.play(Write(accel))
        self.wait()
        self.play(Write(contact_def))
        self.wait()
        self.play(
            Transform(accel[7:], accel[7:].copy().next_to(accel[4], RIGHT, buff=0.18).shift(0.05*DOWN)),
            FadeOut(accel[5:7]),
            FadeOut(accel[:2])
        )
        self.wait()
        self.play(
            Transform(accel[8], accel[8].copy().next_to(accel[4], RIGHT, buff=0.18)),
            FadeOut(accel[2]),
            FadeOut(accel[7])
        )
        self.wait()
        accel_remain = Group(accel[3], accel[4], accel[8])
        self.play(
            Transform(accel_remain, accel_remain.copy().to_corner(UP+LEFT, buff=0.75).shift(0.5*RIGHT)),
            FadeOut(contact_def)
        )
        hlbox1 = SurroundingRectangle(accel_remain, buff=0.15)
        self.play(ShowCreation(hlbox1))
        self.wait()

        # Energy equation
        energy_0 = MathTex(
            '\\Delta W',
            '=',
            '\\Delta E_g',
            '+',
            '\\Delta E_k'
        ).scale(0.7).next_to(accel_remain, RIGHT, buff=1)
        energy_1 = MathTex(
            '0',
            '=',
            'mg(2\\rho-h)',
            '+',
            '\\frac{1}{2}m(v_1^2-v_0^2)',
            '\\Rightarrow',
            'v_1=\\sqrt{v_0^2+2g(h-2\\rho)}'
        ).scale(0.7)
        energy_1.shift(energy_0[1].get_center()-energy_1[1].get_center())
        hlbox2 = SurroundingRectangle(energy_1[-1], buff=0.1)
        self.play(Write(energy_0))
        self.wait()
        self.play(*[ReplacementTransform(energy_0[i], energy_1[i]) for i in range(len(energy_0))])
        self.wait()
        self.play(Write(energy_1[-2:]))
        self.play(ShowCreation(hlbox2))
        self.wait()

        ans = MathTex('v_0=\\sqrt{g(5\\rho-2h)}').scale(0.9).shift(1.25*UP)
        ansbox=SurroundingRectangle(ans, buff=0.2)
        self.play(Write(ans))
        self.play(ShowCreation(ansbox))
        self.wait()
