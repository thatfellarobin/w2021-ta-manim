from manim import *
import numpy as np

DIAGRAM_ORIGIN = 5*LEFT + 2.5*DOWN
DIAGRAM_SCALE = 0.07
DIM_H = 60
DIM_B = 60

class T4P2(Scene):
    def construct(self):
        def path_function(x):
            y = DIM_H*(1 - (x**2/DIM_B**2))
            return DIAGRAM_SCALE * np.array([x, y, 0])
        def path_function_deriv_dir(x):
            dy_dx = (-2 * DIM_H * x) / DIM_B
            theta = np.arctan(dy_dx)
            return np.array([np.cos(theta), np.sin(theta), 0])

        # Scene objects
        x_axis = Line(start=ORIGIN, end=5*RIGHT, color=GRAY)
        y_axis = Line(start=ORIGIN, end=5*UP, color=GRAY)
        path = ParametricFunction(path_function, t_min=0, t_max=DIM_B, fill_opacity=0, color=PURPLE)
        extended_path = ParametricFunction(path_function, t_min=-10, t_max=DIM_B+5, fill_opacity=0, color=PURPLE)
        car = Dot(
            point=path.get_start(),
            radius=0.15,
            color=GREEN
        )
        A_point = SmallDot(point=path.get_start(), color=YELLOW_B)
        A_label = Tex('A', color=YELLOW_B).scale(0.9).next_to(path.get_start(), LEFT+DOWN)
        B_point = SmallDot(point=path.get_end(), color=YELLOW_B)
        B_label = Tex('B', color=YELLOW_B).scale(0.9).next_to(path.get_end(), LEFT+DOWN)
        O_point = SmallDot(point=ORIGIN, color=YELLOW_B)
        O_label = Tex('O', color=YELLOW_B).scale(0.9).next_to(ORIGIN, LEFT+DOWN)

        diagram = Group(
            x_axis,
            y_axis,
            extended_path,
            path,
            car,
            A_point,
            A_label,
            B_point,
            B_label,
            O_point,
            O_label
        ).move_to(ORIGIN).shift(3.25*LEFT+0.5*DOWN)

        self.play(
            ShowCreation(x_axis),
            ShowCreation(y_axis),
            ShowCreation(extended_path)
        )
        self.play(
            FadeIn(car),
            FadeIn(A_point),
            Write(A_label),
            FadeIn(B_point),
            Write(B_label),
            FadeIn(O_point),
            Write(O_label)
        )
        self.wait()

        y_expr = MathTex('y', '=', 'h(1-x^2/b^2)', color=PURPLE).scale(0.7).to_corner(UP+LEFT)
        self.play(Write(y_expr))
        self.wait()

        self.play(MoveAlongPath(car, path), run_time=3)
        self.wait()

        # self.play(Transform(diagram, diagram.copy().scale_about_point(point=O_point.get_center(), scale_factor=0.8)))
        # self.wait()

        # Finding v_B
        energycons_0 = MathTex(
            '\\Delta W',
            '=',
            '\\Delta E_g',
            '+',
            '\\Delta E_k'
        ).scale(0.7).to_edge(UP, buff=1.5).shift(1*RIGHT)
        energycons_1 = MathTex(
            '0',
            '=',
            'mg(y_B-y_A)',
            '+',
            '\\frac{1}{2}m(v_B^2-v_A^2)'
        ).scale(0.7)
        energycons_1.shift(energycons_0[1].get_center()+0.5*DOWN-energycons_1[1].get_center())
        self.play(Write(energycons_0))
        self.wait()
        self.play(*[ReplacementTransform(energycons_0[i].copy(), energycons_1[i]) for i in range(len(energycons_0))])
        self.wait()
        v_B = MathTex('v_B', '=', '34.435\\,\\mathrm{m/s}').scale(0.7)
        v_B.shift(energycons_1[1].get_center()+0.75*DOWN-v_B[1].get_center())
        ansbox1 = SurroundingRectangle(v_B, buff=0.15)
        self.play(Write(v_B))
        self.play(ShowCreation(ansbox1))
        self.wait()

        # Free body diagram
        car_fbd = car.copy().move_to(2*RIGHT+2*DOWN)
        t_line = Line(
            start=car_fbd.get_center(),
            end=car_fbd.get_center() + 1.5*path_function_deriv_dir(DIM_B),
            color=GREY
        )
        t_line_label = MathTex('+t', color=YELLOW_A).scale(0.7).next_to(t_line.get_end(), RIGHT, buff=0.1)
        n_line = Line(
            start=car_fbd.get_center(),
            end=car_fbd.get_center() + 1.5*t_line.copy().rotate(PI/2).get_unit_vector(),
            color=GREY
        )
        n_line_label = MathTex('-n', color=YELLOW_A).scale(0.7).next_to(n_line.get_end(), RIGHT, buff=0.1)
        self.play(
            ShowCreation(t_line),
            Write(t_line_label),
            ShowCreation(n_line),
            Write(n_line_label),
            FadeIn(car_fbd)
        )
        self.wait()