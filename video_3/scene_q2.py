from manim import *
import numpy as np

ROD_LENGTH = 4.0
BLUE_E_DARK = '#0c343d'

class Q2(Scene):
    def construct(self):
        #region Diagram imagery
        particle = Dot(radius=0.2, color=YELLOW)
        track_up = Rectangle(
            height=0.1,
            width=5.0,
            fill_color=GREY,
            fill_opacity=1,
            stroke_opacity=0
        ).next_to(particle, UP, buff=0).shift(1*LEFT)
        track_down = Rectangle(
            height=0.1,
            width=5.0,
            fill_color=GREY,
            fill_opacity=1,
            stroke_opacity=0
        ).next_to(particle, DOWN, buff=0).shift(1*LEFT)
        rod = Line(
            start=np.array([0.8*np.sin(30*(np.pi/180)), 0.8*np.cos(30*(np.pi/180)), 0]),
            end=np.array([-ROD_LENGTH*np.sin(30*(np.pi/180)), -ROD_LENGTH*np.cos(30*(np.pi/180)), 0]),
            color=BLUE_E,
            stroke_width=20.0
        )
        rod.shift(0.34*LEFT)
        hinge = Circle(
            arc_center=rod.get_end(),
            radius=0.2,
            stroke_width=10.0,
            fill_color=BLUE_E,
            stroke_color=BLUE_E_DARK,
            fill_opacity=1.0,
            stroke_opacity=1.0,
        )
        diagram = Group(track_up, track_down, particle, rod, hinge).move_to(ORIGIN)
        self.add(diagram)
        self.wait()
        #endregion

        #region Diagram annotations
        # Fade out diagram
        mask = Rectangle(width=diagram.get_width()+0.2, height=diagram.get_height()+0.2, color=BLACK, stroke_opacity=0, fill_opacity=0.3).move_to(diagram.get_center())
        self.play(FadeIn(mask))

        r_arrow = Arrow(
            start=rod.get_end(),
            end=particle.get_center(),
            color=GREEN,
            buff=0.0,
            stroke_width=8,
            tip_length=0.3,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        r_arrow_angle = np.arctan(r_arrow.get_unit_vector()[1] / r_arrow.get_unit_vector()[0])
        r_annot = MathTex('r', color=GREEN).next_to(r_arrow.get_center(), np.array([np.cos(-np.pi/4), np.sin(-np.pi/4), 0]))
        self.play(ShowCreation(r_arrow, run_time=1.5), Write(r_annot))
        self.wait()

        theta_ref = Line(
            start=hinge.get_center(),
            end=hinge.get_center()+2.5*UP,
            color=GREY
        )
        theta_arrow = Arc(
            start_angle=PI/2,
            angle=-(PI/2)+r_arrow_angle,
            radius=2,
            arc_center=hinge.get_center(),
            color=YELLOW
        ).add_tip(tip_length=0.2)
        theta_annot = MathTex('\\theta=30^{\\circ}', color=YELLOW).scale(0.7).next_to(theta_arrow, UP, buff=0.1).shift(0.1*RIGHT)
        self.play(
            ShowCreation(theta_ref),
            ShowCreation(theta_arrow),
            Write(theta_annot)
        )
        self.wait()

        h_ref = Line(
            start=hinge.get_center(),
            end=hinge.get_center()+4*RIGHT,
            color=GREY
        )
        h_value = np.array([0, (particle.get_center() - hinge.get_center())[1], 0])
        h_arrow = DoubleArrow(
            start=particle.get_center() - h_value,
            end=particle.get_center(),
            color=GREEN,
            buff=0.0,
            stroke_width=8,
            tip_length=0.3,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(0.75*RIGHT)
        h_annot = MathTex('h=0.5\\,\\mathrm{m}').scale(0.7).next_to(h_arrow, RIGHT, buff=0.1)
        self.play(
            ShowCreation(h_ref),
            ShowCreation(h_arrow),
            ShowCreation(h_annot)
        )
        self.wait()
        #endregion

        full_diagram = Group(diagram, mask, r_arrow, r_annot, theta_ref, theta_arrow, theta_annot, h_ref, h_arrow, h_annot)
        self.play(Transform(full_diagram, full_diagram.copy().scale(0.8).shift(4.5*LEFT+1.5*UP)))
        given_theta_dot = MathTex('\\dot{\\theta}=2\\,\\mathrm{rad/s}').scale(0.7).next_to(full_diagram, DOWN, aligned_edge=LEFT)
        given_theta_ddot = MathTex('\\ddot{\\theta}=3\\,\\mathrm{rad/s^2}').scale(0.7).next_to(given_theta_dot, DOWN, aligned_edge=LEFT)
        self.play(
            Write(given_theta_dot),
            Write(given_theta_ddot)
        )
        self.wait()

        #region Calculations arising from the geometry
        geom_1 = MathTex(
            'h=r\\cos(\\theta)',
            '\\Rightarrow',
            'r',
            '=',
            '\\frac{h}{\\cos(\\theta)}',
            '=',
            '0.58\\,\\mathrm{m}'
        ).scale(0.7).to_edge(UP).shift(1.5*RIGHT)
        geom_1[2:].set_color(YELLOW)
        self.play(Write(geom_1[0]))
        self.wait()
        self.play(Write(geom_1[1:]))
        self.wait()

        hlbox = SurroundingRectangle(geom_1[0], buff=0.1)
        self.play(ShowCreation(hlbox))
        self.wait()

        # First derivative
        geom_d1 = MathTex(
            '0=\\dot{r}\\cos(\\theta)-r\\sin(\\theta)\\dot{\\theta}',
            '\\Rightarrow',
            '\\dot{r}',
            '=',
            '\\frac{r\\sin(\\theta)}{\\cos(\\theta)}\\dot{\\theta}',
            '=',
            '0.67\\,\\mathrm{m/s}'
        ).scale(0.7).next_to(geom_1, DOWN, aligned_edge=LEFT)
        geom_d1[2:].set_color(YELLOW)
        self.play(FadeOut(hlbox), Write(geom_d1))
        self.wait()

        # Second derivative
        geom_d2 = MathTex(
            '0',
            '=',
            '\\ddot{r}\\cos(\\theta) - 2\\dot{r}\\sin(\\theta)\\dot{\\theta} - r\\cos(\\theta)\\dot{\\theta}^2 - r\\sin(\\theta)\\ddot{\\theta}',
            '\\Rightarrow',
            '\\ddot{r}',
            '=',
            '2\\dot{r}\\dot{\\theta}\\tan(\\theta) + r\\dot{\\theta}^2 + r\\tan(\\theta)\\ddot{\\theta}',
            '\\ddot{r}',
            '=',
            '4.85\\,\\mathrm{m/s^2}'
        ).scale(0.7).next_to(geom_d1, DOWN, aligned_edge=LEFT)
        geom_d2[-3:].set_color(YELLOW)
        geom_d2[4:].shift((geom_d2[1].get_center()+0.7*DOWN)-geom_d2[5].get_center())
        geom_d2[7:].shift((geom_d2[5].get_center()+0.7*DOWN)-geom_d2[8].get_center())
        self.play(Write(geom_d2[:7]))
        self.wait()
        self.play(Write(geom_d2[7:]))
        self.wait()

        # Cleanup
        self.play(
            FadeOut(geom_1[:2]),
            FadeOut(geom_1[4:6]),
            FadeOut(geom_d1[:2]),
            FadeOut(geom_d1[4:6]),
            FadeOut(geom_d2[:-3]),
            Transform(geom_1[-1], geom_1[-1].copy().shift(geom_1[3].get_center() - geom_1[-2].get_center())),
            Transform(geom_d1[-1], geom_d1[-1].copy().shift(geom_d1[3].get_center() - geom_d1[-2].get_center()))
        )
        self.wait()
        geom_1_result = Group(geom_1[2:4], geom_1[-1])
        geom_d1_result = Group(geom_d1[2:4], geom_d1[-1])
        geom_d2_result = Group(geom_d2[-3:])
        geom_1_result_newpos = geom_1_result.copy().to_edge(UP, buff=0.75).shift(2*LEFT)
        geom_d1_result_newpos = geom_d1_result.copy().next_to(geom_1_result_newpos, RIGHT, buff=0.75).shift(0.04*DOWN)
        geom_d2_result_newpos = geom_d2_result.copy().next_to(geom_d1_result_newpos, RIGHT, buff=0.75).shift(0.02*UP)
        self.play(
            Transform(geom_1_result, geom_1_result_newpos),
            Transform(geom_d1_result, geom_d1_result_newpos),
            Transform(geom_d2_result, geom_d2_result_newpos)
        )
        #endregion

        #region Free body diagram

        #endregion