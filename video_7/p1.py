from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

class T7P1(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Diagram objects
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
        hinge_ext_floor = Line(
            start=hinge_ext_base.get_edge_center(DOWN) + 0.5*LEFT,
            end=hinge_ext_base.get_edge_center(DOWN) + 0.5*RIGHT,
            color=GREY
        )
        pin = Dot(
            point=hinge_ext_circ.get_center(),
            color=GREY
        )
        hinge_ext = Group(hinge_ext_base, hinge_ext_circ, hinge_ext_floor, pin)

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
        follower_points = generate_camfollower_points(2.7)
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
        #endregion

        diagram = Group(
            cam,
            follower,
            hinge_ext
        ).move_to(ORIGIN)

        def follower_updater(follower):
            x = cam_disk.get_edge_center(RIGHT)[0]
            follower.shift(np.array([x-follower.get_edge_center(LEFT)[0], 0, 0]))

        self.add(diagram)
        self.wait()

        omega_expl = Tex('clockwise rotation at a rate of $\\omega$:', color=YELLOW).scale(0.6).to_corner(UP+LEFT, buff=1).shift(4*RIGHT)
        theta_dot = MathTex('\\dot{\\theta} = -\\omega').scale(0.8).next_to(omega_expl, DOWN, aligned_edge=LEFT)

        self.play(Write(omega_expl, run_time=1))
        self.play(Write(theta_dot))
        self.wait()

        follower.add_updater(follower_updater)
        path_arc = Arc(
            start_angle=PI/6,
            angle=-TAU,
            radius=1.1,
            arc_center=pin.get_center()
        )
        for _ in range(2):
            self.play(MoveAlongPath(cam_disk, path_arc, rate_func=linear, run_time=3))
        follower.clear_updaters()
        self.wait()

        #region annotations
        e_line = Line(
            start=pin.get_center(),
            end=cam_disk.get_center(),
            color=WHITE,
            stroke_opacity=0.5
        )
        e_arrow = DoubleArrow(
            start=pin.get_center(),
            end=cam_disk.get_center(),
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        e_arrow.shift(0.3 * e_line.copy().rotate(PI/2).get_unit_vector())
        e_annot = MathTex('e', color=YELLOW).scale(0.6).next_to(e_arrow.get_center(), e_line.copy().rotate(PI/2).get_unit_vector(), buff=0.15)
        cam_center_dot = Dot(
            point=cam_disk.get_center(),
            color=WHITE
        )
        r_line = Line(
            start=cam_disk.get_center(),
            end=cam_disk.get_edge_center(RIGHT),
            color=WHITE,
            stroke_opacity=0.5
        )
        r_arrow = DoubleArrow(
            start=cam_disk.get_center() + 0.3*UP,
            end=cam_disk.get_edge_center(RIGHT) + 0.3*UP,
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        r_annot = MathTex('r', color=YELLOW).scale(0.6).next_to(r_arrow.get_center(), UP, buff=0.15)
        theta_arc = Arc(
            radius=0.75,
            arc_center=pin.get_center(),
            start_angle=0,
            angle=PI/6,
            color=YELLOW
        ).add_tip(tip_length=0.15)
        theta_line = Line(
            start=pin.get_center(),
            end=pin.get_center()+RIGHT,
            color=WHITE,
            stroke_opacity=0.5
        )
        theta_annot = MathTex('\\theta', color=YELLOW).scale(0.6).next_to(theta_arc, RIGHT, buff=0.15).shift(0.05*(LEFT+UP))

        x_ref_line = Line(
            start=pin.get_center()+0.5*DOWN,
            end=pin.get_center()+1*DOWN,
            color=BLUE
        )
        x_arrow = Arrow(
            start=x_ref_line.get_center(),
            end=np.array([follower.get_edge_center(LEFT)[0], x_ref_line.get_center()[1], 0]),
            color=BLUE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        x_annot = MathTex('x_A', color=GREEN).scale(0.6).next_to(x_arrow, DOWN, buff=0.15)
        #endregion

        self.play(
            ShowCreation(e_line),
            ShowCreation(r_line),
            ShowCreation(theta_line),
            Write(cam_center_dot)
        )
        self.play(
            Write(e_arrow),
            Write(e_annot),
            Write(r_arrow),
            Write(r_annot),
            Write(theta_arc),
            Write(theta_annot),
            ShowCreation(x_ref_line),
            Write(x_arrow),
            Write(x_annot)
        )
        self.wait()

        diagram_withannot = Group(
            diagram,
            e_line,
            r_line,
            theta_line,
            cam_center_dot,
            e_arrow,
            e_annot,
            r_arrow,
            r_annot,
            theta_arc,
            theta_annot,
            x_ref_line,
            x_arrow,
            x_annot
        )
        self.play(
            Transform(diagram_withannot, diagram_withannot.copy().to_corner(DOWN+LEFT, buff=1))
        )
        self.wait()

        #region Math it out

        position = MathTex('x_A = e\\cos\\theta + r').scale(0.8).next_to(theta_dot, DOWN, aligned_edge=LEFT)
        velocity = MathTex('v_A = \\dot{x}_A = -e\\dot{\\theta}\\sin\\theta', '= e\\omega\\sin\\theta').scale(0.8).next_to(position, DOWN, aligned_edge=LEFT)
        acceleration = MathTex('a_A = \\ddot{x}_A = -e\\ddot{\\theta}\\sin\\theta - e\\dot{\\theta}^2\\cos\\theta', '= - e\\omega^2\\cos\\theta').scale(0.8).next_to(velocity, DOWN, aligned_edge=LEFT)

        self.play(Write(position))
        self.wait()
        self.play(Write(velocity[0]))
        self.wait()
        self.play(Write(velocity[1]))
        hlbox1 = SurroundingRectangle(velocity[1], buff=0.1)
        self.play(ShowCreation(hlbox1))
        self.wait()
        self.play(Write(acceleration[0]))
        self.wait()
        self.play(Write(acceleration[1]))
        hlbox2 = SurroundingRectangle(acceleration[1], buff=0.1)
        self.play(ShowCreation(hlbox2))
        self.wait()
        #endregion
