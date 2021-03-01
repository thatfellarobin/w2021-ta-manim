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

        #region Coordinates
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
        #endregion

        #region Unit vectors
        i_axis = Arrow(
            start=ORIGIN,
            end=pv(np.array([1, 0, 0])),
            color=BLUE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        i_label = MathTex('\\hat{i}', color=BLUE).scale(0.8).next_to(i_axis.get_end(), i_axis.get_unit_vector(), buff=0.15)
        j_axis = Arrow(
            start=ORIGIN,
            end=pv(np.array([0, 1, 0])),
            color=BLUE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        j_label = MathTex('\\hat{j}', color=BLUE).scale(0.8).next_to(j_axis.get_end(), j_axis.get_unit_vector(), buff=0.15)
        k_axis = Arrow(
            start=ORIGIN,
            end=pv(np.array([0, 0, 1])),
            color=BLUE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        k_label = MathTex('\\hat{k}', color=BLUE).scale(0.8).next_to(k_axis.get_end(), k_axis.get_unit_vector(), buff=0.15)
        origin_dot_unit = origin_dot.copy()
        unitvect_group = Group(
            i_axis,
            i_label,
            j_axis,
            j_label,
            k_axis,
            k_label,
            origin_dot_unit
        ).move_to(3.75*LEFT+1.5*UP)
        #endregion

        #region Dimensions
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
        #endregion

        #region Particle masses
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
        #endregion

        #region Vectors and vector annotations
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
        v1_label = MathTex('4v', color=GREEN).scale(0.5).next_to(v1.get_end(), v1.get_unit_vector(), buff=0.1)
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
        #endregion

        total_diagram = Group(axes_group, dim_group, v_group, ball_group)
        global_shift = -total_diagram.get_center()
        total_diagram.shift(global_shift)
        self.add(total_diagram)
        self.wait()
        self.play(FadeIn(unitvect_group))
        self.wait()
        self.play(
            Transform(total_diagram, total_diagram.copy().to_corner(DOWN+LEFT)),
            Transform(unitvect_group, unitvect_group.copy().to_corner(UP+LEFT))
        )
        global_shift = global_shift + total_diagram.get_center()
        self.wait()

        #region math
        r_bar = MathTex(
            '\\bar{r}',
            '=',
            '\\frac{\\Sigma m_ir_i}{\\Sigma m_i}',
            '=',
            '\\frac{m(2b\\hat{i}) + 3m(-b\\hat{i} + 2.5b\\hat{j} + 1.5b\\hat{k}) + 5m(2b\\hat{i} + 5b\\hat{j} + 3b\\hat{k})}{m+3m+5m}'
        ).scale(0.6).to_corner(UP+RIGHT)
        r_bar_ans = MathTex(
            '\\bar{r} = b\\hat{i}+3.61b\\hat{j}+2.17b\\hat{k}'
        ).scale(0.6).next_to(r_bar, DOWN, aligned_edge=LEFT)
        r_bar_ansbox = SurroundingRectangle(r_bar_ans, buff=0.15)
        r_bar_ansgroup = Group(r_bar_ans, r_bar_ansbox)
        self.play(Write(r_bar[:3]))
        self.wait()
        self.play(Write(r_bar[3:]))
        self.wait()
        self.play(Write(r_bar_ans))
        self.play(ShowCreation(r_bar_ansbox))
        self.wait()
        self.play(
            FadeOut(r_bar),
            Transform(r_bar_ansgroup, r_bar_ansgroup.copy().next_to(total_diagram, RIGHT, aligned_edge=UP))
        )
        self.wait()

        r_bar_dot = MathTex(
            '\\dot{\\bar{r}}',
            '=',
            '\\frac{\\Sigma m_i\\dot{r_i}}{\\Sigma m_i}',
            '=',
            '\\frac{m(4v(-\\cos 60^\\circ\\sin 30^\\circ\\hat{i} + \\cos 60^\\circ\\cos 30^\\circ\\hat{j} + \\sin 60^\\circ\\hat{k})) + 3m(2v\\hat{i}) + 5m(v\\hat{j}) }{ m+3m+5m }'
        ).scale(0.6).to_corner(UP+RIGHT)
        r_bar_dot_ans = MathTex(
            '\\dot{\\bar{r}} = 0.556v\\hat{i} + 0.748v\\hat{j} + 0.385v\\hat{k}'
        ).scale(0.6).next_to(r_bar_dot, DOWN, aligned_edge=LEFT)
        r_bar_dot_ansbox = SurroundingRectangle(r_bar_dot_ans, buff=0.15)
        r_bar_dot_ansgroup = Group(r_bar_dot_ans, r_bar_dot_ansbox)
        self.play(Write(r_bar_dot[:3]))
        self.wait()
        self.play(Write(r_bar_dot[3:]))
        self.wait()
        self.play(Write(r_bar_dot_ans))
        self.play(ShowCreation(r_bar_dot_ansbox))
        self.wait()
        self.play(
            FadeOut(r_bar_dot),
            Transform(r_bar_dot_ansgroup, r_bar_dot_ansgroup.copy().next_to(r_bar_ansgroup, DOWN, buff=0.1, aligned_edge=LEFT))
        )
        self.wait()

        r_bar_ddot = MathTex(
            '\\ddot{\\bar{r}}',
            '=',
            '\\frac{\\Sigma \\vec{F}}{\\Sigma m_i}',
            '=',
            '\\frac{ -3F\\hat{j} + 2F\\hat{k} }{ m+3m+5m }'
        ).scale(0.6).to_corner(UP+RIGHT)
        r_bar_ddot_ans = MathTex(
            '\\ddot{\\bar{r}} = -0.333\\frac{F}{m}\\hat{j} + 0.222\\frac{F}{m}\\hat{k}'
        ).scale(0.6).next_to(r_bar_ddot, DOWN, aligned_edge=LEFT)
        r_bar_ddot_ansbox = SurroundingRectangle(r_bar_ddot_ans, buff=0.15)
        r_bar_ddot_ansgroup = Group(r_bar_ddot_ans, r_bar_ddot_ansbox)
        self.play(Write(r_bar_ddot[:3]))
        self.wait()
        self.play(Write(r_bar_ddot[3:]))
        self.wait()
        self.play(Write(r_bar_ddot_ans))
        self.play(ShowCreation(r_bar_ddot_ansbox))
        self.wait()
        self.play(
            FadeOut(r_bar_ddot),
            Transform(r_bar_ddot_ansgroup, r_bar_ddot_ansgroup.copy().next_to(r_bar_dot_ansgroup, DOWN, buff=0.1, aligned_edge=LEFT))
        )
        self.wait()

        T = MathTex(
            'T',
            '=',
            '\\Sigma\\frac{1}{2}m_iv_i^2',
            '=',
            '\\frac{1}{2}(m(4v)^2 + 3m(2v)^2 + 5mv^2)'
        ).scale(0.6).to_corner(UP+RIGHT)
        T_ans = MathTex(
            'T = 16.5mv^2'
        ).scale(0.6).next_to(T, DOWN, aligned_edge=LEFT)
        T_ansbox = SurroundingRectangle(T_ans, buff=0.15)
        T_ansgroup = Group(T_ans, T_ansbox)
        self.play(Write(T[:3]))
        self.wait()
        self.play(Write(T[3:]))
        self.wait()
        self.play(Write(T_ans))
        self.play(ShowCreation(T_ansbox))
        self.wait()
        self.play(
            FadeOut(T),
            Transform(T_ansgroup, T_ansgroup.copy().next_to(r_bar_ddot_ansgroup, DOWN, buff=0.1, aligned_edge=LEFT))
        )
        self.wait()

        H_o = MathTex(
            'H_O',
            '=',
            '\\Sigma (r_i\\times m_iv_i)',
            '=',
            '2b\\hat{i}\\times m(4v(-\\cos 60^\\circ\\sin 30^\\circ\\hat{i} + \\cos 60^\\circ\\cos 30^\\circ\\hat{j} + \\sin 60^\\circ\\hat{k}))',
            '+',
            '(-b\\hat{i} + 2.5b\\hat{j} + 1.5b\\hat{k})\\times 3m(2v\\hat{i})',
            '+',
            '(2b\\hat{i} + 5b\\hat{j} + 3b\\hat{k})\\times m(v\\hat{j})'
        ).scale(0.6).to_corner(UP+RIGHT)
        H_o[3:].next_to(H_o[1], DOWN, buff=0.2, aligned_edge=LEFT)
        H_o[5:].next_to(H_o[4], DOWN, buff=0.2, aligned_edge=LEFT)
        H_o[7:].next_to(H_o[5], DOWN, buff=0.2, aligned_edge=LEFT)
        H_o.to_corner(UP+RIGHT)
        H_o_ans = MathTex(
            'H_O = -15mvb\\hat{i} + 2.07mvb\\hat{j} - 1.536mvb\\hat{k}'
        ).scale(0.6).next_to(H_o, DOWN, aligned_edge=LEFT)
        H_o_ansbox = SurroundingRectangle(H_o_ans, buff=0.15)
        H_o_ansgroup = Group(H_o_ans, H_o_ansbox)
        self.play(Write(H_o[:3]))
        self.wait()
        self.play(Write(H_o[3:5]))
        self.wait()
        self.play(Write(H_o[5:7]))
        self.wait()
        self.play(Write(H_o[7:]))
        self.wait()
        self.play(Write(H_o_ans))
        self.play(ShowCreation(H_o_ansbox))
        self.wait()
        self.play(
            FadeOut(H_o),
            Transform(H_o_ansgroup, H_o_ansgroup.copy().next_to(T_ansgroup, DOWN, buff=0.1, aligned_edge=LEFT))
        )
        self.wait()

        H_dot_o = MathTex(
            '\\dot{H}_O',
            '=',
            '\\Sigma M_O = \\Sigma (r\\times \\vec{F})',
            '=',
            '(-b\\hat{i} + 2.5b\\hat{j} + 1.5b\\hat{k})\\times -3F\\hat{j}',
            '+',
            '(2b\\hat{i} + 5b\\hat{j} + 3b\\hat{k})\\times 2F\\hat{k}'
        ).scale(0.6).to_corner(UP+RIGHT)
        H_dot_o[3:].next_to(H_dot_o[1], DOWN, buff=0.2, aligned_edge=LEFT)
        H_dot_o[5:].next_to(H_dot_o[4], DOWN, buff=0.2, aligned_edge=LEFT)
        H_dot_o.to_corner(UP+RIGHT)
        H_dot_o_ans = MathTex(
            '\\dot{H}_O = 14.5Fb\\hat{i} - 4Fb\\hat{j} + 3Fb\\hat{k}'
        ).scale(0.6).next_to(H_dot_o, DOWN, aligned_edge=LEFT)
        H_dot_o_ansbox = SurroundingRectangle(H_dot_o_ans, buff=0.15)
        H_dot_o_ansgroup = Group(H_dot_o_ans, H_dot_o_ansbox)
        self.play(Write(H_dot_o[:3]))
        self.wait()
        self.play(Write(H_dot_o[3:5]))
        self.wait()
        self.play(Write(H_dot_o[5:]))
        self.wait()
        self.play(Write(H_dot_o_ans))
        self.play(ShowCreation(H_dot_o_ansbox))
        self.wait()
        self.play(
            FadeOut(H_dot_o),
            Transform(H_dot_o_ansgroup, H_dot_o_ansgroup.copy().next_to(H_o_ansgroup, DOWN, buff=0.1, aligned_edge=LEFT))
        )
        self.wait()


if __name__ == '__main__':
    # For testing
    test = np.array([1, 0, 0])
    print(pv(test))