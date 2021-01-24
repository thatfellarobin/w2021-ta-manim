from manim import *
import numpy as np

DIAGRAM_SCALE = 12
DIM_A = 0.4*DIAGRAM_SCALE
DIM_B = 0.5*DIAGRAM_SCALE
DIAGRAM_ORIGIN = 5*LEFT + 3*DOWN

THETA_DOT = 0.5 # rad/s

START_ANGLE=0.05
EXIT_THETA = DIM_B/DIM_A

class P3(Scene):
    def construct(self):
        def path_function(theta):
            r = DIM_A * theta
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            return np.array([x, y, 0])

        # Scene objects
        x_axis = Line(start=DIAGRAM_ORIGIN, end=DIAGRAM_ORIGIN+4*RIGHT, color=GRAY)
        y_axis = Line(start=DIAGRAM_ORIGIN, end=DIAGRAM_ORIGIN+6*UP, color=GRAY)
        path = ParametricFunction(path_function, t_min=START_ANGLE, t_max=EXIT_THETA, fill_opacity=0, color=PURPLE).shift(DIAGRAM_ORIGIN)
        marble = Dot(point=path_function(START_ANGLE)+DIAGRAM_ORIGIN, color=YELLOW)

        slot_1 = Line(start=0.1*UP+DIM_B*RIGHT, end=0.1*UP)
        slot_2 = Line(start=0.1*DOWN, end=0.1*DOWN+DIM_B*RIGHT)
        slot_arc = Arc(start_angle=PI/2, angle=PI, radius=0.1)
        slot = slot_1.copy()
        slot.append_vectorized_mobject(slot_arc)
        slot.append_vectorized_mobject(slot_2)
        slot.shift(DIAGRAM_ORIGIN).rotate(START_ANGLE, about_point=DIAGRAM_ORIGIN).set_color(TEAL)

        # Annotations


        # Updaters
        def slot_updater(slot):
            target_direction = marble.get_center() - DIAGRAM_ORIGIN
            current_direction = slot.get_center() - DIAGRAM_ORIGIN
            if target_direction[0] == 0:
                target_angle = 0
            else:
                target_angle = np.arctan(target_direction[1]/target_direction[0])
            if current_direction[0] == 0:
                current_angle = 0
            else:
                current_angle = np.arctan(current_direction[1]/current_direction[0])
            newslot = slot.copy().rotate(target_angle-current_angle, about_point=DIAGRAM_ORIGIN)
            slot.become(newslot)

        self.play(
            ShowCreation(x_axis),
            ShowCreation(y_axis)
        )
        self.play(ShowCreation(path))
        self.play(
            FadeIn(marble),
            FadeIn(slot)
        )


        slot.add_updater(slot_updater)
        self.wait()

        # Animate rotation
        dt = 1/60
        angle_values = np.arange(START_ANGLE, EXIT_THETA, dt*THETA_DOT)
        travel_time = (EXIT_THETA - START_ANGLE) / THETA_DOT
        resampled_path = VMobject()
        resampled_path.set_points_as_corners([path_function(START_ANGLE), path_function(START_ANGLE)])
        for theta in angle_values:
            resampled_path.add_points_as_corners(path_function(theta))
        resampled_path.set_opacity(0)
        self.add(resampled_path)
        # self.play(Transform(marble, marble.copy().move_to(path_function(theta)), rate_func=linear, run_time=dt))

        self.play(MoveAlongPath(marble, resampled_path), rate_func=linear, run_time=travel_time)
        self.wait()