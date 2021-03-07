from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

DSCALE = 0.75/50

class T7P3(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Diagram objects
        # Link ADB
        adb = Line(
            start=DSCALE*300*((3/5)*DOWN + (4/5)*RIGHT),
            end=DSCALE*250*((3/5)*UP + (4/5)*LEFT),
            color=BLUE,
            stroke_width=15
        )
        point_a_adb = Dot(
            point=adb.get_start(),
            radius=0.15,
            color=BLUE_E
        )
        point_d_adb = Dot(
            point=ORIGIN,
            radius=0.15,
            color=BLUE_E
        )
        point_b_adb = Dot(
            point=adb.get_end(),
            radius=0.15,
            color=BLUE_E
        )
        link_adb = Group(adb, point_a_adb, point_d_adb, point_b_adb)

        # Link CDE
        cde = Line(
            start=DSCALE*400*np.array([-np.cos(PI/6), -np.sin(PI/6), 0]),
            end=DSCALE*300*np.array([np.cos(PI/6), np.sin(PI/6), 0]),
            color=RED,
            stroke_width=15
        )
        point_c_cde = Dot(
            point=cde.get_start(),
            radius=0.15,
            color=RED_E
        )
        point_d_cde = Dot(
            point=ORIGIN,
            radius=0.15,
            color=RED_E
        )
        point_e_cde = Dot(
            point=cde.get_end(),
            radius=0.15,
            color=RED_E
        )
        link_cde = Group(cde, point_c_cde, point_d_cde, point_e_cde)

        diagram = Group(link_adb, link_cde).move_to(ORIGIN)
        self.add(diagram)
        self.wait()

