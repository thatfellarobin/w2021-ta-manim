from manim import *
import numpy as np

MED_DARK_GREY = '#666666'
GOLD_DARK = '#5c4326'
BLUE_E_DARK = '#0c343d'
GREEN_DARK = '#2b4022'

class T5P2(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Diagram imagery (up position)
        car = Rectangle(
            width=1.75,
            height=1,
            color=GREEN,
            fill_color=GREEN_DARK,
            fill_opacity=1
        )
        hinge = Dot(
            color=GREEN,
            radius=0.1
        )
        rod = Line(
            start=ORIGIN,
            end=2*UP,
            color=YELLOW_A,
            stroke_width=6
        )
        bob = Dot(
            point=rod.get_end(),
            color=BLUE_E,
            radius=0.25
        )
        ground = Line(
            start=2*LEFT,
            end=2*RIGHT,
            color=GREY
        ).move_to(car.get_edge_center(DOWN))

        l_arrow = DoubleArrow(
            start=rod.get_start(),
            end=rod.get_end(),
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).next_to(rod, LEFT)
        l_label = MathTex('l', color=YELLOW).scale(0.8).next_to(l_arrow, LEFT)
        car_mass_label = MathTex('\\textbf{2m}').scale(0.7).next_to(car.get_center(), RIGHT, buff=0.2)
        bob_mass_label = MathTex('\\textbf{2m}').scale(0.6).move_to(bob.get_center())
        ground_frictionless_arrow = Arrow(
            start=ground.get_end()+1*LEFT+0.5*DOWN,
            end=ground.get_end()+0.5*LEFT,
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        ground_frictionless_label = Tex('frictionless surface', color=YELLOW).scale(0.6).next_to(ground_frictionless_arrow.get_start(), LEFT, buff=0.2)
        t0_label = MathTex('t_0', color=YELLOW).scale(0.8).next_to(ground, UP, buff=2, aligned_edge=LEFT)
        #endregion

        diagram_up = Group(
            ground,
            car,
            rod,
            hinge,
            bob,
            l_arrow,
            l_label,
            car_mass_label,
            bob_mass_label,
            ground_frictionless_arrow,
            ground_frictionless_label,
            t0_label
        )
        self.add(diagram_up)
        self.wait()

        self.play(Transform(diagram_up, diagram_up.copy().shift(2.75*LEFT)))
        self.wait()

        #region Diagram imagery (down position)
        car_down = Rectangle(
            width=1.75,
            height=1,
            color=GREEN,
            fill_color=GREEN_DARK,
            fill_opacity=1
        )
        hinge_down = Dot(
            color=GREEN,
            radius=0.1
        )
        rod_down = Line(
            start=ORIGIN,
            end=2*DOWN,
            color=YELLOW_A,
            stroke_width=6
        )
        bob_down = Dot(
            point=rod_down.get_end(),
            color=BLUE_E,
            radius=0.25
        )
        ground_down = Line(
            start=2*LEFT,
            end=2*RIGHT,
            color=GREY
        ).move_to(car_down.get_edge_center(DOWN))

        diagram_down = Group(
            ground_down,
            car_down,
            rod_down,
            hinge_down,
            bob_down
        ).shift(2.75*RIGHT)
        transition_arrow = Arrow(
            start=0.5*LEFT,
            end=0.5*RIGHT,
            color=YELLOW_A,
            buff=0.0,
            stroke_width=10,
            tip_length=0.3,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        self.play(
            FadeIn(transition_arrow),
            FadeIn(diagram_down)
        )
        theta_dot_arrow = Arc(
            radius=1.5,
            arc_center=hinge_down.get_center(),
            start_angle=-PI*(4/10),
            angle=-PI*(2/10),
            color=YELLOW
        ).add_tip(tip_length=0.2)
        theta_dot_label = MathTex('\\dot{\\theta}', color=YELLOW).scale(0.8).next_to(theta_dot_arrow.get_end(), LEFT, buff=0.15)
        vx_arrow = Arrow(
            start=car_down.get_edge_center(RIGHT),
            end=car_down.get_edge_center(RIGHT)+RIGHT,
            color=BLUE,
            buff=0.0,
            stroke_width=7,
            tip_length=0.25,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        vx_label = MathTex('v_x', color=BLUE).scale(0.8).next_to(vx_arrow, RIGHT, buff=0.15)
        t1_label = MathTex('t_1', color=YELLOW).scale(0.8).next_to(ground_down, UP, buff=2, aligned_edge=LEFT)
        diagram_down = Group(
            diagram_down,
            theta_dot_arrow,
            theta_dot_label,
            vx_arrow,
            vx_label,
            t1_label
        )

        self.play(
            Write(theta_dot_arrow),
            Write(theta_dot_label),
            Write(vx_arrow),
            Write(vx_label),
            Write(t1_label)
        )
        self.wait()
        #endregion

        diagram_all = Group(
            diagram_up,
            transition_arrow,
            diagram_down
        )
        self.play(Transform(diagram_all, diagram_all.copy().scale(0.8).to_corner(DOWN+LEFT)))
        self.wait()

        #region Conservation of momentum
        impulse = MathTex('J=\\int F\\,\\mathrm{d}t = \\Delta p').scale(0.8).to_corner(UP+LEFT)
        impulse_eq = MathTex(
            '0',
            '=',
            '2mv_x + 2m(v_x-l\\dot{\\theta})',
            '-',
            '0'
        ).scale(0.8).next_to(impulse, DOWN, aligned_edge=LEFT)
        self.play(Write(impulse))
        self.wait()
        self.play(Write(impulse_eq[:2]))
        self.wait()
        self.play(Write(impulse_eq[2]))
        self.wait()
        self.play(Write(impulse_eq[3:]))
        self.wait()
        self.play(FadeOut(impulse_eq[3:]))
        self.wait()
        hlbox_1 = SurroundingRectangle(impulse_eq[:3])
        self.play(ShowCreation(hlbox_1))
        #endregion

        #region Conservation of energy

        #endregion
