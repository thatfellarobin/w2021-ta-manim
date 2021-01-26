from manim import *
import numpy as np


GRAPH_SCALE=1.5

class P2(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            graph_origin=3*DOWN + 6*LEFT,
            x_min=0,
            x_max=250,
            x_labeled_nums=np.arange(0, 300, 100),
            x_axis_label="$x$",
            x_axis_width=2.5*GRAPH_SCALE,
            x_axis_config={"tick_frequency": 100},
            y_min=0,
            y_max=400,
            y_labeled_nums=np.arange(0, 450, 100),
            y_axis_label="$y$",
            y_axis_height=4*GRAPH_SCALE,
            y_axis_config={"tick_frequency": 100},
            **kwargs
        )

    def construct(self):
        self.setup_axes()
        self.wait()

        k = 20e3
        fullpath = self.get_graph(lambda x: k/x, x_min=50, x_max=250, color=BLUE)
        path = self.get_graph(lambda x: k/x, x_min=50, x_max=200, color=WHITE).set_opacity(0)
        bead = Dot(self.coords_to_point(50, k/50), color=YELLOW).set_opacity(0)

        marker_line = self.get_vertical_line_to_graph(200, fullpath, color=YELLOW_B)
        tangent_line = self.get_graph(lambda x: 200 - 0.5*x, x_min=150, x_max=300, color=RED)
        a_cent_arrow = Line(start=self.coords_to_point(200, 100), end=self.coords_to_point(250, 200), color=PURPLE).add_tip(tip_length=0.2)
        horiz_line = Line(start=self.coords_to_point(200, 100), end=self.coords_to_point(200, 100)+1.7*RIGHT, color=GRAY)
        theta_arc = Arc(start_angle=0, angle=-26.6*(PI/180), radius=1.3, buff=0, color=YELLOW).move_arc_center_to(self.coords_to_point(200, 100)).add_tip(tip_length=0.2)

        # Text
        y = MathTex('y(x)', '=', '\\frac{k}{x}', color=BLUE).scale(0.7).shift(2*RIGHT + 3*UP)
        y_prime = MathTex('y^{\\prime}(x)', '=', '\\frac{d}{dx}y(x)', '=', '-\\frac{k}{x^2}', color=RED).scale(0.7).next_to(y, DOWN, aligned_edge=LEFT)
        theta = MathTex('\\theta_1', '=', '\\mathrm{tan^{-1}}(y^{\\prime}(x_1))', '=', '-26.6^{\\circ}', color=YELLOW).scale(0.7).next_to(theta_arc, RIGHT)
        a_cent = MathTex('a_{1c}=', '\\frac{v^2}{\\rho_1}', color=PURPLE).scale(0.8).next_to(a_cent_arrow, direction=a_cent_arrow.get_unit_vector(), buff=0)
        rho = MathTex('\\rho(x)', '=', '\\frac{\\sqrt{\\left(1+y^{\\prime}(x)^2\\right)^3}}{y^{\\prime\\prime}(x)}').scale(0.7).next_to(y_prime, DOWN, aligned_edge=LEFT)
        y_double_prime = MathTex('y^{\\prime\\prime}(x)', '=', '\\frac{d}{dx}y^{\\prime}(x)', '=', '\\frac{2k}{x^3}').scale(0.7).next_to(rho, DOWN, aligned_edge=LEFT)

        # Magnitude of accel
        a_solution_magnitude = MathTex(
            '|\\vec{a_1}|',
            '=',
            '\\frac{v^2}{\\rho_1}',
            '=',
            '322\\,\\mathrm{mm/s^2}').scale(0.7).next_to(y_double_prime, DOWN, aligned_edge=LEFT)
        a_solution_x = MathTex(
            'a_{1x}=|\\vec{a_1}|\\mathrm{cos}(\\theta_1+\pi/2)=288\\,\\mathrm{mm/s^2}'
        ).scale(0.65).next_to(a_solution_magnitude, DOWN, aligned_edge=LEFT)
        a_solution_y = MathTex(
            'a_{1y}=|\\vec{a_1}|\\mathrm{sin}(\\theta_1+\pi/2)=144\\,\\mathrm{mm/s^2}'
        ).scale(0.65).next_to(a_solution_x, DOWN, aligned_edge=LEFT)

        self.add(path)
        self.play(ShowCreation(fullpath))
        self.play(Write(y))
        self.wait()
        self.add_foreground_mobject(bead)
        self.wait()
        self.play(
            Transform(bead, bead.copy().set_opacity(1)),
            MoveAlongPath(bead, path, rate_func=linear, run_time=1.5)
        )
        self.wait()
        self.play(ShowCreation(marker_line))
        self.wait()
        self.play(ShowCreation(tangent_line))
        self.wait()
        self.play(Write(y_prime))
        self.wait()
        self.play(ShowCreation(horiz_line))
        self.play(ShowCreation(theta_arc))
        self.play(Write(theta[0:3]))
        self.wait()
        self.play(Write(theta[3:]))
        self.play(FadeOut(theta[2:4]))
        self.play(Transform(theta[4], theta[4].copy().next_to(theta[1], RIGHT, buff=0.15)))

        self.wait()
        self.play(ShowCreation(a_cent_arrow))
        self.play(Write(a_cent))
        self.wait()
        self.play(Write(rho))
        self.wait()
        self.play(Write(y_double_prime))
        self.wait()
        self.play(Write(a_solution_magnitude))
        a_sol_mag_box = SurroundingRectangle(a_solution_magnitude, buff=.1)
        self.play(ShowCreation(a_sol_mag_box))
        self.wait()

        self.play(Write(a_solution_x))
        self.wait()
        self.play(Write(a_solution_y))
        self.wait()
        a_group = Group(a_solution_x, a_solution_y)
        a_sol_box = SurroundingRectangle(a_group, buff=.1)
        self.play(ShowCreation(a_sol_box))
        self.wait()

