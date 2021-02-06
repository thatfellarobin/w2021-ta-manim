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
            dy_dx = (-2 * DIM_H * x) / DIM_B**2
            theta = np.arctan(dy_dx)
            return (np.array([np.cos(theta), np.sin(theta), 0]), theta)

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
        ).scale(0.7).to_edge(UP, buff=1.75)
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
        ans1 = Group(v_B, ansbox1)
        self.play(
            FadeOut(energycons_0),
            FadeOut(energycons_1),
            Transform(ans1, ans1.copy().shift(1.5*LEFT+UP))
        )

        # Free body diagram
        car_fbd = car.copy().move_to(1*LEFT+0.5*UP)
        theta_ref = Line(
            start=car_fbd.get_center(),
            end=car_fbd.get_center()+RIGHT,
            color=GREY
        )
        theta_arc = Arc(
            radius=0.7,
            arc_center=car_fbd.get_center(),
            start_angle=0,
            angle=path_function_deriv_dir(DIM_B)[1],
            color=YELLOW
        ).add_tip(tip_length=0.2)
        theta_label = MathTex('\\theta_B', color=YELLOW).scale(0.7).next_to(theta_arc, RIGHT)
        t_line = Line(
            start=car_fbd.get_center(),
            end=car_fbd.get_center() + 1.0*path_function_deriv_dir(DIM_B)[0],
            color=YELLOW_A
        )
        t_line_label = MathTex('+t', color=YELLOW_A).scale(0.7).next_to(t_line.get_end(), RIGHT, buff=0.1)
        n_line = Line(
            start=car_fbd.get_center(),
            end=car_fbd.get_center() + 1.0*t_line.copy().rotate(PI/2).get_unit_vector(),
            color=YELLOW_A
        )
        n_line_label = MathTex('-n', color=YELLOW_A).scale(0.7).next_to(n_line.get_end(), RIGHT, buff=0.1)
        gravity_arrow = Arrow(
            start=car_fbd.get_center(),
            end=car_fbd.get_center()+DOWN,
            color=BLUE,
            buff=0.0,
            stroke_width=6,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        gravity_arrow_label = MathTex('mg', color=BLUE).scale(0.7).next_to(gravity_arrow.get_end(), DOWN, buff=0.1)
        N_arrow = Arrow(
            start=car_fbd.get_center()-n_line.get_unit_vector(),
            end=car_fbd.get_center()-0.12*n_line.get_unit_vector(),
            color=PURPLE,
            buff=0.0,
            stroke_width=6,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        N_arrow_label = MathTex('N_B', color=PURPLE).scale(0.7).next_to(N_arrow.get_start(), LEFT, buff=0.1)

        fbd = Group(
            car_fbd,
            theta_ref,
            theta_arc,
            theta_label,
            t_line,
            t_line_label,
            n_line,
            n_line_label,
            gravity_arrow,
            gravity_arrow_label,
            N_arrow,
            N_arrow_label
        )

        self.play(
            ShowCreation(theta_ref),
            ShowCreation(theta_arc),
            Write(theta_label),
            ShowCreation(t_line),
            Write(t_line_label),
            ShowCreation(n_line),
            Write(n_line_label),
            FadeIn(car_fbd)
        )
        self.wait()
        self.play(
            Write(gravity_arrow),
            Write(gravity_arrow_label),
            Write(N_arrow),
            Write(N_arrow_label)
        )
        self.wait()

        # Normal accel and stuff
        normal_accel = MathTex(
            'a_{nB}',
            '=',
            'mg\\cos(\\theta_B) - N_B',
            '=',
            'v_B^2/\\rho_B'
        ).scale(0.75).next_to(fbd, RIGHT, buff=0.8, aligned_edge=UP).shift(1.5*UP)
        normal_accel[3:].next_to(normal_accel[1:], DOWN, aligned_edge=LEFT)
        self.play(Write(normal_accel[:3]))
        self.wait()
        self.play(Write(normal_accel[3:]))
        self.wait()
        question = Tex('we need $\\theta_B$ and $\\rho_B$', color=YELLOW).scale(0.6).next_to(normal_accel, DOWN, aligned_edge=LEFT)
        self.play(Write(question))
        self.wait()
        theta_expr = MathTex('\\theta(x)=\\mathrm{tan}^{-1}(y^\\prime(x))').scale(0.75).next_to(question, DOWN, aligned_edge=LEFT)
        rho_expr = MathTex('\\rho(x)', '=', '\\frac{\\sqrt{\\left(1+y^{\\prime}(x)^2\\right)^3}}{y^{\\prime\\prime}(x)}').scale(0.75).next_to(theta_expr, DOWN, aligned_edge=LEFT)
        self.play(Write(theta_expr))
        self.play(Write(rho_expr))
        self.wait()
        y_prime_expr = MathTex('y^\\prime(','x',')=-2h','x','/','b^2', color=PURPLE).scale(0.7).next_to(y_expr, RIGHT, buff=0.75)
        y_prime2_expr = MathTex('y^{\\prime\\prime}(','x',')=-2h/b^2', color=PURPLE).scale(0.7).next_to(y_prime_expr, RIGHT, buff=0.75)
        self.play(Write(y_prime_expr))
        self.wait()
        self.play(Write(y_prime2_expr))
        self.wait()
        self.play(FadeOut(question))
        self.wait()
        y_prime_expr_sub = MathTex('y^\\prime(','b',')=-2h','/','b', color=PURPLE).scale(0.7)
        y_prime_expr_sub.shift(y_prime_expr[0].get_center() - y_prime_expr_sub[0].get_center())
        y_prime2_expr_sub = MathTex('y^{\\prime\\prime}(','b',')=-2h/b^2', color=PURPLE).scale(0.7).next_to(y_prime_expr, RIGHT, buff=0.5)
        y_prime_expr_sub.shift(y_prime2_expr[0].get_center() - y_prime2_expr_sub[0].get_center())
        self.play(
            ReplacementTransform(y_prime_expr[0], y_prime_expr_sub[0]),
            ReplacementTransform(y_prime_expr[1], y_prime_expr_sub[1]),
            ReplacementTransform(y_prime_expr[2], y_prime_expr_sub[2]),
            FadeOut(y_prime_expr[3]),
            ReplacementTransform(y_prime_expr[4], y_prime_expr_sub[3]),
            ReplacementTransform(y_prime_expr[5], y_prime_expr_sub[4]),
            *[ReplacementTransform(y_prime2_expr[i], y_prime2_expr_sub[i]) for i in range(len(y_prime2_expr))]
        )
        self.wait()

        normal_ans = MathTex('N_B=151.7\\,\\mathrm{N}').scale(0.8).next_to(rho_expr, DOWN, buff=1.5)
        ansbox2 = SurroundingRectangle(normal_ans, buff=0.2)
        ans2 = Group(normal_ans, ansbox2).next_to(rho_expr, DOWN, aligned_edge=LEFT)
        self.play(Write(normal_ans))
        self.play(ShowCreation(ansbox2))
        self.wait()

