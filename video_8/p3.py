from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

DIAGRAM_SCALE = 15


class T8P3(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Diagram objects
        main_gear = Circle(
            radius=DIAGRAM_SCALE*0.1,
            stroke_color=BLUE_E,
            fill_color=BLUE_E_DARK,
            stroke_width=10,
            fill_opacity=1
        )
        secondary_gear = Circle(
            arc_center=DIAGRAM_SCALE*0.15*np.array([np.cos(2*PI/3), np.sin(2*PI/3), 0]),
            radius=DIAGRAM_SCALE*0.05,
            stroke_color=BLUE_E,
            fill_color=BLUE_E_DARK,
            stroke_width=10,
            fill_opacity=1
        )
        main_rod = Rectangle(
            width=DIAGRAM_SCALE*0.3,
            height=0.25,
            color=RED_D,
            stroke_opacity=0,
            fill_opacity=1
        )
        hinge_A = Dot(
            point=main_rod.get_edge_center(RIGHT),
            radius=0.2,
            color=GOLD
        )
        hinge_B = Dot(
            point=main_rod.get_center(),
            radius=0.2,
            color=GOLD
        )
        hinge_C = Dot(
            point=main_rod.get_edge_center(LEFT),
            radius=0.2,
            color=GOLD
        )
        main_rod_assy = Group(main_rod, hinge_A, hinge_B, hinge_C).rotate(-PI/3)
        secondary_rod = Rectangle(
            width=DIAGRAM_SCALE*0.1,
            height=0.15,
            color=RED_D,
            stroke_opacity=0,
            fill_opacity=1
        )
        hinge_D = Dot(
            point=secondary_rod.get_edge_center(LEFT),
            radius=0.12,
            color=GOLD
        )
        hinge_E = Dot(
            point=secondary_rod.get_edge_center(RIGHT),
            radius=0.12,
            color=GOLD
        )
        secondary_rod_assy = Group(secondary_rod, hinge_D, hinge_E).shift(DIAGRAM_SCALE*0.075*RIGHT - hinge_D.get_center())

        diagram = Group(
            main_gear,
            secondary_gear,
            main_rod_assy,
            secondary_rod_assy
        ).move_to(ORIGIN)
        self.add(diagram)
        self.wait()
        #endregion

        #region annotate diagram
        point_A = Dot(
            point=hinge_A.get_center(),
            color=YELLOW
        )
        point_A_annot = MathTex('A', color=YELLOW).scale(0.7).next_to(point_A, RIGHT, buff=0.15)
        point_B = Dot(
            point=hinge_B.get_center(),
            color=YELLOW
        )
        point_B_annot = MathTex('B', color=YELLOW).scale(0.7).next_to(point_B, LEFT, buff=0.15)
        point_C = Dot(
            point=hinge_C.get_center(),
            color=YELLOW
        )
        point_C_annot = MathTex('C', color=YELLOW).scale(0.7).next_to(point_C, LEFT, buff=0.15)
        point_D = Dot(
            point=hinge_D.get_center(),
            color=YELLOW
        )
        point_D_annot = MathTex('D', color=YELLOW).scale(0.7).next_to(point_D, DOWN+RIGHT, buff=0.15)
        point_E = Dot(
            point=hinge_E.get_center(),
            color=YELLOW
        )
        point_E_annot = MathTex('E', color=YELLOW).scale(0.7).next_to(point_E, RIGHT, buff=0.15)
        self.play(
            FadeIn(point_A),
            Write(point_A_annot),
            FadeIn(point_B),
            Write(point_B_annot),
            FadeIn(point_C),
            Write(point_C_annot),
            FadeIn(point_D),
            Write(point_D_annot),
            FadeIn(point_E),
            Write(point_E_annot)
        )
        self.wait()

        rot_DE_arrow = Arc(
            radius=0.5,
            start_angle=-PI/2,
            angle=-PI,
            color=GREEN
        ).add_tip(tip_length=0.15)
        rot_DE_arrow.move_arc_center_to(point_E.get_center())
        rot_DE_annot = MathTex(
            '\\vec{\\omega}_{DE}=-4\\hat{k}',
            '\\vec{\\alpha}_{DE}=-20\\hat{k}',
            color=GREEN
        ).scale(0.7)
        rot_DE_annot[1].next_to(rot_DE_annot[0], DOWN, buff=0.125)
        rot_DE_annot.next_to(rot_DE_arrow.get_end(), UP, buff=0.1)
        self.play(
            FadeIn(rot_DE_arrow),
            Write(rot_DE_annot)
        )
        self.wait()


        diagram = Group(
            diagram,
            point_A,
            point_A_annot,
            point_B,
            point_B_annot,
            point_C,
            point_C_annot,
            point_D,
            point_D_annot,
            point_E,
            point_E_annot,
            rot_DE_arrow,
            rot_DE_annot
        )
        #endregion

        #region Cleanup and show coordinate system
        diagram_newpos = diagram.copy().scale(0.85).to_corner(DOWN+RIGHT, buff=0.75)
        self.play(
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
        coordsys = Group(i_arrow, j_arrow, i_label, j_label, k_dot, k_circle, k_label).scale(0.75).next_to(diagram, LEFT, buff=0, aligned_edge=DOWN)
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

        #region Velocity Analysis
        #region Solving for v_D
        eq_v_D = MathTex(
            '\\vec{v}_D = \\vec{v}_E + \\vec{v}_{D/E}'
        ).scale(0.55).to_corner(UP+LEFT, buff=0.5)
        eq_v_D_sub = MathTex(
            '\\vec{v}_D',
            '=',
            '0 + \\vec{\\omega}_{ED} \\times \\vec{r}_{D/E}',
            '=',
            '-4\\hat{k} \\times -0.1\\hat{i}',
            '\\Rightarrow',
            '\\vec{v}_D = 0.4\\hat{j}',
        ).scale(0.55).next_to(eq_v_D, DOWN, buff=0.2, aligned_edge=LEFT)
        eq_v_D_sub[3:].next_to(eq_v_D_sub[1:3], DOWN, aligned_edge=LEFT, buff=0.15)
        eq_v_D_sub[5:].next_to(eq_v_D_sub[3:5], DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(Write(eq_v_D))
        self.wait()
        self.play(Write(eq_v_D_sub[:5]))
        self.wait(0.5)
        self.play(Write(eq_v_D_sub[5:]))
        self.wait()
        self.play(
            FadeOut(eq_v_D),
            FadeOut(eq_v_D_sub[:-1]),
            Transform(eq_v_D_sub[-1], eq_v_D_sub[-1].copy().to_corner(UP+LEFT, buff=0.5))
        )
        self.wait()
        #endregion

        #region Solving for v_B
        # Assumed directions
        assume_text = Tex('Purple:', ' assumed direction').scale(0.6).to_corner(UP+RIGHT)
        assume_text[0].set_color(PURPLE)
        v_B_arrow = Arrow(
            start=hinge_B.get_center(),
            end=hinge_B.get_center()+np.array([np.cos(PI/6), np.sin(PI/6), 0]),
            color=PURPLE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        v_B_label = MathTex('\\vec{v}_B', color=PURPLE).scale(0.6).next_to(v_B_arrow.get_end(), UP, buff=0.12).shift(0.05*LEFT)
        omega_main_arrow = Arc(
            radius=0.5,
            start_angle=PI,
            angle=1.5*PI,
            color=PURPLE
        ).add_tip(tip_length=0.15)
        omega_main_arrow.move_arc_center_to(main_gear.get_center())
        omega_main_annot = MathTex('\\omega_{G}', color=PURPLE).scale(0.6).next_to(omega_main_arrow.get_end(), UP, buff=0.15)
        self.play(
            Write(assume_text),
            Write(v_B_arrow),
            Write(v_B_label),
            Write(omega_main_arrow),
            Write(omega_main_annot)
        )
        self.wait()

        eq_v_B = MathTex(
            '\\vec{v}_B = \\vec{v}_D + \\vec{v}_{B/D}'
        ).scale(0.55).next_to(eq_v_D_sub[-1], DOWN, aligned_edge=LEFT)
        eq_v_B_sub = MathTex(
            '|\\vec{v}_B|\\cos(30^\\circ)\\hat{i} + |\\vec{v}_B|\\sin(30^\\circ)\\hat{j}',
            '=',
            '0.4\\hat{j} + \\vec{\\omega}_{G} \\times \\vec{r}_{B/D}',
            '=',
            '0.4\\hat{j} + |\\vec{\\omega}_{G}|\\hat{k} \\times -0.075\\hat{i}',
            '=',
            '(0.4 - 0.075|\\vec{\\omega}_{G}|)\\hat{j}'
        ).scale(0.55).next_to(eq_v_B, DOWN, buff=0.2, aligned_edge=LEFT)
        eq_v_B_sub[3:].next_to(eq_v_B_sub[1:3], DOWN, aligned_edge=LEFT, buff=0.15)
        eq_v_B_sub[5:].next_to(eq_v_B_sub[3:5], DOWN, aligned_edge=LEFT, buff=0.15)
        eq_v_B_dir_i = MathTex(
            '\\hat{i}:',
            '|\\vec{v}_B|\\cos(30^\\circ)',
            '=',
            '0'
        ).scale(0.55).next_to(eq_v_B_sub, DOWN, aligned_edge=LEFT, buff=0.2).shift(0.5*RIGHT)
        eq_v_B_dir_i[0].set_color(YELLOW)
        eq_v_B_dir_j = MathTex(
            '\\hat{j}:',
            '|\\vec{v}_B|\\sin(30^\\circ)',
            '=',
            '0.4 - 0.075|\\vec{\\omega}_{G}|',
        ).scale(0.55).next_to(eq_v_B_dir_i, DOWN, aligned_edge=LEFT, buff=0.2)
        eq_v_B_dir_j[0].set_color(YELLOW)

        v_B_ans = MathTex(
            '|\\vec{v}_B| = 0'
        ).scale(0.55).next_to(eq_v_B_dir_j, DOWN, aligned_edge=LEFT)
        omega_G_ans = MathTex(
            '|\\vec{\\omega}_{G}| = 5.33',
            '\\Rightarrow',
            '\\vec{\\omega}_{G} = 5.33\\hat{k}'
        ).scale(0.55).next_to(v_B_ans, DOWN, aligned_edge=LEFT)

        v_B_ans_newpos = v_B_ans.copy().next_to(eq_v_D_sub[-1], DOWN, buff=0.15, aligned_edge=LEFT)
        omega_G_ans_newpos = omega_G_ans[-1].copy().next_to(v_B_ans_newpos, RIGHT, buff=0.75, aligned_edge=DOWN)

        self.play(Write(eq_v_B))
        self.wait()
        self.play(Write(eq_v_B_sub[:3]))
        self.wait(0.5)
        self.play(Write(eq_v_B_sub[3:5]))
        self.wait(0.5)
        self.play(Write(eq_v_B_sub[5:]))
        self.wait()
        self.play(
            Write(eq_v_B_dir_i),
            Write(eq_v_B_dir_j)
        )
        self.wait()
        self.play(
            Write(v_B_ans),
            Write(omega_G_ans)
        )
        self.wait()
        self.play(
            FadeOut(eq_v_B),
            FadeOut(eq_v_B_sub),
            FadeOut(eq_v_B_dir_i),
            FadeOut(eq_v_B_dir_j),
            Transform(v_B_ans, v_B_ans_newpos),
            FadeOut(omega_G_ans[:-1]),
            Transform(omega_G_ans[-1], omega_G_ans_newpos)
        )
        self.wait()
        #endregion

        #region Solving for omega_ABC and omega_F
        v_C_ans = MathTex('\\vec{v}_C = 0').scale(0.55).next_to(v_B_ans[-1], DOWN, aligned_edge=LEFT)
        self.play(Write(v_C_ans))
        self.wait()
        omega_ABC_ans = MathTex('\\vec{\\omega}_{ABC} = 0').scale(0.55).next_to(v_C_ans, RIGHT, aligned_edge=DOWN, buff=0.75)
        ansbox1 = SurroundingRectangle(omega_ABC_ans)
        self.play(Write(omega_ABC_ans))
        self.play(ShowCreation(ansbox1))
        self.wait()

        # Gearing relation
        eq_gear = MathTex(
            '\\vec{\\omega}_Gr_G = -\\vec{\\omega}_Fr_F'
        ).scale(0.55).next_to(v_C_ans, DOWN, aligned_edge=LEFT)
        eq_gear_subbed = MathTex(
            '\\vec{\\omega}_F = -\\frac{\\vec{\\omega}_Gr_G}{r_F} = -\\frac{(5.33\\hat{k})(0.1)}{0.05}',
            '\\Rightarrow',
            '\\vec{\\omega}_F = -10.7\\hat{k}'
        ).scale(0.55).next_to(eq_gear, DOWN, aligned_edge=LEFT)
        eq_gear_subbed[1:].next_to(eq_gear_subbed[0], DOWN, aligned_edge=LEFT).shift(0.5*RIGHT)
        ansbox2 = SurroundingRectangle(eq_gear_subbed[-1])
        ansgroup2 = Group(eq_gear_subbed[-1], ansbox2)
        self.play(Write(eq_gear))
        self.wait()
        self.play(Write(eq_gear_subbed[0]))
        self.wait()
        self.play(Write(eq_gear_subbed[1:]))
        self.play(ShowCreation(ansbox2))
        self.wait()
        self.play(
            FadeOut(eq_gear),
            FadeOut(eq_gear_subbed[:-1]),
            Transform(ansgroup2, ansgroup2.copy().next_to(v_C_ans, DOWN, buff=0.15, aligned_edge=LEFT).shift(0.05*DOWN))
        )
        self.wait()
        #endregion
        #endregion

        #region Acceleration Analysis
        # Acceleration of D
        eq_a_D = MathTex(
            '\\vec{a}_D = \\vec{a}_E + \\vec{\\alpha}_{DE}\\times\\vec{r}_{D/E} - |\\vec{\\omega}_{DE}|^2\\vec{r}_{D/E}'
        ).scale(0.55).next_to(ansgroup2, DOWN, aligned_edge=LEFT)
        eq_a_D_sub = MathTex(
            '\\vec{a}_D',
            '=',
            '0 + (-20\\hat{k}\\times (-0.1\\hat{i})) - 4^2 (-0.1\\hat{i})',
            '\\Rightarrow',
            '\\vec{a}_D = 1.6\\hat{i} + 2\\hat{j}',
        ).scale(0.55).next_to(eq_a_D, DOWN, buff=0.2, aligned_edge=LEFT)
        eq_a_D_sub[3:].next_to(eq_a_D_sub[1:3], DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(Write(eq_a_D))
        self.wait()
        self.play(Write(eq_a_D_sub[:3]))
        self.wait(0.5)
        self.play(Write(eq_a_D_sub[3:]))
        self.wait()
        self.play(
            FadeOut(eq_a_D),
            FadeOut(eq_a_D_sub[:-1]),
            Transform(eq_a_D_sub[-1], eq_a_D_sub[-1].copy().next_to(ansgroup2, DOWN, buff=0.15, aligned_edge=LEFT))
        )
        self.wait()

        # Acceleration of B relative to A
        # Label assumptions
        alpha_ABC_arrow = Arc(
            radius=0.5,
            start_angle=0,
            angle=PI,
            color=PURPLE
        ).add_tip(tip_length=0.15)
        alpha_ABC_arrow.move_arc_center_to(point_A.get_center())
        alpha_ABC_annot = MathTex('\\alpha_{ABC}', color=PURPLE).scale(0.6).next_to(alpha_ABC_arrow.get_end(), DOWN, buff=0.15)
        self.play(
            Write(alpha_ABC_arrow),
            Write(alpha_ABC_annot)
        )
        self.wait()

        # Solve
        eq_a_BA = MathTex(
            '\\vec{a}_B = \\vec{a}_A + \\vec{\\alpha}_{ABC}\\times\\vec{r}_{B/A} - |\\vec{\\omega}_{ABC}|^2\\vec{r}_{B/A}'
        ).scale(0.55).next_to(eq_a_D_sub[-1], DOWN, aligned_edge=LEFT)
        eq_a_BA_sub = MathTex(
            '\\vec{a}_B',
            '=',
            '0 + (|\\vec{\\alpha}_{ABC}|\\hat{k} \\times [-0.15\\sin(30^\\circ)\\hat{i} + 0.15\\cos(30^\\circ)\\hat{j}]) - 0',
            '\\Rightarrow',
            '\\vec{a}_B = -0.130|\\vec{\\alpha}_{ABC}|\\hat{i} - 0.075|\\vec{\\alpha}_{ABC}|\\hat{j}',
        ).scale(0.55).next_to(eq_a_BA, DOWN, buff=0.2, aligned_edge=LEFT)
        eq_a_BA_sub[3:].next_to(eq_a_BA_sub[1:3], DOWN, aligned_edge=LEFT, buff=0.15)
        self.play(Write(eq_a_BA))
        self.wait()
        self.play(Write(eq_a_BA_sub[:3]))
        self.wait(0.5)
        self.play(Write(eq_a_BA_sub[3:]))
        self.wait()
        self.play(
            FadeOut(eq_a_BA),
            FadeOut(eq_a_BA_sub[:-1]),
            Transform(eq_a_BA_sub[-1], eq_a_BA_sub[-1].copy().next_to(eq_a_D_sub[-1], DOWN, buff=0.15, aligned_edge=LEFT))
        )
        self.wait()

        # Acceleration of B relative to D
        # Label assumptions
        alpha_main_annot = MathTex('\\alpha_{G}', color=PURPLE).scale(0.6).next_to(omega_main_annot, UP, buff=0.1)
        self.play(Write(alpha_main_annot))
        self.wait()
        # Solve
        eq_a_BD = MathTex(
            '\\vec{a}_B = \\vec{a}_D + \\vec{\\alpha}_{G}\\times\\vec{r}_{B/D} - |\\vec{\\omega}_{G}|^2\\vec{r}_{B/D}'
        ).scale(0.55).next_to(eq_a_BA_sub[-1], DOWN, aligned_edge=LEFT)
        eq_a_BD_sub = MathTex(
            '-0.130|\\vec{\\alpha}_{ABC}|\\hat{i} - 0.075|\\vec{\\alpha}_{ABC}|\\hat{j}',
            '=',
            '(1.6\\hat{i} + 2\\hat{j}) + (|\\vec{\\alpha}_{G}|\\hat{k} \\times -0.075\\hat{i}) - 5.33^2(-0.075\\hat{i})',
            '='
            '3.73\\hat{i} + (2-0.075|\\vec{\\alpha}_{G}|)\\hat{j}'
        ).scale(0.55).next_to(eq_a_BD, DOWN, buff=0.2, aligned_edge=LEFT)
        eq_a_BD_sub[1:].next_to(eq_a_BD_sub[0], DOWN, aligned_edge=LEFT, buff=0.15).shift(0.5*RIGHT)
        eq_a_BD_sub[3:].next_to(eq_a_BD_sub[1:3], DOWN, aligned_edge=LEFT, buff=0.15)
        self.play(Write(eq_a_BD))
        self.wait()
        self.play(Write(eq_a_BD_sub[0]))
        self.wait(0.5)
        self.play(Write(eq_a_BD_sub[1:3]))
        self.wait(0.5)
        self.play(Write(eq_a_BD_sub[3:]))
        self.wait()
        eq_a_BD_sub_dir_i = MathTex(
            '\\hat{i}:',
            '-0.130|\\vec{\\alpha}_{ABC}|',
            '=',
            '3.73'
        ).scale(0.55).next_to(eq_a_BD_sub, DOWN, aligned_edge=LEFT, buff=0.15).shift(0.5*RIGHT)
        eq_a_BD_sub_dir_i[0].set_color(YELLOW)
        eq_a_BD_sub_dir_j = MathTex(
            '\\hat{j}:',
            '-0.075|\\vec{\\alpha}_{ABC}|',
            '=',
            '2-0.075|\\vec{\\alpha}_{G}|',
        ).scale(0.55).next_to(eq_a_BD_sub_dir_i, DOWN, aligned_edge=LEFT, buff=0.15)
        eq_a_BD_sub_dir_j[0].set_color(YELLOW)

        alpha_AB_ans = MathTex(
            '|\\vec{\\alpha}_{ABC}| = -28.7',
            '\\Rightarrow',
            '\\vec{\\alpha}_{ABC} = -28.7\\hat{k}'
        ).scale(0.55).next_to(eq_a_BD_sub_dir_j, DOWN, aligned_edge=LEFT)
        ansbox3 = SurroundingRectangle(alpha_AB_ans[-1])
        alpha_G_ans = MathTex(
            '|\\vec{\\alpha}_{G}| = -2.03',
            '\\Rightarrow',
            '\\vec{\\alpha}_{G} = -2.03\\hat{k}'
        ).scale(0.55).next_to(alpha_AB_ans, DOWN, aligned_edge=LEFT)
        self.play(
            Write(eq_a_BD_sub_dir_i),
            Write(eq_a_BD_sub_dir_j)
        )
        self.wait()
        self.play(
            Write(alpha_AB_ans),
            Write(alpha_G_ans)
        )
        self.play(ShowCreation(ansbox3))
        self.wait()

        #endregion
