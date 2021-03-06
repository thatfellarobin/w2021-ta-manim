from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

LINK_WIDTH = 0.25
DSCALE = 0.75/50

class T7P2(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Diagram objects

        # Link EB
        eb = Line(
            start=ORIGIN,
            end=50*DSCALE*UP,
            color=BLUE,
            stroke_width=15
        )
        point_e_eb = Dot(
            point=eb.get_start(),
            radius=0.15,
            color=BLUE_E
        )
        point_b_eb = Dot(
            point=eb.get_end(),
            radius=0.15,
            color=BLUE_E
        )
        link_eb = Group(eb, point_e_eb, point_b_eb)

        # Link ABC
        ab = Line(
            start=50*DSCALE*np.array([np.cos(3*PI/4), np.sin(3*PI/4), 0]),
            end=ORIGIN,
            color=RED,
            stroke_width=15
        )
        bc = Line(
            start=ab.get_end(),
            end=250*DSCALE*np.array([np.cos(PI/3), np.sin(PI/3), 0]),
            color=RED,
            stroke_width=15
        )
        point_a_abc = Dot(
            point=ab.get_start(),
            radius=0.15,
            color=RED_E
        )
        point_b_abc = Dot(
            point=ab.get_end(),
            radius=0.15,
            color=RED_E
        )
        point_c_abc = Dot(
            point=bc.get_end(),
            radius=0.15,
            color=RED_E
        )
        link_abc = Group(ab, bc, point_a_abc, point_b_abc, point_c_abc)
        link_abc.shift(point_b_eb.get_center()-point_b_abc.get_center())

        # Link AD
        ad = Line(
            start=ORIGIN,
            end=250*DSCALE*np.array([np.cos(3*PI/4), np.sin(3*PI/4), 0]),
            color=BLUE,
            stroke_width=15
        )
        point_a_ad = Dot(
            point=ad.get_start(),
            radius=0.15,
            color=BLUE_E
        )
        point_d_ad = Dot(
            point=ad.get_end(),
            radius=0.15,
            color=BLUE_E
        )
        link_ad = Group(ad, point_a_ad, point_d_ad)
        link_ad.shift(point_a_abc.get_center()-point_a_ad.get_center())
        #endregion

        diagram = Group(link_ad, link_abc, link_eb).move_to(ORIGIN)
        self.add(diagram)
        self.wait()

        # Separate the elements
        self.play(
            Transform(link_eb, link_eb.copy().scale(0.6).to_corner(UP+RIGHT, buff=0.75)),
            Transform(link_abc, link_abc.copy().scale(0.6).to_edge(RIGHT, buff=0.75)),
            Transform(link_ad, link_ad.copy().scale(0.6).to_corner(DOWN+RIGHT, buff=0.75))
        )
        self.wait()