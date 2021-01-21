from manim import *
import numpy as np


class Graph_Problem1(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            # axes_color=BLACK,
            graph_origin=1 * UP + 4.5 * LEFT,
            x_min=0,
            x_max=3,
            x_labeled_nums=np.arange(0, 4, 1),
            x_axis_label="$t$",
            x_axis_width=7,
            y_min=-15,
            y_max=10,
            y_labeled_nums=np.arange(-15, 15, 5),
            y_axis_label=None,
            y_axis_height=5.5,
            y_axis_config={"tick_frequency": 2.5},
            **kwargs
        )

    def construct(self):
        self.setup_axes(animate=True)

        vel_graph = self.get_graph(lambda x: 6*x - 3*x**2)
        vel_graph_label = self.get_graph_label(vel_graph, label="v(t)=bt+ct^2")

        acc_graph = self.get_graph(lambda x: 6 - 6*x, color=RED)
        acc_graph_label = self.get_graph_label(acc_graph, label="a(t)=\\frac{d}{dt}v(t)").shift(0.2 * DOWN)

        pos_graph = self.get_graph(lambda x: 3*x**2 -x**3, color=GREEN)
        pos_graph_label = self.get_graph_label(pos_graph, label="s(t)=\\int v(t)\\,dt")

        # Create plots
        self.play(ShowCreation(vel_graph))
        self.play(Write(vel_graph_label))
        self.wait()
        self.play(ShowCreation(acc_graph))
        self.play(Write(acc_graph_label))
        self.wait()
        self.play(ShowCreation(pos_graph))
        self.play(Write(pos_graph_label))
        self.wait()

        # Demonstrate effect of initial conditions
        self.play(
            pos_graph.animate.shift(UP),
            pos_graph_label.animate.shift(UP),
            run_time=1
        )
        self.wait(0.3)
        self.play(
            pos_graph.animate.shift(3 * DOWN),
            pos_graph_label.animate.shift(3 * DOWN),
            run_time=1
        )
        self.wait(0.3)
        self.play(
            pos_graph.animate.shift(2 * UP),
            pos_graph_label.animate.shift(2 * UP),
            run_time=1
        )
        self.wait()
        circle_initcond = Circle(color=YELLOW, radius=0.15).move_to(self.coords_to_point(0,0))
        initcond_label = MathTex(r"s(0)=0", color=YELLOW).next_to(self.coords_to_point(0,0), LEFT).scale(0.7)
        self.play(
            ShowCreation(circle_initcond),
            Write(initcond_label)
        )
        self.wait()
        self.play(
            FadeOut(circle_initcond),
            FadeOut(initcond_label)
        )

        # Indicate turnaround point
        turnaround_circle = Circle(color=YELLOW, radius=0.15).move_to(self.coords_to_point(2, 0))
        self.play(ShowCreation(turnaround_circle))
        self.wait()
        self.play(turnaround_circle.animate.shift(self.coords_to_point(2, 4) - self.coords_to_point(2, 0)))
        self.wait()

        # Expression to solve for the turnaround time
        time_t2 = MathTex("t_2", color=PURPLE).move_to(self.coords_to_point(2, 6.5))
        turnaround_expression = MathTex("v(t_2)=0\\Rightarrow t_2=2\\,\\mathrm{s}").move_to(self.coords_to_point(2, 9))
        self.play(
            Write(time_t2),
            Write(turnaround_expression)
        )
        self.wait()
        self.play(
            FadeOut(time_t2),
            FadeOut(turnaround_expression)
        )

        # Show the calculation of total distance on the graph
        turnaround_line = self.get_vertical_line_to_graph(2, pos_graph, color=YELLOW)
        self.play(
            FadeOut(vel_graph),
            FadeOut(vel_graph_label),
            FadeOut(acc_graph),
            FadeOut(acc_graph_label),
            ReplacementTransform(turnaround_circle, turnaround_line)
        )
        self.wait()
        totaldist = MathTex(
            "d_{tot}=", "|s(2)-s(0)|", "+", "|s(3)-s(2)|"
            ).shift(0.75 * DOWN + 0.75 * RIGHT)
        self.play(Write(totaldist))
        dist1_box = SurroundingRectangle(totaldist[1], buff=.1)
        dist2_box = SurroundingRectangle(totaldist[3], buff=.1)
        self.wait()
        self.play(ShowCreation(dist1_box))
        self.wait()
        self.play(ReplacementTransform(dist1_box, dist2_box))
        self.wait()
        self.play(FadeOut(dist2_box))
        distresult_intermediate = MathTex(
            "d_{tot}=", "|4-0|", "+", "|0-4|"
            ).shift(0.75 * DOWN).align_to(totaldist, direction=LEFT)
        distresult_final = MathTex(
            "d_{tot}=", "8\\,\\mathrm{m}"
            ).shift(0.75 * DOWN).align_to(totaldist, direction=LEFT)
        self.play(*[ReplacementTransform(totaldist[i], distresult_intermediate[i]) for i in range(4)])
        self.wait()
        self.play(ReplacementTransform(distresult_intermediate[1:4], distresult_final[1]))

        self.wait()

class Q1_Equations(Scene):
    def construct(self):
        vel_func = MathTex("v(t)", "=", "6t-3t^2").shift(2 * UP)
        acc_func = MathTex("a(t)", "=", "\\frac{d}{dt}v(t)", "=", "6-6t")
        pos_func = MathTex("s(t)", "=", "\\int v(t)\\,dt", "=", "3t^2-t^3", "+", "s_0").shift(2 * DOWN)

        acc_sub = MathTex("a(3)", "=", "6-6(3)").align_to(acc_func, LEFT)
        acc_soln = MathTex("-12\\,\\mathrm{m/s^2}").align_to(acc_sub[2], LEFT)

        pos_sub = MathTex("s(0)", "=", "3(0)^2-(0)^3", "+", "s_0", "=0").shift(2 * DOWN).align_to(pos_func, LEFT)

        # Show expressions
        self.play(
            Write(vel_func),
            Write(acc_func),
            Write(pos_func)
        )
        self.wait()

        # Solve through acceleration
        self.play(
            FadeOut(acc_func[2:4])
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(acc_func[0], acc_sub[0]),
            ReplacementTransform(acc_func[1], acc_sub[1]),
            ReplacementTransform(acc_func[4], acc_sub[2])
        )
        self.wait()
        self.play(
            ReplacementTransform(acc_sub[2], acc_soln)
        )
        self.wait()

        # Solve through position for initial condition
        self.play(
            FadeOut(pos_func[2:4])
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(pos_func[0], pos_sub[0]),
            ReplacementTransform(pos_func[1], pos_sub[1]),
            ReplacementTransform(pos_func[4], pos_sub[2]),
            ReplacementTransform(pos_func[5:7], pos_sub[3:5])
        )
        self.wait(0.5)
        self.play(
            Write(pos_sub[5])
        )
        self.wait()
        self.play(
            FadeOut(pos_sub[:-2])
        )
        self.wait()

        self.clear()
        self.wait()

        avg_speed = MathTex("v_{avgspeed}=\\frac{d_{tot}}{t_{tot}}", "=2.67\\,\\mathrm{m/s}}")
        self.play(Write(avg_speed))
        self.wait()