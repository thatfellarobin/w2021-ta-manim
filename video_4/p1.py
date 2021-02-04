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

        # Group objects and rotate scene
        diagram = Group(
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
        diagram.rotate(angle=60*(PI/180)).move_to(ORIGIN)

        text_A = Tex("A", color=WHITE).move_to(block_A.get_center()).scale(1.2)
        text_B = Tex("B", color=WHITE).move_to(block_B.get_center()).scale(1.2)

        diagram_withlabels = Group(diagram, text_A, text_B)

        self.add(diagram_withlabels)
        self.wait()
        #endregion

        #region Annotate angles
        angref_A = Line(
            start=ORIGIN,
            end=1.5*RIGHT,
            color=YELLOW
        ).next_to(ground_A.get_end(), RIGHT, buff=0.1)
        angref_B = angref_A.copy().next_to(ground_B.get_end(), LEFT, buff=0.1)
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

        diagram_withlabels_andangles = Group(
            diagram_withlabels,
            angref_A,
            angref_B,
            ang_A,
            ang_B,
            ang_A_annot,
            ang_B_annot
        )
        #endregion


        # A = Group(block_A, text_A)
        # B = Group(block_B, text_B)

        # floor = Line(start=3.5*LEFT, end=4.25*RIGHT, color=GREY).shift(A.get_edge_center(DOWN)[1]*UP)
        # wall = Line(start=ORIGIN, end=3.5*UP, color=GREY).shift(floor.get_end())

        # rope_tie_1 = Dot(
        #     color=YELLOW_A,
        #     radius=0.16
        # ).move_to(B.get_edge_center(RIGHT))
        # rope_tie_2 = Dot(
        #     color=YELLOW_A,
        #     radius=0.16
        # ).move_to(A.get_edge_center(RIGHT))

        # blockmid = (A.get_center() + B.get_center()) / 2
        # pulley = Circle(
        #     radius=0.77,
        #     stroke_width=10.0,
        #     color=BLUE_E,
        #     fill_color=BLUE_E_DARK,
        #     fill_opacity=1.0
        # ).shift(blockmid + 4*RIGHT)

        # pulley_mount_points = [
        #     pulley.get_center(),
        #     np.array([wall.get_center()[0], blockmid[1]+0.4, 0]),
        #     np.array([wall.get_center()[0], blockmid[1]-0.4, 0])
        # ]
        # pulley_mount = Polygon(
        #     *pulley_mount_points,
        #     color=GREY_BLUE,
        #     fill_color=GREY_BLUE_DARK,
        #     fill_opacity=1.0,
        #     stroke_width=5.0
        # )
        # pulley_axle = Circle(
        #     arc_center=pulley.get_center(),
        #     radius=0.2,
        #     stroke_width=8.0,
        #     color=BLUE_E,
        #     fill_color=BLUE_E_DARK,
        #     fill_opacity=1.0
        # )

        # rope_1 = Line(
        #     start=rope_tie_1.get_center(),
        #     end=pulley.get_edge_center(UP),
        #     color=YELLOW_E,
        #     stroke_width=5.0
        # )
        # rope_2 = Line(
        #     start=rope_tie_2.get_center(),
        #     end=pulley.get_edge_center(DOWN),
        #     color=YELLOW_E,
        #     stroke_width=5.0
        # )

        # pull_force = Arrow(
        #     color=RED,
        #     buff=0,
        #     start=ORIGIN,
        #     end=2*LEFT
        # ).next_to(A, LEFT, buff=0)
        # force_label = MathTex("P", color=pull_force.get_color()).scale(1.4).next_to(pull_force, LEFT)

        # diagram = Group(floor, wall, rope_1, rope_2, rope_tie_1, rope_tie_2, A, B, pulley, pulley_mount, pulley_axle, pull_force, force_label).move_to(ORIGIN)
        # self.add(diagram)
        # self.wait()
        # #endregion

        # #region Talk about pulleys
        # mask = Rectangle(height=10, width=14, fill_color=BLACK, fill_opacity=0.6, stroke_opacity=0)
        # self.play(Transform(diagram, diagram.copy().shift(1.5*UP)))
        # self.play(FadeIn(mask))
        # s_A_arrow = Arrow(
        #     color=GREEN,
        #     buff=0,
        #     start=rope_2.get_end(),
        #     end=rope_2.get_start()
        # ).shift(0.2*DOWN)
        # s_B_arrow = Arrow(
        #     color=GREEN,
        #     buff=0,
        #     start=rope_1.get_end(),
        #     end=rope_1.get_start()
        # ).shift(0.2*UP)
