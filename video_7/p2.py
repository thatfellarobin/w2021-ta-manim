from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

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
            Transform(link_eb, link_eb.copy().scale(0.6).to_corner(UP+RIGHT, buff=0.75).shift(0.5*LEFT)),
            Transform(link_abc, link_abc.copy().scale(0.6).to_edge(RIGHT, buff=0.75).shift(0.25*UP + 0.5*LEFT)),
            Transform(link_ad, link_ad.copy().scale(0.6).to_corner(DOWN+RIGHT, buff=0.75).shift(0.5*LEFT))
        )
        self.wait()

        # label points
        A_label1 = MathTex('A').scale(0.6).next_to(point_a_ad, RIGHT, buff=0.15)
        A_label2 = A_label1.copy().next_to(point_a_abc, LEFT, buff=0.15)
        B_label1 = MathTex('B').scale(0.6).next_to(point_b_eb, RIGHT, buff=0.15)
        B_label2 = B_label1.copy().next_to(point_b_abc, DOWN, buff=0.15)
        C_label1 = MathTex('C').scale(0.6).next_to(point_c_abc, RIGHT, buff=0.15)
        D_label1 = MathTex('D').scale(0.6).next_to(point_d_ad, LEFT, buff=0.15)
        E_label1 = MathTex('E').scale(0.6).next_to(point_e_eb, RIGHT, buff=0.15)
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
            radius=0.2,
            color=YELLOW
        )
        k_label = MathTex('\\hat{k}', color=YELLOW).scale(0.7).next_to(k_circle, LEFT, buff=0.15)
        coordsys = Group(i_arrow, j_arrow, i_label, j_label, k_dot, k_circle, k_label).next_to(link_ad, LEFT, buff=0, aligned_edge=DOWN)
        self.play(
            Write(i_arrow),
            Write(j_arrow),
            Write(i_label),
            Write(j_label),
            Write(k_dot),
            Write(k_circle),
            Write(k_label),
        )
        self.wait()


        #region Math

        #region Link EB
        title_link_eb = Tex('Link EB:', color=YELLOW).scale(0.5).to_corner(UP+LEFT)
        eq_eb = MathTex(
            '\\vec{v}_B = \\vec{v}_E + \\vec{v}_{B/E}',
            '= 0 + \\vec{\\omega}_{EB}\\times\\vec{r}_{B/E}',
            '= 30\\hat{k} \\times 0.05\\hat{j}',
            '\\Rightarrow',
            '\\vec{v}_B = -1.5\\hat{i}\\,\\mathrm{m/s}'
        ).scale(0.55).next_to(title_link_eb, DOWN, aligned_edge=LEFT)
        self.play(Write(title_link_eb))
        self.wait()
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

        # Draw arrows for assumed velocity and rotation
        v_c_arrow = Arrow(
            start=point_c_abc.get_center(),
            end=point_c_abc.get_center() + 0.5*np.array([np.cos(PI/4), np.sin(PI/4), 0]),
            color=PURPLE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        v_c_annot = MathTex('\\vec{v}_C', color=PURPLE).scale(0.6).next_to(v_c_arrow, np.array([np.cos(PI/4), np.sin(PI/4), 0]), buff=0.15)
        omega_abc_arrow = Arc(
            radius=0.25,
            arc_center=link_abc.get_center(),
            start_angle=-PI/4,
            angle=1.5*PI,
            color=PURPLE
        ).add_tip(tip_length=0.15)
        omega_abc_annot = MathTex('\\omega_{ABC}', color=PURPLE).scale(0.6).next_to(omega_abc_arrow, UP, buff=0.15)
        assume_text = Tex('Purple:', ' assumed value').scale(0.6).next_to(link_eb, LEFT, buff=2, aligned_edge=UP)
        assume_text[0].set_color(PURPLE)

        # Section BC
        eq_bc = MathTex(
            '\\vec{v}_C = \\vec{v}_B + \\vec{v}_{C/B}'
        ).scale(0.55).next_to(title_link_abc, DOWN, aligned_edge=LEFT)
        eq_bc_sub = MathTex(
            '|\\vec{v}_C|\\cos(45^\\circ)\\hat{i} + |\\vec{v}_C|\\sin(45^\\circ)\\hat{j}',
            '=',
            '-1.5\\hat{i} + \\vec{\\omega}_{ABC}\\times\\vec{r}_{C/B}',
            '=',
            '-1.5\\hat{i} + |\\vec{\\omega}_{ABC}|\\hat{k} \\times (0.25\\cos(60^\\circ)\\hat{i} + 0.25\\sin(60^\\circ)\\hat{j})',
            '=',
            '-1.5\\hat{i} - |\\vec{\\omega}_{ABC}|(0.25\\sin(60^\\circ))\\hat{i} + |\\vec{\\omega}_{ABC}|(0.25\\cos(60^\\circ))\\hat{j}',
        ).scale(0.55).next_to(eq_bc, DOWN, buff=0.2, aligned_edge=LEFT)
        eq_bc_sub[3:].next_to(eq_bc_sub[1:3], DOWN, aligned_edge=LEFT, buff=0.15)
        eq_bc_sub[5:].next_to(eq_bc_sub[3:5], DOWN, aligned_edge=LEFT, buff=0.15)
        eq_bc_dir_i = MathTex(
            '\\hat{i}:',
            '|\\vec{v}_C|\\cos(45^\\circ)',
            '=',
            '-1.5 - |\\vec{\\omega}_{ABC}|(0.25\\sin(60^\\circ))'
        ).scale(0.55).next_to(eq_bc_sub, DOWN, aligned_edge=LEFT, buff=0.2).shift(0.5*RIGHT)
        eq_bc_dir_i[0].set_color(YELLOW)
        eq_bc_dir_j = MathTex(
            '\\hat{j}:',
            '|\\vec{v}_C|\\sin(45^\\circ)',
            '=',
            '|\\vec{\\omega}_{ABC}|(0.25\\cos(60^\\circ))',
        ).scale(0.55).next_to(eq_bc_dir_i, DOWN, aligned_edge=LEFT, buff=0.2)
        eq_bc_dir_j[0].set_color(YELLOW)

        v_c_ans = MathTex('|\\vec{v}_C|=-0.776\\,\\mathrm{m/s}').scale(0.55).next_to(eq_bc_dir_j, DOWN, aligned_edge=LEFT)
        omega_abc_ans = MathTex('|\\vec{\\omega}_{ABC}|=-4.39\\,\\mathrm{rad/s}').scale(0.55).next_to(v_c_ans, DOWN, aligned_edge=LEFT)
        ansbox1 = SurroundingRectangle(v_c_ans)
        ansgroup1 = Group(v_c_ans, ansbox1, omega_abc_ans)

        self.play(Write(title_link_abc))
        self.wait()
        self.play(
            Write(assume_text),
            Write(v_c_arrow),
            Write(v_c_annot),
            Write(omega_abc_arrow),
            Write(omega_abc_annot)
        )
        self.wait()
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
            '-1.5\\hat{i} + \\vec{\\omega}_{ABC}\\times\\vec{r}_{A/B}',
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

        #region Link AD
        title_link_ad = Tex('Link AD:', color=YELLOW).scale(0.5).next_to(eq_ba_sub[-1], DOWN, aligned_edge=LEFT)

        # Draw arrows for assumed velocity and rotation
        v_d_arrow = Arrow(
            start=point_d_ad.get_center(),
            end=point_d_ad.get_center() + 0.5*np.array([-np.cos(PI/4), np.sin(PI/4), 0]),
            color=PURPLE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        v_d_annot = MathTex('\\vec{v}_D', color=PURPLE).scale(0.6).next_to(v_d_arrow, np.array([-np.cos(PI/4), np.sin(PI/4), 0]), buff=0.15)
        omega_ad_arrow = Arc(
            radius=0.25,
            arc_center=link_ad.get_center(),
            start_angle=-PI/4,
            angle=1.5*PI,
            color=PURPLE
        ).add_tip(tip_length=0.15)
        omega_ad_annot = MathTex('\\omega_{AD}', color=PURPLE).scale(0.6).next_to(omega_ad_arrow, UP, buff=0.15)
        self.play(
            Write(v_d_arrow),
            Write(v_d_annot),
            Write(omega_ad_arrow),
            Write(omega_ad_annot)
        )
        self.wait()

        eq_ad = MathTex(
            '\\vec{v}_D = \\vec{v}_A + \\vec{v}_{D/A}'
        ).scale(0.55).next_to(title_link_ad, DOWN, aligned_edge=LEFT)
        eq_ad_sub = MathTex(
            '-|\\vec{v}_D|\\cos(45^\\circ)\\hat{i} + |\\vec{v}_D|\\sin(45^\\circ)\\hat{j}',
            '=',
            '(-1.345\\hat{i} + 0.1552\\hat{j}) + \\vec{\\omega}_{AD}\\times\\vec{r}_{D/A}',
            '=',
            '(-1.345\\hat{i} + 0.1552\\hat{j}) + |\\vec{\\omega}_{AD}|\\hat{k} \\times (-0.25\\cos(45^\\circ)\\hat{i} + 0.25\\sin(45^\\circ)\\hat{j})',
            '=',
            '(-1.345\\hat{i} + 0.1552\\hat{j}) - |\\vec{\\omega}_{AD}|(0.25\\sin(45^\\circ))\\hat{i} - |\\vec{\\omega}_{AD}|(0.25\\cos(45^\\circ))\\hat{j}',
        ).scale(0.55).next_to(eq_ad, DOWN, buff=0.2, aligned_edge=LEFT)
        eq_ad_sub[3:].next_to(eq_ad_sub[0], DOWN, aligned_edge=LEFT, buff=0.15).shift(RIGHT)
        eq_ad_sub[5:].next_to(eq_ad_sub[3:5], DOWN, aligned_edge=LEFT, buff=0.15)
        eq_ad_dir_i = MathTex(
            '\\hat{i}:',
            '-|\\vec{v}_D|\\cos(45^\\circ)',
            '=',
            '-1.345 - |\\vec{\\omega}_{AD}|(0.25\\sin(45^\\circ))'
        ).scale(0.55).next_to(eq_ad_sub, DOWN, aligned_edge=LEFT, buff=0.2).shift(0.5*RIGHT)
        eq_ad_dir_i[0].set_color(YELLOW)
        eq_ad_dir_j = MathTex(
            '\\hat{j}:',
            '|\\vec{v}_D|\\sin(45^\\circ)',
            '=',
            '0.1552 - |\\vec{\\omega}_{AD}|(0.25\\cos(45^\\circ))',
        ).scale(0.55).next_to(eq_ad_dir_i, DOWN, aligned_edge=LEFT, buff=0.2)
        eq_ad_dir_j[0].set_color(YELLOW)

        v_d_ans = MathTex('|\\vec{v}_D|=1.06\\,\\mathrm{m/s}').scale(0.55).next_to(eq_ad_dir_j, DOWN, aligned_edge=LEFT)
        omega_ad_ans = MathTex('|\\vec{\\omega}_{AD}|=-3.36\\,\\mathrm{rad/s}').scale(0.55).next_to(v_d_ans, DOWN, aligned_edge=LEFT)
        ansbox2 = SurroundingRectangle(v_d_ans)
        ansgroup2 = Group(v_d_ans, ansbox2, omega_ad_ans)

        self.play(Write(title_link_ad))
        self.play(Write(eq_ad))
        self.wait()
        self.play(Write(eq_ad_sub[:3]))
        self.wait()
        self.play(Write(eq_ad_sub[3:5]))
        self.wait()
        self.play(Write(eq_ad_sub[5:]))
        self.wait()
        self.play(
            Write(eq_ad_dir_i),
            Write(eq_ad_dir_j)
        )
        self.wait()
        self.play(
            Write(v_d_ans),
            Write(omega_ad_ans)
        )
        self.play(ShowCreation(ansbox2))
        self.wait()
        self.play(
            FadeOut(eq_ad),
            FadeOut(eq_ad_sub),
            FadeOut(eq_ad_dir_i),
            FadeOut(eq_ad_dir_j),
            Transform(ansgroup2, ansgroup2.copy().next_to(title_link_ad, DOWN, aligned_edge=LEFT, buff=0.15))
        )
        self.wait()
        #endregion
