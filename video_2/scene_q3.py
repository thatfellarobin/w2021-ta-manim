from manim import *
import numpy as np

DIAGRAM_SCALE = 12
DIM_A = 0.4*DIAGRAM_SCALE
DIM_B = 0.5*DIAGRAM_SCALE
DIAGRAM_ORIGIN = 5.5*LEFT + 3*DOWN

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
        peg = Dot(point=path_function(START_ANGLE)+DIAGRAM_ORIGIN, color=YELLOW)

        slot_1 = Line(start=0.1*UP+DIM_B*RIGHT, end=0.1*UP)
        slot_2 = Line(start=0.1*DOWN, end=0.1*DOWN+DIM_B*RIGHT)
        slot_arc = Arc(start_angle=PI/2, angle=PI, radius=0.1)
        slot = slot_1.copy()
        slot.append_vectorized_mobject(slot_arc)
        slot.append_vectorized_mobject(slot_2)
        slot.shift(DIAGRAM_ORIGIN).rotate(START_ANGLE, about_point=DIAGRAM_ORIGIN).set_color(TEAL)

        # Annotations
        theta_dot = MathTex('\\dot{\\theta}=3\\,\\mathrm{rad/s}', color=YELLOW).scale(0.8).shift(1.5*RIGHT+3*UP)
        theta_dot_explain = Tex('For this animation, I slowed it down', 'so we can see what\'s happening').scale(0.7).next_to(theta_dot, DOWN, aligned_edge=LEFT)
        theta_dot_explain[1].next_to(theta_dot_explain[0], DOWN, aligned_edge=LEFT)

        # Updaters
        def slot_updater(slot):
            target_direction = peg.get_center() - DIAGRAM_ORIGIN
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

        # Show diagram elements
        self.play(
            ShowCreation(x_axis),
            ShowCreation(y_axis)
        )
        self.play(ShowCreation(path))
        self.play(
            FadeIn(peg),
            FadeIn(slot)
        )


        slot.add_updater(slot_updater)
        self.wait()

        # Animate rotation
        dt = 1/60
        angle_values = np.arange(START_ANGLE, EXIT_THETA, dt*THETA_DOT)
        partial_angle_values = np.arange(START_ANGLE, EXIT_THETA*0.75, dt*THETA_DOT)

        resampled_path = VMobject()
        resampled_path.set_points_as_corners([path_function(START_ANGLE), path_function(START_ANGLE)])
        for theta in angle_values:
            resampled_path.add_points_as_corners([path_function(theta)])
        resampled_path.set_opacity(0).shift(DIAGRAM_ORIGIN)
        self.add(resampled_path)

        resampled_partial_path = VMobject()
        resampled_partial_path.set_points_as_corners([path_function(START_ANGLE), path_function(START_ANGLE)])
        for theta in partial_angle_values:
            resampled_partial_path.add_points_as_corners([path_function(theta)])
        resampled_partial_path.set_opacity(0).shift(DIAGRAM_ORIGIN)
        self.add(resampled_partial_path)

        travel_time = (EXIT_THETA - START_ANGLE) / THETA_DOT
        partial_travel_time = (EXIT_THETA*0.75 - START_ANGLE) / THETA_DOT
        self.play(Write(theta_dot))
        self.play(Write(theta_dot_explain))
        self.wait()
        self.play(MoveAlongPath(peg, resampled_partial_path), rate_func=linear, run_time=partial_travel_time)
        self.play(Transform(peg, peg, run_time=0.1)) # to get the peg and slot to line up properly at the end of motion
        self.wait()
        # TODO: Add explainer of different measurements
        r_line = Line(DIAGRAM_ORIGIN, peg.get_center())
        r_annot = Brace(r_line, direction=r_line.copy().rotate(-PI / 2).get_unit_vector())
        r_annot_text = r_annot.get_tex("r", buff=0.1).set_color(RED)
        b_line = Line(DIAGRAM_ORIGIN, DIAGRAM_ORIGIN+DIM_B*r_line.get_unit_vector())
        b_annot = Brace(b_line, direction=b_line.copy().rotate(PI / 2).get_unit_vector())
        b_annot_text = b_annot.get_tex("b", buff=0.1).set_color(RED)
        theta_annot = Arc(
            start_angle=0,
            angle=np.arctan(r_line.get_unit_vector()[1]/r_line.get_unit_vector()[0]),
            radius=1.5,
            color=YELLOW,
            arc_center=DIAGRAM_ORIGIN
        ).add_tip(tip_length=0.2)
        theta_annot_text = MathTex('\\theta', color=YELLOW).scale(0.8).next_to(theta_annot, RIGHT)

        # self.play(Transform(path, path.copy().set_color())))
        self.play(ShowCreation(theta_annot))
        self.play(Write(theta_annot_text))
        self.wait()
        self.play(ShowCreation(r_annot))
        self.play(Write(r_annot_text))
        self.wait()
        self.play(ShowCreation(b_annot))
        self.play(Write(b_annot_text))
        self.wait()
        self.play(
            FadeOut(theta_annot),
            FadeOut(theta_annot_text),
            FadeOut(r_annot),
            FadeOut(r_annot_text),
            FadeOut(b_annot),
            FadeOut(b_annot_text)
        )

        self.play(MoveAlongPath(peg, resampled_partial_path.copy().reverse_points()), rate_func=smooth, run_time=1)
        self.wait()
        self.play(MoveAlongPath(peg, resampled_path), rate_func=linear, run_time=travel_time)
        self.play(Transform(peg, peg, run_time=0.1)) # to get the peg and slot to line up properly at the end of motion

        # Show that b and r are equal
        r_line = Line(DIAGRAM_ORIGIN, peg.get_center())
        r_annot = Brace(r_line, direction=r_line.copy().rotate(-PI / 2).get_unit_vector())
        r_annot_text = r_annot.get_tex("r", buff=0.1).set_color(RED)
        b_line = Line(DIAGRAM_ORIGIN, DIAGRAM_ORIGIN+DIM_B*r_line.get_unit_vector())
        b_annot = Brace(b_line, direction=b_line.copy().rotate(PI / 2).get_unit_vector())
        b_annot_text = b_annot.get_tex("b", buff=0.1).set_color(RED)
        r_equals_b = Tex('the peg exits when', '$r=b$').scale(0.8).next_to(theta_annot_text, DOWN, aligned_edge=LEFT)
        r_equals_b[1].set_color(RED).next_to(r_equals_b[0], RIGHT)
        self.play(
            FadeIn(r_annot),
            FadeIn(b_annot)
        )
        self.play(
            Write(r_annot_text),
            Write(b_annot_text)
        )
        self.wait()
        self.play(Write(r_equals_b))
        self.wait()
        # TODO: Find the angle of exit

        # TODO: Explain the rest of the fucking problem

