from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

DSCALE = 0.5/50

class T7P3(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Diagram objects
        # Link ADB
        adb = Line(
            start=DSCALE*300*((3/5)*DOWN + (4/5)*RIGHT),
            end=DSCALE*250*((3/5)*UP + (4/5)*LEFT),
            color=BLUE,
            stroke_width=15
        )
        point_a_adb = Dot(
            point=adb.get_start(),
            radius=0.15,
            color=BLUE_E
        )
        point_d_adb = Dot(
            point=ORIGIN,
            radius=0.15,
            color=BLUE_E
        )
        point_b_adb = Dot(
            point=adb.get_end(),
            radius=0.15,
            color=BLUE_E
        )
        link_adb = Group(adb, point_a_adb, point_d_adb, point_b_adb)

        # Link CDE
        cde = Line(
            start=DSCALE*400*np.array([-np.cos(PI/6), -np.sin(PI/6), 0]),
            end=DSCALE*300*np.array([np.cos(PI/6), np.sin(PI/6), 0]),
            color=RED_B,
            stroke_width=15
        )
        point_c_cde = Dot(
            point=cde.get_start(),
            radius=0.15,
            color=RED_E
        )
        point_d_cde = Dot(
            point=ORIGIN,
            radius=0.15,
            color=RED_E
        )
        point_e_cde = Dot(
            point=cde.get_end(),
            radius=0.15,
            color=RED_E
        )
        link_cde = Group(cde, point_c_cde, point_d_cde, point_e_cde)
        #endregion

        diagram = Group(link_adb, link_cde).move_to(ORIGIN)
        self.add(diagram)
        self.wait()

        # Separate the elements
        self.play(
            Transform(link_adb, link_adb.copy().scale(0.6).to_corner(UP+RIGHT, buff=1).shift(0.5*LEFT)),
            Transform(link_cde, link_cde.copy().scale(0.6).to_corner(DOWN+RIGHT, buff=1).shift(0.5*LEFT))
        )
        self.wait()

        # label points
        A_label1 = MathTex('A').scale(0.6).next_to(point_a_adb, RIGHT, buff=0.15)
        B_label1 = MathTex('B').scale(0.6).next_to(point_b_adb, LEFT, buff=0.15)
        C_label1 = MathTex('C').scale(0.6).next_to(point_c_cde, DOWN, buff=0.15)
        D_label1 = MathTex('D').scale(0.6).next_to(point_d_adb, DOWN+LEFT, buff=0.15)
        D_label2 = D_label1.copy().next_to(point_d_cde, UP+LEFT, buff=0.15)
        E_label1 = MathTex('E').scale(0.6).next_to(point_e_cde, RIGHT, buff=0.15)
        self.play(
            Write(A_label1),
            Write(B_label1),
            Write(C_label1),
            Write(D_label1),
            Write(D_label2),
            Write(E_label1),
        )
        self.wait()

        # label other stuff
        length_ad = MathTex('300\\,\\mathrm{mm}', color=YELLOW).scale(0.5).next_to((point_a_adb.get_center() + point_d_adb.get_center())/2, LEFT+DOWN, buff=0.1)
        length_db = MathTex('250\\,\\mathrm{mm}', color=YELLOW).scale(0.5).next_to((point_d_adb.get_center() + point_b_adb.get_center())/2, LEFT+DOWN, buff=0.1)
        length_cd = MathTex('400\\,\\mathrm{mm}', color=YELLOW).scale(0.5).next_to((point_c_cde.get_center() + point_d_cde.get_center())/2, LEFT+UP, buff=0.1)
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
        coordsys = Group(i_arrow, j_arrow, i_label, j_label).scale(0.75).to_corner(DOWN+RIGHT, buff=0.75)
        self.play(
            Write(length_ad),
            Write(length_db),
            Write(length_cd),
            Write(i_arrow),
            Write(j_arrow),
            Write(i_label),
            Write(j_label),
        )
        self.wait()

        # Label velocity assumptions.
        v_b_arrow = Arrow(
            start=point_b_adb.get_center(),
            end=point_b_adb.get_center()+RIGHT,
            color=PURPLE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        v_b_label = MathTex('\\vec{v}_B').scale(0.6).next_to(v_b_arrow, RIGHT, buff=0.15)
        v_c_arrow = Arrow(
            start=point_c_cde.get_center(),
            end=point_c_cde.get_center()+LEFT,
            color=PURPLE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        v_c_label = MathTex('\\vec{v}_C').scale(0.6).next_to(v_c_arrow, LEFT, buff=0.15)
        omega_adb_arrow = Arc(
            radius=0.25,
            arc_center=link_adb.get_center()+RIGHT,
            start_angle=-3*PI/4,
            angle=-1.5*PI,
            color=PURPLE
        ).add_tip(tip_length=0.15)
        omega_adb_annot = MathTex('\\omega_{ADB}', color=PURPLE).scale(0.6).next_to(omega_adb_arrow, UP, buff=0.15)
        omega_cde_arrow = Arc(
            radius=0.25,
            arc_center=link_cde.get_center()+DOWN,
            start_angle=-3*PI/4,
            angle=-1.5*PI,
            color=PURPLE
        ).add_tip(tip_length=0.15)
        omega_cde_annot = MathTex('\\omega_{CDE}', color=PURPLE).scale(0.6).next_to(omega_cde_arrow, DOWN, buff=0.15)
        self.play(
            Write(v_b_arrow),
            Write(v_b_label),
            Write(v_c_arrow),
            Write(v_c_label),
            Write(omega_adb_arrow),
            Write(omega_adb_annot),
            Write(omega_cde_arrow),
            Write(omega_cde_annot)
        )
        self.wait()

        #region Math it out

        title_link_adb = Tex('Link ADB:', color=YELLOW).scale(0.5).to_corner(UP+LEFT)
        #region Link ab
        eq_ab = MathTex(
            '\\vec{v}_B = \\vec{v}_A + \\vec{v}_{B/A}'
        ).scale(0.55).next_to(title_link_adb, DOWN, aligned_edge=LEFT)
        eq_ab_sub = MathTex(
            '|\\vec{v}_B|\\hat{i}',
            '=',
            '-4\\hat{j} + \\vec{\\omega}_{ADB}\\times\\vec{r}_{B/A}',
            '=',
            '-4\\hat{j} + -|\\vec{\\omega}_{ADB}|\\hat{k} \\times \\left(-0.55\\left(\\frac{4}{5}\\right)\\hat{i} + 0.55\\left(\\frac{3}{5}\\right)\\hat{j}\\right)',
            '=',
            '0.33|\\vec{\\omega}_{ADB}|\\hat{i} + (0.44|\\vec{\\omega}_{ADB}| - 4)\\hat{j}',
        ).scale(0.55).next_to(eq_ab, DOWN, buff=0.2, aligned_edge=LEFT)
        eq_ab_sub[3:].next_to(eq_ab_sub[1:3], DOWN, aligned_edge=LEFT, buff=0.15)
        eq_ab_sub[5:].next_to(eq_ab_sub[3:5], DOWN, aligned_edge=LEFT, buff=0.15)
        eq_ab_dir_i = MathTex(
            '\\hat{i}:',
            '|\\vec{v}_B|',
            '=',
            '0.33|\\vec{\\omega}_{ADB}|'
        ).scale(0.55).next_to(eq_ab_sub, DOWN, aligned_edge=LEFT, buff=0.2).shift(0.5*RIGHT)
        eq_ab_dir_i[0].set_color(YELLOW)
        eq_ab_dir_j = MathTex(
            '\\hat{j}:',
            '0',
            '=',
            '0.44|\\vec{\\omega}_{ADB}| - 4',
        ).scale(0.55).next_to(eq_ab_dir_i, DOWN, aligned_edge=LEFT, buff=0.2)
        eq_ab_dir_j[0].set_color(YELLOW)

        v_b_ans = MathTex('|\\vec{v}_B| = 3.00\\,\\mathrm{m/s}').scale(0.55).next_to(eq_ab_dir_j, DOWN, aligned_edge=LEFT)
        omega_ab_ans = MathTex('|\\vec{\\omega}_{ADB}|=9.091\\,\\mathrm{rad/s}').scale(0.55).next_to(v_b_ans, DOWN, aligned_edge=LEFT)
        ansgroup1 = Group(v_b_ans, omega_ab_ans)

        self.play(Write(title_link_adb))
        self.play(Write(eq_ab))
        self.wait()
        self.play(Write(eq_ab_sub[:3]))
        self.wait()
        self.play(Write(eq_ab_sub[3:5]))
        self.wait()
        self.play(Write(eq_ab_sub[5:]))
        self.wait()
        self.play(
            Write(eq_ab_dir_i),
            Write(eq_ab_dir_j)
        )
        self.wait()
        self.play(
            Write(v_b_ans),
            Write(omega_ab_ans)
        )
        self.wait()
        self.play(
            FadeOut(eq_ab),
            FadeOut(eq_ab_sub),
            FadeOut(eq_ab_dir_i),
            FadeOut(eq_ab_dir_j),
            Transform(ansgroup1, ansgroup1.copy().next_to(title_link_adb, DOWN, aligned_edge=LEFT, buff=0.15))
        )
        self.wait()
        #endregion

        #region link ad
        eq_ad = MathTex(
            '\\vec{v}_D = \\vec{v}_A + \\vec{v}_{D/A}'
        ).scale(0.55).next_to(ansgroup1, DOWN, aligned_edge=LEFT)
        eq_ad_sub = MathTex(
            '\\vec{v}_D',
            '=',
            '-4\\hat{j} + \\vec{\\omega}_{ADB}\\times\\vec{r}_{B/A}',
            '=',
            '-4\\hat{j} + -9.091\\hat{k} \\times \\left(-0.3\\left(\\frac{4}{5}\\right)\\hat{i} + 0.3\\left(\\frac{3}{5}\\right)\\hat{j}\\right)',
            '\\Rightarrow',
            '\\vec{v}_D = [1.636\\hat{i} - 1.818\\hat{j}]\\,\\mathrm{m/s}',
        ).scale(0.55).next_to(eq_ad, DOWN, buff=0.2, aligned_edge=LEFT)
        eq_ad_sub[3:].next_to(eq_ad_sub[1:3], DOWN, aligned_edge=LEFT, buff=0.15)
        eq_ad_sub[5:].next_to(eq_ad_sub[3:5], DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(Write(eq_ad))
        self.wait()
        self.play(Write(eq_ad_sub[:3]))
        self.wait()
        self.play(Write(eq_ad_sub[3:5]))
        self.wait()
        self.play(Write(eq_ad_sub[5:]))
        self.wait()
        self.play(
            FadeOut(eq_ad),
            FadeOut(eq_ad_sub[:-1]),
            Transform(eq_ad_sub[-1], eq_ad_sub[-1].copy().next_to(ansgroup1, DOWN, aligned_edge=LEFT))
        )
        self.wait()

        #endregion
