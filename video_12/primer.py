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

class VibPrimer(Scene):
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

        # Step one: use Newton's second law to get the equation of motion
        step1_tex = Tex(
            '\\textbf{Step 1:}',
            ' Use Newton\'s second law to get the equation of motion',
            color=YELLOW
        ).scale(0.6).to_corner(UP+LEFT, buff=0.5)
        self.play(Write(step1_tex))
        self.wait()
        newton_law = MathTex(
            '\\Sigma F = m\\ddot{x}',
            '\\Sigma M = I\\ddot{\\theta}'
        ).scale(0.5).next_to(step1_tex, DOWN, aligned_edge=LEFT)
        newton_law[1].next_to(newton_law[0], RIGHT, buff=1)
        self.play(Write(newton_law[0]))
        self.wait()
        self.play(Write(newton_law[1]))
        self.wait()

        # Step two: Rearrange it so that all the terms are on one side and the acceleration term has a coefficient of 1
        step2_tex = Tex(
            '\\textbf{Step 2:}',
            ' Rearrange terms to one side and divide by acceleration coefficient',
            color=YELLOW
        ).scale(0.6).next_to(newton_law, DOWN, aligned_edge=LEFT)
        self.play(Write(step2_tex))
        self.wait()
        eq_motion = MathTex(
            '\\ddot{x} + 2\\zeta \\omega_n\\dot{x} + \\omega_n^2 x = 0',
            '\\ddot{\\theta} + 2\\zeta \\omega_n\\dot{\\theta} + \\omega_n^2 \\theta = 0'
        ).scale(0.5).next_to(step2_tex, DOWN, aligned_edge=LEFT)
        eq_motion[1].next_to(eq_motion[0], RIGHT, buff=1)
        self.play(Write(eq_motion[0]))
        self.wait()
        self.play(Write(eq_motion[1]))
        self.wait()
        # TODO: explain the different terms?

        # Step three: equate coefficients to find natural frequency and damping ratio

        # Step four: