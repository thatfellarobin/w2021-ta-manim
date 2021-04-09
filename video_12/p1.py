from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

BALL_RADIUS = 0.75
BALL_HEIGHT = 2
BALL_OFFSET = 0.5

class T12P1(Scene):
    def number_equation(self, eq, n, color=YELLOW_B):
        num = MathTex('\\textbf{' + str(n) + '}', color=color).scale(0.5)
        circle = Circle(
            color=color,
            radius=0.225,
            arc_center=num.get_center()
        )
        line = Line(
            start=circle.get_edge_center(LEFT),
            end=circle.get_edge_center(LEFT)+0.6*LEFT,
            color=color
        )
        group = Group(num, circle, line)
        group.next_to(eq, RIGHT, buff=0.25)
        self.play(FadeIn(group))
        return group

    def recursive_set_opacity(self, mobj, opacity=0):
        for item in mobj:
            if len(item) > 1:
                self.recursive_set_opacity(mobj=item, opacity=opacity)
            else:
                item.set_opacity(opacity)
        return mobj

    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Diagram objects

        #endregion