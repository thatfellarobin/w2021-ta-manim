from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

LINK_WIDTH = 0.25
DSCALE = 0.75/50

class T7P2(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Diagram objects

        # Link EB
        eb = Line(
            start=ORIGIN,
            end=50*DSCALE*UP,
            color=BLUE,
            stroke_width=15
        )
        point_e_eb = Dot(
            point=eb.get_start(),
            radius=0.15,
            color=BLUE_E
        )
        point_b_eb = Dot(
            point=eb.get_end(),
            radius=0.15,
            color=BLUE_E
        )
        link_eb = Group(eb, point_e_eb, point_b_eb)

        # Link ABC
        ab = Line(
            start=50*DSCALE*np.array([np.cos(3*PI/4), np.sin(3*PI/4), 0]),
            end=ORIGIN,
            color=RED,
            stroke_width=15
        )
        bc = Line(
            start=ab.get_end(),
            end=250*DSCALE*np.array([np.cos(PI/3), np.sin(PI/3), 0]),
            color=RED,
            stroke_width=15
        )
        point_a_abc = Dot(
            point=ab.get_start(),
            radius=0.15,
            color=RED_E
        )
        point_b_abc = Dot(
            point=ab.get_end(),
            radius=0.15,
            color=RED_E
        )
        point_c_abc = Dot(
            point=bc.get_end(),
            radius=0.15,
            color=RED_E
        )
        link_abc = Group(ab, bc, point_a_abc, point_b_abc, point_c_abc)
        link_abc.shift(point_b_eb.get_center()-point_b_abc.get_center())

        # Link AD
        ad = Line(
            start=ORIGIN,
            end=250*DSCALE*np.array([np.cos(3*PI/4), np.sin(3*PI/4), 0]),
            color=BLUE,
            stroke_width=15
        )
        point_a_ad = Dot(
            point=ad.get_start(),
            radius=0.15,
            color=BLUE_E
        )
        point_d_ad = Dot(
            point=ad.get_end(),
            radius=0.15,
            color=BLUE_E
        )
        link_ad = Group(ad, point_a_ad, point_d_ad)
        link_ad.shift(point_a_abc.get_center()-point_a_ad.get_center())
        #endregion

        diagram = Group(link_ad, link_abc, link_eb).move_to(ORIGIN)
        self.add(diagram)
        self.wait()

        # Separate the elements
        self.play(
            Transform(link_eb, link_eb.copy().scale(0.6).to_corner(UP+RIGHT, buff=0.75)),
            Transform(link_abc, link_abc.copy().scale(0.6).to_edge(RIGHT, buff=0.75).shift(0.25*UP)),
            Transform(link_ad, link_ad.copy().scale(0.6).to_corner(DOWN+RIGHT, buff=0.75))
        )
        self.wait()

        # label points
        A_label1 = MathTex('A').scale(0.8).next_to(point_a_ad, RIGHT, buff=0.15)
        A_label2 = A_label1.copy().next_to(point_a_abc, LEFT, buff=0.15)
        B_label1 = MathTex('B').scale(0.8).next_to(point_b_eb, RIGHT, buff=0.15)
        B_label2 = B_label1.copy().next_to(point_b_abc, DOWN, buff=0.15)
        C_label1 = MathTex('C').scale(0.8).next_to(point_c_abc, RIGHT, buff=0.15)
        D_label1 = MathTex('D').scale(0.8).next_to(point_d_ad, LEFT, buff=0.15)
        E_label1 = MathTex('E').scale(0.8).next_to(point_e_eb, RIGHT, buff=0.15)
        self.play(
            Write(A_label1),
            Write(A_label2),
            Write(B_label1),
            Write(B_label2),
            Write(C_label1),
            Write(D_label1),
            Write(E_label1),
        )
        self.wait()

        # label other stuff
        length_eb = MathTex('50\\,\\mathrm{mm}', color=YELLOW).scale(0.5).next_to(eb.get_center(), LEFT, buff=0.1)
        length_ab = MathTex('50\\,\\mathrm{mm}', color=YELLOW).scale(0.5).next_to(ab.get_center(), LEFT+DOWN, buff=0.1)
        length_bc = MathTex('250\\,\\mathrm{mm}', color=YELLOW).scale(0.5).next_to(bc.get_center(), RIGHT+DOWN, buff=0.1)
        length_ad = MathTex('250\\,\\mathrm{mm}', color=YELLOW).scale(0.5).next_to(ad.get_center(), LEFT+DOWN, buff=0.1)
        self.play(
            Write(length_eb),
            Write(length_ab),
            Write(length_bc),
            Write(length_ad),
        )
        self.wait()
        # TODO: Add assumed velocities


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
        coordsys = Group(i_arrow, j_arrow, i_label, j_label).next_to(link_ad, LEFT, buff=0, aligned_edge=DOWN)
        self.play(
            Write(i_arrow),
            Write(j_arrow),
            Write(i_label),
            Write(j_label),
        )
        self.wait()


        #region Math


        #region Link EB
        title_link_eb = Tex('Link EB:', color=YELLOW).scale(0.5).to_corner(UP+LEFT)
        eq_eb = MathTex(
            '\\vec{v}_B = \\vec{v}_E + \\vec{v}_{B/E}',
            '= 0 + \\omega_{EB}\\times\\vec{r}_{EB}',
            '= 30\\hat{k} \\times 0.05\\hat{j}',
            '\\Rightarrow',
            '\\vec{v}_B = -1.5\\hat{i}\\,\\mathrm{m/s}'
        ).scale(0.55).next_to(title_link_eb, DOWN, aligned_edge=LEFT)
        self.play(Write(title_link_eb))
        self.play(Write(eq_eb[0]))
        self.wait()
        self.play(Write(eq_eb[1]))
        self.wait()
        self.play(Write(eq_eb[2]))
        self.wait()
        self.play(Write(eq_eb[3:]))
        self.wait()
        self.play(
            FadeOut(eq_eb[:-1]),
            Transform(eq_eb[-1], eq_eb[-1].copy().next_to(title_link_eb, DOWN, aligned_edge=LEFT, buff=0.15))
        )
        self.wait()
        #endregion

        #region Link ABC
        title_link_abc = Tex('Link ABC:', color=YELLOW).scale(0.5).next_to(eq_eb, DOWN, aligned_edge=LEFT)
        eq_bc = MathTex(
            '\\vec{v}_C = \\vec{v}_B + \\vec{v}_{C/B}'
        ).scale(0.55).next_to(title_link_abc, DOWN, aligned_edge=LEFT)
        eq_bc_sub = MathTex(
            '|v_C|\\cos(45^\\circ)\\hat{i} + |v_C|\\sin(45^\\circ)\\hat{j}',
            '=',
            '-1.5\\hat{i} + \\omega_{ABC}\\times\\vec{r}_{BC}',
            '=',
            '-1.5\\hat{i} + |\\omega_{ABC}|\\hat{k} \\times (0.25\\cos(60^\\circ)\\hat{i} + 0.25\\sin(60^\\circ)\\hat{j})',
            '=',
            '-1.5\\hat{i} - |\\omega_{ABC}|(0.25\\sin(60^\\circ))\\hat{i} + |\\omega_{ABC}|(0.25\\cos(60^\\circ))\\hat{j}',
        ).scale(0.55).next_to(eq_bc, DOWN, buff=0.2, aligned_edge=LEFT)
        eq_bc_sub[3:].next_to(eq_bc_sub[1:3], DOWN, aligned_edge=LEFT, buff=0.15)
        eq_bc_sub[5:].next_to(eq_bc_sub[3:5], DOWN, aligned_edge=LEFT, buff=0.15)
        eq_bc_dir_i = MathTex(
            '\\hat{i}:',
            '|v_C|\\cos(45^\\circ)',
            '=',
            '-1.5 - |\\omega_{ABC}|(0.25\\sin(60^\\circ))'
        ).scale(0.55).next_to(eq_bc_sub, DOWN, aligned_edge=LEFT, buff=0.2).shift(0.5*RIGHT)
        eq_bc_dir_i[0].set_color(YELLOW)
        eq_bc_dir_j = MathTex(
            '\\hat{j}:',
            '|v_C|\\sin(45^\\circ)',
            '=',
            '|\\omega_{ABC}|(0.25\\cos(60^\\circ))',
        ).scale(0.55).next_to(eq_bc_dir_i, DOWN, aligned_edge=LEFT, buff=0.2)
        eq_bc_dir_j[0].set_color(YELLOW)

        v_c_ans = MathTex('|v_C|=-0.776\\,\\mathrm{m/s}').scale(0.55).next_to(eq_bc_dir_j, DOWN, aligned_edge=LEFT)
        omega_abc_ans = MathTex('|\\omega_{ABC}|=-4.39\\,\\mathrm{rad/s}').scale(0.55).next_to(v_c_ans, DOWN, aligned_edge=LEFT)
        ansbox1 = SurroundingRectangle(v_c_ans)
        ansgroup1 = Group(v_c_ans, ansbox1, omega_abc_ans)

        self.play(Write(title_link_abc))
        self.play(Write(eq_bc))
        self.wait()
        self.play(Write(eq_bc_sub[:3]))
        self.wait()
        self.play(Write(eq_bc_sub[3:5]))
        self.wait()
        self.play(Write(eq_bc_sub[5:]))
        self.wait()
        self.play(
            Write(eq_bc_dir_i),
            Write(eq_bc_dir_j)
        )
        self.wait()
        self.play(
            Write(v_c_ans),
            Write(omega_abc_ans)
        )
        self.play(ShowCreation(ansbox1))
        self.wait()
        self.play(
            FadeOut(eq_bc),
            FadeOut(eq_bc_sub),
            FadeOut(eq_bc_dir_i),
            FadeOut(eq_bc_dir_j),
            Transform(ansgroup1, ansgroup1.copy().next_to(title_link_abc, DOWN, aligned_edge=LEFT, buff=0.15))
        )
        self.wait()

        eq_ba = MathTex(
            '\\vec{v}_A = \\vec{v}_B + \\vec{v}_{A/B}'
        ).scale(0.55).next_to(ansgroup1, DOWN, aligned_edge=LEFT)
        eq_ba_sub = MathTex(
            '\\vec{v}_A',
            '=',
            '-1.5\\hat{i} + \\omega_{ABC}\\times\\vec{r}_{BA}',
            '=',
            '-1.5\\hat{i} + (-4.39\\hat{k}) \\times (-0.05\\cos(45^\\circ)\\hat{i} + 0.05\\sin(45^\\circ)\\hat{j})',
            '\\Rightarrow',
            '\\vec{v}_A = -1.345\\hat{i} + 0.1552\\hat{j}',
        ).scale(0.55).next_to(eq_ba, DOWN, buff=0.2, aligned_edge=LEFT)
        eq_ba_sub[3:].next_to(eq_ba_sub[1:3], DOWN, aligned_edge=LEFT, buff=0.15)
        eq_ba_sub[5:].next_to(eq_ba_sub[3:5], DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(Write(eq_ba))
        self.wait()
        self.play(Write(eq_ba_sub[:3]))
        self.wait()
        self.play(Write(eq_ba_sub[3:5]))
        self.wait()
        self.play(Write(eq_ba_sub[5:]))
        self.wait()
        self.play(
            FadeOut(eq_ba),
            FadeOut(eq_ba_sub[:-1]),
            Transform(eq_ba_sub[-1], eq_ba_sub[-1].copy().next_to(ansgroup1, DOWN, aligned_edge=LEFT, buff=0.15))
        )
        self.wait()
        #endregion


        #endregion
