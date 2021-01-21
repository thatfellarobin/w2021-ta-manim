from manim import *
import numpy as np


class P1(Scene, MovingCameraScene):
    # CONFIG = { # Originally thought I'd use GraphSchene
    #     'x_min': 0,
    #     'x_max': 20,
    #     'x_labeled_nums': np.arange(0, 25, 5),
    #     'x_axis_label': "$t$",
    #     # 'x_axis_width': 7,
    #     'x_axis_config': {"tick_frequency": 2.5},
    #     'y_min': 0,
    #     'y_max': 8,
    #     'y_labeled_nums': np.arange(0, 10, 2),
    #     'y_axis_label': None,
    #     # 'y_axis_height': 5.5
    #     # 'y_axis_config': {"tick_frequency": 2.5}
    # }

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        a = MathTex("a(t)", "=", "\\frac{dv(t)}{dt}", "=", "0.015t^2", color=RED)
        v = MathTex("v(t)", "=", "\\int a(t)\\,dt", "=", "0.005t^3 + v_0", color=BLUE)
        s = MathTex("s(t)", "=", "\\int v(t)\\,dt", "=", "0.00125t^4 + v_0t + s_0", color=GREEN)

        # Initial conditions
        initcond_prose = Tex("The automobile is \\textbf{originally} at \\textbf{rest} at $s=0$", color=YELLOW)
        initcond = Tex("$s(0)=0$, $v(0)=0$", color=YELLOW)
        self.play(Write(initcond_prose))
        self.wait()
        self.play(Write(initcond_prose))
        self.wait()
        # There should be some animations here showing `s` and `v` getting modified.

        # # Indicate turnaround point
        # turnaround_circle = Circle(color=YELLOW, radius=0.15).move_to(self.coords_to_point(2, 0))
        # self.play(ShowCreation(turnaround_circle))
        # self.wait()
        # self.play(turnaround_circle.animate.shift(self.coords_to_point(2, 4) - self.coords_to_point(2, 0)))
        # self.wait()

        # # Expression to solve for the turnaround time
        # time_t2 = MathTex("t_2", color=PURPLE).move_to(self.coords_to_point(2, 6.5))
        # turnaround_expression = MathTex("v(t_2)=0\\Rightarrow t_2=2\\,\\mathrm{s}").move_to(self.coords_to_point(2, 9))
        # self.play(
        #     Write(time_t2),
        #     Write(turnaround_expression)
        # )
        # self.wait()
        # self.play(
        #     FadeOut(time_t2),
        #     FadeOut(turnaround_expression)
        # )

        # # Show the calculation of total distance on the graph
        # turnaround_line = self.get_vertical_line_to_graph(2, pos_graph, color=YELLOW)
        # self.play(
        #     FadeOut(vel_graph),
        #     FadeOut(vel_graph_label),
        #     FadeOut(acc_graph),
        #     FadeOut(acc_graph_label),
        #     ReplacementTransform(turnaround_circle, turnaround_line)
        # )
        # self.wait()
        # totaldist = MathTex(
        #     "d_{tot}=", "|s(2)-s(0)|", "+", "|s(3)-s(2)|"
        #     ).shift(0.75 * DOWN + 0.75 * RIGHT)
        # self.play(Write(totaldist))
        # dist1_box = SurroundingRectangle(totaldist[1], buff=.1)
        # dist2_box = SurroundingRectangle(totaldist[3], buff=.1)
        # self.wait()
        # self.play(ShowCreation(dist1_box))
        # self.wait()
        # self.play(ReplacementTransform(dist1_box, dist2_box))
        # self.wait()
        # self.play(FadeOut(dist2_box))
        # distresult_intermediate = MathTex(
        #     "d_{tot}=", "|4-0|", "+", "|0-4|"
        #     ).shift(0.75 * DOWN).align_to(totaldist, direction=LEFT)
        # distresult_final = MathTex(
        #     "d_{tot}=", "8\\,\\mathrm{m}"
        #     ).shift(0.75 * DOWN).align_to(totaldist, direction=LEFT)
        # self.play(*[ReplacementTransform(totaldist[i], distresult_intermediate[i]) for i in range(4)])
        # self.wait()
        # self.play(ReplacementTransform(distresult_intermediate[1:4], distresult_final[1]))

        # self.wait()

# class Q1_Equations(Scene):
#     def construct(self):
