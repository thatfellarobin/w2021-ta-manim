from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

DIM_A=1.25


class T8P2(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Diagram objects
        gear = Circle(
            radius=DIM_A,
            stroke_color=BLUE_E,
            fill_color=BLUE_E_DARK,
            stroke_width=10,
            fill_opacity=1
        )
        gear_center = Dot(
            point=gear.get_center(),
            radius=0.1,
            color=BLUE_E
        )
        gear_group = Group(gear, gear_center)

        rack = Rectangle(
            width=5,
            height=0.5,
            color=RED_D,
            stroke_opacity=0,
            fill_opacity=1
        ).next_to(gear_group, DOWN, buff=0)

        diagram = Group(gear_group, rack).move_to(ORIGIN)
        self.add(diagram)
        self.wait()
        #endregion

        #region annotate diagram
        point_B = SmallDot(
            point=gear.get_edge_center(UP),
            color=YELLOW
        )
        point_B_annot = MathTex('B', color=YELLOW).scale(0.7).next_to(point_B, UP, buff=0.15)
        point_O = SmallDot(
            point=gear.get_center(),
            color=YELLOW
        )
        point_O_annot = MathTex('O', color=YELLOW).scale(0.7).next_to(point_O, DOWN+LEFT, buff=0.1)
        point_A = SmallDot(
            point=gear.get_edge_center(DOWN),
            color=YELLOW
        )
        point_A_annot = MathTex('A', color=YELLOW).scale(0.7).next_to(point_A, DOWN+RIGHT, buff=0)
        point_P_annot = MathTex('P', color=WHITE).scale(0.7).next_to(rack.get_edge_center(LEFT), RIGHT, buff=0.5)


        radius_arrow = DoubleArrow(
            start=gear.get_center(),
            end=gear.get_center()+DIM_A*np.array([np.cos(PI/4), np.sin(PI/4), 0]),
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        radius_annot = MathTex('0.15\\,\\mathrm{m}', color=YELLOW).scale(0.7).next_to(radius_arrow, UP+RIGHT, buff=0.15)
        gear_move_arrow = Arrow(
            start=gear.get_center(),
            end=gear.get_center()+2*RIGHT,
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        gear_move_annot = MathTex(
            'v_O = 3\\,\\mathrm{m/s}',
            'a_O = 6\\,\\mathrm{m/s^2}',
            color=YELLOW
        ).scale(0.7)
        gear_move_annot[1].next_to(gear_move_annot[0], DOWN, aligned_edge=LEFT, buff=0.1)
        gear_move_annot.next_to(gear_move_arrow, RIGHT, buff=0.1)
        rack_move_arrow = Arrow(
            start=rack.get_corner(UP+LEFT),
            end=rack.get_corner(UP+LEFT)+LEFT,
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        rack_move_annot = MathTex(
            'v_P = 2\\,\\mathrm{m/s}',
            'a_P = 3\\,\\mathrm{m/s^2}',
            color=YELLOW
        ).scale(0.7)
        rack_move_annot[1].next_to(rack_move_annot[0], DOWN, aligned_edge=RIGHT, buff=0.1)
        rack_move_annot.next_to(rack_move_arrow, LEFT, buff=0.1)

        self.play(
            Write(point_B),
            Write(point_B_annot),
            Write(point_A),
            Write(point_A_annot),
            Write(point_O),
            Write(point_O_annot),
            Write(point_P_annot),
            Write(radius_arrow),
            Write(radius_annot),
            Write(gear_move_arrow),
            Write(gear_move_annot),
            Write(rack_move_arrow),
            Write(rack_move_annot)
        )
        self.wait()

        diagram = Group(
            diagram,
            point_B,
            point_B_annot,
            point_O,
            point_O_annot,
            point_A,
            point_A_annot,
            point_P_annot,
            radius_arrow,
            radius_annot,
            gear_move_arrow,
            gear_move_annot,
            rack_move_arrow,
            rack_move_annot
        )
        #endregion

        #region Cleanup and show coordinate system
        diagram_newpos = diagram.copy().scale(0.65).to_corner(DOWN+RIGHT, buff=0.75)
        gear_copy = gear_group.copy()
        for item in gear_copy:
            item.set_opacity(0)
        gear_newpos = gear_group.copy().scale(0.9).next_to(diagram_newpos, UP, aligned_edge=RIGHT, buff=0.5).shift(2*LEFT)

        self.play(
            Transform(gear_copy, gear_newpos),
            Transform(diagram, diagram_newpos)
        )
        self.wait()

        # Create coordinate system
        i_arrow = Arrow(
            start=ORIGIN,
            end=RIGHT,
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        i_label = MathTex('\\hat{i}', color=YELLOW).scale(0.7).next_to(i_arrow, RIGHT, buff=0.15)
        j_arrow = Arrow(
            start=ORIGIN,
            end=UP,
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        j_label = MathTex('\\hat{j}', color=YELLOW).scale(0.7).next_to(j_arrow, UP, buff=0.15)
        k_dot = Dot(
            point=i_arrow.get_start(),
            color=YELLOW
        )
        k_circle = Circle(
            arc_center=k_dot.get_center(),
            radius=0.15,
            color=YELLOW
        )
        k_label = MathTex('\\hat{k}', color=YELLOW).scale(0.7).next_to(k_circle, LEFT, buff=0.15)
        coordsys = Group(i_arrow, j_arrow, i_label, j_label, k_dot, k_circle, k_label).scale(0.75).next_to(diagram, LEFT, buff=0.5, aligned_edge=DOWN)
        self.play(
            Write(i_arrow),
            Write(j_arrow),
            Write(i_label),
            Write(j_label),
            Write(k_dot),
            Write(k_circle),
            Write(k_label)
        )
        self.wait()
        #endregion

        #region Math it out
        #region Solving for omega
        gear_move_arrow2 = Arrow(
            start=gear_copy.get_center(),
            end=gear_copy.get_center()+(2/3)*3*RIGHT,
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        gear_move_annot2 = MathTex(
            'v_O = 3\\,\\mathrm{m/s}',
            color=YELLOW
        ).scale(0.6).next_to(gear_move_arrow2, RIGHT, buff=0.1)
        rack_move_arrow2 = Arrow(
            start=gear_copy.get_edge_center(DOWN),
            end=gear_copy.get_edge_center(DOWN)+(2/3)*2*LEFT,
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        rack_move_annot2 = MathTex(
            'v_P = 2\\,\\mathrm{m/s}',
            color=YELLOW
        ).scale(0.6).next_to(rack_move_arrow2, LEFT, buff=0.1)
        self.play(
            Write(gear_move_arrow2),
            Write(gear_move_annot2),
            Write(rack_move_arrow2),
            Write(rack_move_annot2)
        )
        self.wait()

        ic_joinline1 = Line(
            start=gear_move_arrow2.get_start(),
            end=rack_move_arrow2.get_start(),
            color=YELLOW,
            stroke_opacity=0.5
        )
        ic_joinline2 = Line(
            start=gear_move_arrow2.get_end(),
            end=rack_move_arrow2.get_end(),
            color=YELLOW,
            stroke_opacity=0.5
        )
        self.play(ShowCreation(ic_joinline1))
        self.wait()
        self.play(ShowCreation(ic_joinline2))
        self.wait()

        ic_anim_dist = np.linalg.norm(gear_copy.get_center() - gear_copy.get_edge_center(DOWN)) * (0.09/0.15)

        point_IC = Dot(
            point=gear_copy.get_center() + ic_anim_dist*DOWN,
            color=YELLOW
        )
        point_IC_annot = MathTex('IC', color=YELLOW).scale(0.6).next_to(point_IC, UP+LEFT, buff=0)
        self.play(FadeIn(point_IC))
        for _ in range(2):
            self.play(Flash(point_IC))
        self.play(Write(point_IC_annot))
        self.wait()

        #endregion



        #endregion