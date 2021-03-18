from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

DSCALE = 1/3
IMGSCALE = 4/500


class T9P1(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        reserved_area = Rectangle(
            width=IMGSCALE*466,
            height=IMGSCALE*572,
            color=YELLOW
        ).to_corner(UP+RIGHT, buff=0.5)
        self.add(reserved_area)

        #region Free body diagram of weight
        block = Rectangle(
            height=1,
            width=0.75,
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1
        )
        fbd_tension_arrow = Arrow(
            start=block.get_edge_center(UP),
            end=block.get_edge_center(UP)+UP,
            color=RED,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_tension_label = MathTex('2T', color=RED).scale(0.6).next_to(fbd_tension_arrow, UP, buff=0.1)
        mg_a_arrow = Arrow(
            start=block.get_edge_center(DOWN),
            end=block.get_edge_center(DOWN)+DOWN,
            color=PURPLE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        mg_a_label = MathTex('m_ag', color=PURPLE).scale(0.6).next_to(mg_a_arrow, DOWN, buff=0)
        accel_a_arrow = Arrow(
            start=block.get_edge_center(RIGHT)+0.25*RIGHT,
            end=block.get_edge_center(RIGHT)+0.25*RIGHT+UP,
            color=BLUE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        accel_a_label = MathTex('\\frac{a}{2}', color=BLUE).scale(0.6).next_to(accel_a_arrow, UP, buff=0.1)

        fbd = Group(
            block,
            fbd_tension_arrow,
            fbd_tension_label,
            mg_a_arrow,
            mg_a_label,
            accel_a_arrow,
            accel_a_label
        ).move_to(ORIGIN)

        self.add(block)
        self.wait()
        self.play(
            Write(mg_a_arrow),
            Write(mg_a_label)
        )
        self.wait(0.5)
        self.play(
            Write(fbd_tension_arrow),
            Write(fbd_tension_label)
        )
        self.wait(0.5)
        self.play(
            Write(accel_a_arrow),
            Write(accel_a_label)
        )
        self.wait()

        self.play(
            Transform(fbd, fbd.copy().scale(0.75).next_to(reserved_area, LEFT, aligned_edge=UP))
        )
        self.wait()

        fbd_eq = MathTex(
            '\\Sigma F_y = m\\frac{a}{2} = 2T - m_ag'
        ).scale(0.6).to_corner(UP+LEFT, buff=0.75)
        fbd_eq_sub = MathTex(
            'T=43.24\\,\\mathrm{kN}'
        ).scale(0.6).next_to(fbd_eq, DOWN, aligned_edge=LEFT)

        self.play(Write(fbd_eq))
        self.wait()
        self.play(Write(fbd_eq_sub))
        self.wait()
        self.play(
            FadeOut(fbd_eq),
            Transform(fbd_eq_sub, fbd_eq_sub.copy().to_corner(UP+LEFT, buff=0.75))
        )
        self.wait()
        #endregion
