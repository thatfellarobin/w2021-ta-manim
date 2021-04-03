from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

DSCALE = 2

class T11P1(Scene):
    def number_equation(self, eq, n, color=YELLOW_B):
        num = MathTex('\\textbf{' + str(n) + '}', color=color).scale(0.5)
        circle = Circle(
            color=color,
            radius=0.225,
            arc_center=num.get_center()
        )
        line = Line(
            start=circle.get_edge_center(LEFT),
            end=circle.get_edge_center(LEFT)+0.6*LEFT,
            color=color
        )
        group = Group(num, circle, line)
        group.next_to(eq, RIGHT, buff=0.25)
        self.play(FadeIn(group))
        return group

    def recursive_set_opacity(self, mobj, opacity=0):
        for item in mobj:
            if len(item) > 1:
                self.recursive_set_opacity(mobj=item, opacity=opacity)
            else:
                item.set_opacity(opacity)
        return mobj

    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Diagram objects
        def create_A_frame():
            left = Line(
                start=0.4*LEFT+1.3*DOWN,
                end=ORIGIN,
                color=BROWN,
                stroke_width=12
            )
            right = left.copy().flip(axis=UP)
            right.shift(left.get_end()-right.get_end())
            horiz = Line(
                start=left.get_center(),
                end=right.get_center(),
                color=BROWN,
                stroke_width=12
            )
            pivot = Dot(
                point=left.get_end(),
                color=BROWN,
                radius=0.12
            )
            Aframe = Group(left, right, horiz, pivot)
            return Aframe

        ground = Line(
            start=3*LEFT,
            end=3*RIGHT,
            color=GREY
        )

        A_frame_left = create_A_frame().shift(DSCALE*0.5*LEFT).align_to(ground, DOWN)
        A_frame_right = create_A_frame().shift(DSCALE*0.5*RIGHT).align_to(ground, DOWN)

        beam = Rectangle(
            height=0.125,
            width=DSCALE*2*(0.9+0.5),
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1
        ).next_to(Group(A_frame_left, A_frame_right), UP, buff=0)

        diagram = Group(
            ground,
            A_frame_left,
            A_frame_right,
            beam
        ).move_to(ORIGIN)
        self.add(diagram)
        self.wait()
        #endregion

        #region Annotate diagram
        point_A = Dot(
            point=A_frame_left.get_edge_center(UP),
            radius=0.05,
            color=YELLOW
        ).shift((0.125/2)*UP) # shift up half of beams height. tried to use .align_to(), but it's broken >:(
        point_A_label = MathTex('A', color=YELLOW).scale(0.6).next_to(point_A, DOWN, buff=0.15)
        point_B = Dot(
            point=A_frame_right.get_edge_center(UP),
            radius=0.05,
            color=YELLOW
        ).shift((0.125/2)*UP) # shift up half of beams height. tried to use .align_to(), but it's broken >:(
        point_B_label = MathTex('B', color=YELLOW).scale(0.6).next_to(point_B, DOWN, buff=0.15)
        point_C = Dot(
            point=beam.get_edge_center(LEFT),
            radius=0.05,
            color=YELLOW
        )
        point_C_label = MathTex('C', color=YELLOW).scale(0.6).next_to(point_C, LEFT, buff=0.15)
        point_D = Dot(
            point=beam.get_edge_center(RIGHT),
            radius=0.05,
            color=YELLOW
        )
        point_D_label = MathTex('D', color=YELLOW).scale(0.6).next_to(point_D, RIGHT, buff=0.15)
        point_G = Dot(
            point=beam.get_center(),
            radius=0.05,
            color=YELLOW
        )
        point_G_label = MathTex('G', color=YELLOW).scale(0.6).next_to(point_G, UP, buff=0.15)

        b_arrow_left = DoubleArrow(
            start=point_A.get_center(),
            end=point_G.get_center(),
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(1.75*DOWN)
        b_arrow_label_left = MathTex('b', color=YELLOW).scale(0.6).next_to(b_arrow_left, DOWN, buff=0.1)
        b_arrow_right = DoubleArrow(
            start=point_G.get_center(),
            end=point_B.get_center(),
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(1.75*DOWN)
        b_arrow_label_right = MathTex('b', color=YELLOW).scale(0.6).next_to(b_arrow_right, DOWN, buff=0.1)

        a_arrow_left = DoubleArrow(
            start=point_C.get_center(),
            end=point_A.get_center(),
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(1.75*DOWN)
        a_arrow_label_left = MathTex('a', color=YELLOW).scale(0.6).next_to(a_arrow_left, DOWN, buff=0.1)
        a_arrow_right = DoubleArrow(
            start=point_B.get_center(),
            end=point_D.get_center(),
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(1.75*DOWN)
        a_arrow_label_right = MathTex('a', color=YELLOW).scale(0.6).next_to(a_arrow_right, DOWN, buff=0.1)

        self.play(
            FadeIn(point_A),
            Write(point_A_label),
            FadeIn(point_B),
            Write(point_B_label),
            FadeIn(point_C),
            Write(point_C_label),
            FadeIn(point_D),
            Write(point_D_label),
            FadeIn(point_G),
            Write(point_G_label)
        )
        self.play(
            Write(b_arrow_left),
            Write(b_arrow_label_left),
            Write(b_arrow_right),
            Write(b_arrow_label_right),
            Write(a_arrow_left),
            Write(a_arrow_label_left),
            Write(a_arrow_right),
            Write(a_arrow_label_right),
        )
        self.wait()

        diagram = Group(
            diagram,
            point_A,
            point_A_label,
            point_B,
            point_B_label,
            point_C,
            point_C_label,
            point_D,
            point_D_label,
            point_G,
            point_G_label,
            b_arrow_left,
            b_arrow_label_left,
            b_arrow_right,
            b_arrow_label_right,
            a_arrow_left,
            a_arrow_label_left,
            a_arrow_right,
            a_arrow_label_right,
        )
        #endregion

        #region Animate the key points in time

        #endregion
