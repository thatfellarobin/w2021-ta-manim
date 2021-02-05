from manim import *
import numpy as np

TEAL_DARK = '#1c4037'
GREEN_DARK = '#2b4022'
BLUE_E_DARK = '#0c343d'
GREY_BLUE = '#465778'
GREY_BLUE_DARK = '#2d384d'
GOLD_DARK = '#5c4326'


class P1(Scene):
    def construct(self):

        #region Diagram imagery

        # Basic pulley shape
        pulley_outer = Circle(
            radius=0.25,
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1.0,
            stroke_width=5.0
        )
        pulley_axle = Circle(
            radius=0.1,
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1.0,
            stroke_width=5.0
        )
        pulley = Group(pulley_outer, pulley_axle)

        block_A = Rectangle(
            color=GOLD,
            fill_color=GOLD_DARK,
            height=1.25,
            width=1.25,
            mark_paths_closed=True,
            close_new_points=True,
            stroke_width=4,
            fill_opacity=1
        ).shift(3*LEFT + 2.5*UP)
        pulley_A = pulley.copy().next_to(block_A, RIGHT)
        pulley_tie_A = Line(
            start=block_A.get_edge_center(RIGHT),
            end=pulley_A.get_center(),
            color=GOLD_E
        )
        string_1 = Line(
            start=pulley_A.get_edge_center(UP),
            end=pulley_A.get_edge_center(UP) + 3*RIGHT,
            color=YELLOW_E
        )
        string_2 = Line(
            start=pulley_A.get_edge_center(DOWN),
            end=pulley_A.get_edge_center(DOWN) + 2*RIGHT,
            color=YELLOW_E
        )
        pulley_mid = pulley.copy()
        pulley_mid.shift(string_2.get_end() - pulley_mid.get_edge_center(UP))
        string_3 = Line(
            start=pulley_mid.get_edge_center(RIGHT),
            end=pulley_mid.get_edge_center(RIGHT) + 3*DOWN,
            color=YELLOW_E
        )
        block_B = Rectangle(
            color=TEAL,
            fill_color=TEAL_DARK,
            height=1.25,
            width=1.25,
            mark_paths_closed=True,
            close_new_points=True,
            stroke_width=4,
            fill_opacity=1
        )
        block_B.shift(string_3.get_end() - block_B.get_edge_center(UP))

        ground_A = Line(
            start=np.array([block_B.get_edge_center(LEFT)[0], block_A.get_edge_center(DOWN)[1], 0]),
            end=np.array([block_A.get_edge_center(LEFT)[0], block_A.get_edge_center(DOWN)[1], 0])+1*LEFT,
            color=GREY
        )
        ground_B = Line(
            start=np.array([block_B.get_edge_center(LEFT)[0], block_A.get_edge_center(DOWN)[1], 0]),
            end=np.array([block_B.get_edge_center(LEFT)[0], block_B.get_edge_center(DOWN)[1], 0])+1*DOWN,
            color=GREY
        )
        ground_string = Line(
            start=0.25*DOWN,
            end=0.25*UP,
            color=GREY
        ).move_to(string_1.get_end())
        pulley_mid_support = Line(
            start=pulley_mid.get_center(),
            end=ground_A.get_start(),
            color=GREY,
            stroke_width=8.0
        )

        # Conservation of string items
        s_A_ref = Line(
            start=ORIGIN,
            end=0.5*UP,
            color=GREEN
        ).next_to(pulley_mid, direction=UP, buff=0.75)
        s_B_ref = Line(
            start=ORIGIN,
            end=0.5*RIGHT,
            color=GREEN
        ).next_to(pulley_mid, direction=RIGHT)
        s_A_arrow = Arrow(
            start=string_2.get_end(),
            end=string_2.get_start(),
            color=GREEN,
            buff=0.0,
            stroke_width=6,
            tip_length=0.25,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(-string_2.get_end() + s_A_ref.get_center())
        s_B_arrow = Arrow(
            start=string_3.get_start(),
            end=string_3.get_end(),
            color=GREEN,
            buff=0.0,
            stroke_width=6,
            tip_length=0.25,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(-string_3.get_start() + s_B_ref.get_center())
        s_A_ref.scale_about_point(scale_factor=2, point=s_A_ref.get_end())

        # Group objects and rotate scene
        diagram_static = Group(
            string_1,
            string_2,
            string_3,
            pulley_A,
            pulley_mid,
            pulley_tie_A,
            block_A,
            block_B,
            ground_A,
            ground_B,
            ground_string,
            pulley_mid_support
        )
        diagram_stringAnnot = Group(diagram_static, s_A_ref, s_B_ref, s_A_arrow, s_B_arrow)
        diagram_stringAnnot.rotate(angle=60*(PI/180)).move_to(ORIGIN)

        text_A = Tex("A", color=WHITE).move_to(block_A.get_center()).scale(1.2)
        text_B = Tex("B", color=WHITE).move_to(block_B.get_center()).scale(1.2)

        #endregion
        self.add(diagram_static, text_A, text_B)
        self.wait()

        #region Annotate angles
        angref_A = Line(
            start=ORIGIN,
            end=1.25*RIGHT,
            color=YELLOW
        ).next_to(ground_A.get_end(), RIGHT, buff=0.2)
        angref_B = angref_A.copy().next_to(ground_B.get_end(), LEFT, buff=0.2)
        ang_A = Arc(
            radius=1,
            arc_center=ground_A.get_end(),
            start_angle=0,
            angle=60*(PI/180),
            color=YELLOW
        ).add_tip(tip_length=0.2)
        ang_B = Arc(
            radius=1,
            arc_center=ground_B.get_end(),
            start_angle=PI,
            angle=-30*(PI/180),
            color=YELLOW
        ).add_tip(tip_length=0.2)
        ang_A_annot = MathTex('\\theta_1=60^{\\circ}', color=YELLOW).scale(0.8).next_to(ang_A, RIGHT, buff=0.1)
        ang_B_annot = MathTex('\\theta_2=30^{\\circ}', color=YELLOW).scale(0.8).next_to(ang_B, LEFT, buff=0.1)

        self.play(
            ShowCreation(angref_A),
            ShowCreation(angref_B),
            ShowCreation(ang_A),
            ShowCreation(ang_B),
            Write(ang_A_annot),
            Write(ang_B_annot)
        )
        self.wait()
        #endregion

        #region Discuss conservation of string
        # Annotate strings
        s_A_annot = MathTex('s_A', color=GREEN).scale(0.8).move_to(s_A_arrow.get_center()).shift(0.5*s_A_arrow.copy().rotate(-PI/2).get_unit_vector())
        s_B_annot = MathTex('s_B', color=GREEN).scale(0.8).move_to(s_B_arrow.get_center()).shift(0.5*s_B_arrow.copy().rotate(PI/2).get_unit_vector())
        self.play(
            ShowCreation(s_A_ref),
            ShowCreation(s_B_ref),
            ShowCreation(s_A_arrow),
            ShowCreation(s_B_arrow),
        )
        self.play(
            Write(s_A_annot),
            Write(s_B_annot)
        )
        self.wait()
        string_sum = MathTex('L_{tot}', '=', '2', 's_A', '+', 's_B').scale(0.9).shift(3.5*RIGHT + 3*UP)
        self.play(Write(string_sum))
        self.wait()
        string_sum_d = MathTex('0', '=', '2', 'v_A', '+', 'v_B').scale(0.9)
        string_sum_d.shift((string_sum[1].get_center()+0.75*DOWN)-string_sum_d[1].get_center())
        self.play(Write(string_sum_d))
        self.wait()
        # briefly explain why we can leave out certain sections of string
        string_1_subsec = string_1.copy().scale_about_point(point=string_1.get_end(), scale_factor=(1/3))
        for _ in range(3):
            self.play(CircleIndicate(string_1_subsec))
        self.wait()

        #endregion

        diagram_fullyAnnot = Group(
            diagram_stringAnnot,
            text_A,
            text_B,
            angref_A,
            angref_B,
            ang_A,
            ang_B,
            ang_A_annot,
            ang_B_annot,
            s_A_annot,
            s_B_annot
        )
        string_sum_grouped = Group(string_sum, string_sum_d)

        # At this point, should explain how to identify energy problem?

        # Prepare to do math
        self.play(
            Transform(diagram_fullyAnnot, diagram_fullyAnnot.copy().scale(0.8).shift(3.5*LEFT+1*UP)),
            Transform(string_sum_grouped, string_sum_grouped.copy().scale(0.8).to_edge(LEFT).shift(0.5*RIGHT+5*DOWN))
        )
        self.wait()