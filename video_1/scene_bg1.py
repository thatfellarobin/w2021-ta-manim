from manim import *
import numpy as np


class Graph_Position(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            # axes_color=BLACK,
            x_min=0,
            x_max=10,
            x_axis_label="$t$",
            y_min=0,
            y_max=50,
            y_axis_height=5.5,
            y_axis_config={
                "tick_frequency": 10},
            y_axis_label="$s(t)$",
            **kwargs
        )

    def construct(self):
        self.setup_axes()

        pos_graph = self.get_graph(lambda x: 0.5 * x ** 2)

        # Assemble Scene
        self.add(
            pos_graph
            )

        # Render
        self.play(ShowCreation(pos_graph))
        self.wait(1)


class Graph_Velocity(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            # axes_color=BLACK,
            x_min=0,
            x_max=10,
            x_axis_label="$t$",
            y_min=0,
            y_max=10,
            y_axis_height=5.5,
            y_axis_config={
                "tick_frequency": 1},
            y_axis_label="$v(t)$",
            **kwargs
        )

    def construct(self):
        self.setup_axes()

        vel_graph = self.get_graph(lambda x: x)

        # Assemble Scene
        self.add(
            vel_graph
            )

        # Render
        self.play(ShowCreation(vel_graph))
        self.wait(1)


class Graph_Acceleration(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            # axes_color=BLACK,
            x_min=0,
            x_max=10,
            x_axis_label="$t$",
            y_min=0,
            y_max=2,
            y_axis_label="$a(t)$",
            y_axis_height=5.5,
            y_axis_config={
                "tick_frequency": 1},
            **kwargs
        )

    def construct(self):
        self.setup_axes()

        acc_graph = self.get_graph(lambda x: 1)

        # Assemble Scene
        self.add(
            acc_graph
            )

        # Render
        self.play(ShowCreation(acc_graph))
        self.wait(1)
