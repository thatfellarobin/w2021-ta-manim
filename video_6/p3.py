from manim import *
import numpy as np

MED_DARK_GREY = '#666666'
GOLD_DARK = '#5c4326'
BLUE_E_DARK = '#0c343d'
GREEN_DARK = '#2b4022'

def pv(vector=np.array([0, 0, 0]), return_third_dim=False):
    # project vector onto new basis
    x1 = np.array([-np.sin(PI/6), np.cos(PI/6), 0])
    x2 = np.array([-np.cos(PI/6), -np.sin(PI/6), 2])
    x1 = x1 / np.linalg.norm(x1)
    x2 = x2 / np.linalg.norm(x2)
    x3 = np.cross(x1, x2)
    A = np.column_stack((np.transpose(x1), np.transpose(x2), np.transpose(x3)))

    A_inv = np.linalg.inv(A)
    projected = np.matmul(A_inv, vector)
    if return_third_dim:
        return projected
    else:
        return np.array([projected[0], projected[1], 0])


class T6P3(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        x_axis = Line(
            start=pv(np.array([-1.5, 0, 0])),
            end=pv(np.array([2.75, 0, 0])),
            color=BLUE
        )
        x_label = MathTex('x', color=BLUE).scale(0.8).next_to(x_axis.get_end(), x_axis.get_unit_vector(), buff=0.15)
        y_axis = Line(
            start=ORIGIN,
            end=pv(np.array([0, 5.5, 0])),
            color=BLUE
        )
        y_label = MathTex('y', color=BLUE).scale(0.8).next_to(y_axis.get_end(), y_axis.get_unit_vector(), buff=0.15)
        z_axis = Line(
            start=ORIGIN,
            end=pv(np.array([0, 0, 2])),
            color=BLUE
        )
        z_label = MathTex('z', color=BLUE).scale(0.8).next_to(z_axis.get_end(), z_axis.get_unit_vector(), buff=0.15)
        origin_dot = SmallDot(
            point=ORIGIN,
            color=BLUE
        )
        axes_group = Group(
            x_axis,
            x_label,
            y_axis,
            y_label,
            z_axis,
            z_label
        )

        dim_5 = Line(
            start=pv(np.array([2, 0, 0])),
            end=pv(np.array([2, 5, 0])),
            color=YELLOW_B
        )
        dim_5_label = MathTex('5b', color=YELLOW_B).scale(0.5).next_to(dim_5.get_center(), DOWN, buff=0.15)
        dim_2 = Line(
            start=pv(np.array([0, 5, 0])),
            end=pv(np.array([2, 5, 0])),
            color=YELLOW_B
        )
        dim_2_label = MathTex('2b', color=YELLOW_B).scale(0.5).next_to(dim_2.get_center(), RIGHT, buff=0.15).shift(0.1*DOWN)
        dim_3 = Line(
            start=pv(np.array([2, 5, 0])),
            end=pv(np.array([2, 5, 3])),
            color=YELLOW_B
        )
        dim_3_label = MathTex('3b', color=YELLOW_B).scale(0.5).next_to(dim_3.get_center(), RIGHT, buff=0.15)
        dim_1 = Line(
            start=pv(np.array([0, 2.5, 0])),
            end=pv(np.array([-1, 2.5, 0])),
            color=YELLOW_B
        )
        dim_1_label = MathTex('b', color=YELLOW_B).scale(0.5).next_to(dim_1.get_center(), RIGHT, buff=0.1).shift(0.1*DOWN)
        dim_2_5 = Line(
            start=pv(np.array([-1, 0, 0])),
            end=pv(np.array([-1, 2.5, 0])),
            color=YELLOW_B
        )
        dim_2_5_label = MathTex('2.5b', color=YELLOW_B).scale(0.5).next_to(dim_2_5.get_center(), DOWN, buff=0.14).shift(0.05*LEFT)
        dim_1_5 = Line(
            start=pv(np.array([-1, 2.5, 0])),
            end=pv(np.array([-1, 2.5, 1.5])),
            color=YELLOW_B
        )
        dim_1_5_label = MathTex('1.5b', color=YELLOW_B).scale(0.5).next_to(dim_1_5.get_center(), LEFT, buff=0.125).shift(0.1*DOWN)
        dim_group = Group(
            dim_5,
            dim_5_label,
            dim_2,
            dim_2_label,
            dim_3,
            dim_3_label,
            dim_1,
            dim_1_label,
            dim_2_5,
            dim_2_5_label,
            dim_1_5,
            dim_1_5_label
        )



        ball_1 = Dot(
            point=pv(np.array([2, 0, 0])),
            color=MAROON,
            radius=0.2
        )
        ball_1_label = Tex('\\textbf{m}').scale(0.5).move_to(ball_1.get_center())
        ball_2 = Dot(
            point=pv(np.array([-1, 2.5, 1.5])),
            color=MAROON,
            radius=0.22
        )
        ball_2_label = Tex('\\textbf{3m}').scale(0.5).move_to(ball_2.get_center())
        ball_3 = Dot(
            point=pv(np.array([2, 5, 3])),
            color=MAROON,
            radius=0.25
        )
        ball_3_label = Tex('\\textbf{5m}').scale(0.5).move_to(ball_3.get_center())
        ball_group = Group(
            ball_1,
            ball_1_label,
            ball_2,
            ball_2_label,
            ball_3,
            ball_3_label
        )

        v1 = Arrow(
            start=ball_1.get_center(),
            end=pv(np.array([2-2.25*np.cos(PI/3)*np.sin(PI/6), 2.25*np.cos(PI/3)*np.cos(PI/6), 2.25*np.sin(PI/3)])),
            color=GREEN,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        v1_label = MathTex('4v', color=GREEN).scale(0.5).next_to(v1.get_end(), RIGHT, buff=0.1)
        v1_xy_refline = Line(
            start=ball_1.get_center(),
            end=pv(np.array([2-3*np.cos(PI/3)*np.sin(PI/6), 3*np.cos(PI/3)*np.cos(PI/6), 0])),
            color=YELLOW_B
        )
        v1_z_refline = Line(
            start=v1.get_end(),
            end=pv(np.array([2-2.25*np.cos(PI/3)*np.sin(PI/6), 2.25*np.cos(PI/3)*np.cos(PI/6), 0])),
            color=YELLOW_B
        )
        v1_xy_angleref = Arc(
            radius=1.4,
            arc_center=ball_1.get_center(),
            start_angle=-0.25,
            angle=0.25,
            color=YELLOW
        ).add_tip(tip_length=0.15)
        v1_xy_angleref_label = MathTex('30^\\circ', color=YELLOW).scale(0.5).next_to(v1_xy_angleref, RIGHT, buff=0.1)
        v1_z_angleref = Arc(
            radius=0.7,
            arc_center=ball_1.get_center(),
            start_angle=0,
            angle=1,
            color=YELLOW
        ).add_tip(tip_length=0.15)
        v1_z_angleref_label = MathTex('60^\\circ', color=YELLOW).scale(0.5).next_to(v1_z_angleref, RIGHT, buff=0.1).shift(0.1*UP+0.05*LEFT)
        v2 = Arrow(
            start=ball_2.get_center(),
            end=pv(np.array([-1+1.5, 2.5, 1.5])),
            color=GREEN,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        v2_label = MathTex('2v', color=GREEN).scale(0.5).next_to(v2.get_end(), LEFT, buff=0.1)
        v3 = Arrow(
            start=ball_3.get_center(),
            end=pv(np.array([2, 5+1.5, 3])),
            color=GREEN,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        v3_label = MathTex('v', color=GREEN).scale(0.5).next_to(v3.get_end(), v3.get_unit_vector(), buff=0.1)
        f2 = Arrow(
            start=ball_2.get_center(),
            end=pv(np.array([-1, 2.5-1.5, 1.5])),
            color=RED,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        f2_label = MathTex('3F', color=RED).scale(0.5).next_to(f2.get_end(), f2.get_unit_vector(), buff=0.1)
        f3 = Arrow(
            start=ball_3.get_center(),
            end=pv(np.array([2, 5, 3+1.5])),
            color=RED,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        f3_label = MathTex('2F', color=RED).scale(0.5).next_to(f3.get_end(), f3.get_unit_vector(), buff=0.1)

        v_group = Group(
            v1_xy_refline,
            v1_z_refline,
            v1_xy_angleref,
            v1_xy_angleref_label,
            v1_z_angleref,
            v1_z_angleref_label,
            v1,
            v1_label,
            v2,
            v2_label,
            v3,
            v3_label,
            f2,
            f2_label,
            f3,
            f3_label
        )

        total_diagram = Group(axes_group, dim_group, v_group, ball_group)
        global_shift = -total_diagram.get_center()
        total_diagram.shift(global_shift)
        self.add(total_diagram)
        self.wait()





if __name__ == '__main__':
    # For testing
    test = np.array([1, 0, 0])
    print(pv(test))