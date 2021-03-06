from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

class T6P1(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        cam_disk = Circle(
            radius=1.5,
            stroke_color=GOLD,
            fill_color=GOLD_DARK,
            fill_opacity=1
        )
        cam_hinge = Dot(
            point=-1.1*np.array([np.cos(PI/6), np.sin(PI/6), 0]),
            radius=0.25,
            color=GOLD
        )
        cam = Group(cam_disk, cam_hinge)

        hinge_ext_circ = Dot(
            point=cam_hinge.get_center(),
            radius=0.175,
            color=BLUE_E
        )
        hinge_ext_base = Rectangle(
            width=0.175*2,
            height=0.3,
            fill_color=BLUE_E,
            fill_opacity=1,
            stroke_opacity=0
        )
        hinge_ext_base.shift(hinge_ext_circ.get_center() - hinge_ext_base.get_edge_center(UP))
        hinge_ext = Group(hinge_ext_base, hinge_ext_circ)
        pin = Dot(
            point=hinge_ext_circ.get_center(),
            color=GREY
        )

        def generate_camfollower_points(face_width):
            hfw = face_width/2
            follower_points_half1 = [
                hfw*UP,
                hfw*UP + 0.1*RIGHT,
                hfw*UP + 0.1*RIGHT + 0.2*RIGHT + 0.3*DOWN
            ]
            follower_points_half2 = follower_points_half1.copy()
            for i in range(len(follower_points_half2)):
                follower_points_half2[i] = np.multiply(follower_points_half2[i], [1, -1, 1]) # invert y
            follower_points_half2.reverse()
            follower_points = follower_points_half1.copy() + follower_points_half2
            return follower_points
        follower_points = generate_camfollower_points(2.4)
        follower_plate = Polygon(
            *follower_points,
            color=GREEN_E,
            fill_color=GREEN_DARK,
            fill_opacity=1.0
        ).next_to(pin, RIGHT, buff=0)
        follower_plate.shift(np.array([cam_disk.get_edge_center(RIGHT)[0] - follower_plate.get_edge_center(LEFT)[0], 0, 0]))
        follower_rod = Rectangle(
            width=3.5,
            height=0.3,
            color=GREEN_E,
            fill_color=GREEN_DARK,
            fill_opacity=1.0
        ).next_to(follower_plate, RIGHT, buff=0)
        follower = Group(follower_rod, follower_plate)

        diagram = Group(
            cam,
            follower,
            hinge_ext,
            pin
        )

        self.add(diagram)
        self.wait()