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


class T8P1(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Diagram objects
        disk = Circle(
            radius=DIM_A,
            stroke_color=BLUE_E,
            fill_color=BLUE_E_DARK,
            stroke_width=10,
            fill_opacity=1
        )
        disk_center = Dot(
            point=disk.get_center(),
            radius=0.1,
            color=BLUE_E
        )
        disk_group = Group(disk, disk_center)
        pin = Dot(
            point=disk.get_edge_center(LEFT),
            color=LIGHT_GRAY
        )
        rod = Line(
            start=disk.get_edge_center(LEFT),
            end=disk.get_edge_center(LEFT)+(DIM_A*2)*np.array([-np.cos(PI/6), -np.sin(PI/6), 0]),
            color=RED_E,
            stroke_width=15
        )
        ground = Rectangle(
            width=7,
            height=0.3,
            color=GREY,
            stroke_opacity=0,
            fill_opacity=1
        ).next_to(DIM_A*(LEFT+DOWN), DOWN, buff=0)
        #endregion

        diagram = Group(disk_group, rod, pin, ground).move_to(ORIGIN)
        self.add(diagram)
        self.wait()

        #region annotate region
        radius_arrow = DoubleArrow(
            start=disk.get_center(),
            end=disk.get_center()+DIM_A*np.array([np.cos(PI/4), np.sin(PI/4), 0]),
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        radius_annot = MathTex('a', color=YELLOW).scale(0.7).next_to(radius_arrow, UP+RIGHT, buff=0.15)
        rodlength_arrow = DoubleArrow(
            start=rod.get_start(),
            end=rod.get_end(),
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(0.25*rod.copy().rotate(-PI/2).get_unit_vector())
        rodlength_annot = MathTex(
            '2a',
            color=YELLOW
        ).scale(0.7).next_to(rodlength_arrow.get_center(), rodlength_arrow.copy().rotate(-PI/2).get_unit_vector(), buff=0.15)

        self.play(
            Write(radius_arrow),
            Write(radius_annot),
            Write(rodlength_arrow),
            Write(rodlength_annot)
        )
        self.wait()
        #endregion

        diagram = Group(
            diagram,
            radius_arrow,
            radius_annot,
            rodlength_arrow,
            rodlength_annot
        )

        #region Cleanup and show coordinate system
        diagram_newpos = diagram.copy().scale(0.6).to_corner(DOWN+RIGHT, buff=0.5)
        rod_copy = rod.copy().set_opacity(0)
        rod_newpos = rod.copy().scale(0.75).to_corner(UP+RIGHT, buff=1.25)
        disk_copy = disk_group.copy()
        for item in disk_copy:
            item.set_opacity(0)
        disk_newpos = disk_group.copy().scale(0.75).to_edge(RIGHT, buff=0.5)

        self.play(
            Transform(rod_copy, rod_newpos),
            Transform(disk_copy, disk_newpos),
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

        #region Explain pure rolling
        fixed_point = Dot(
            point=disk_copy.get_edge_center(DOWN),
            color=YELLOW
        )
        fixed_point_annot = MathTex('R', color=YELLOW).scale(0.6).next_to(fixed_point, DOWN, buff=0.15)
        self.play(FadeIn(fixed_point))
        for _ in range(2):
            self.play(Flash(fixed_point))
        self.play(Write(fixed_point_annot))
        self.wait()
        #endregion

        #region Velocity
        # Velocity of A
        r_AR_arrow = Arrow(
            start=fixed_point.get_center(),
            end=disk_copy.get_edge_center(LEFT),
            color=GREEN,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        r_AR_label = MathTex('r_{A/R}', color=GREEN).scale(0.6).next_to(r_AR_arrow.get_center(), UP+RIGHT, buff=0.075)
        self.play(
            FadeIn(r_AR_arrow),
            Write(r_AR_label)
        )
        self.wait()

        eq_a = MathTex(
            '\\vec{v}_A = \\vec{v}_R + \\vec{v}_{A/R}'
        ).scale(0.55).to_corner(UP+LEFT, buff=0.5)
        eq_a_sub = MathTex(
            '\\vec{v}_A',
            '=',
            '0 + \\vec{\\omega}_{disk} \\times \\vec{r}_{A/R}',
            '=',
            '\\omega\\hat{k} \\times (-a\\hat{i} + a\\hat{j})',
            '\\Rightarrow',
            '\\vec{v}_A = -a\\omega\\hat{i} - a\\omega\\hat{j}',
        ).scale(0.55).next_to(eq_a, DOWN, buff=0.2, aligned_edge=LEFT)
        eq_a_sub[3:].next_to(eq_a_sub[1:3], DOWN, aligned_edge=LEFT, buff=0.15)
        eq_a_sub[5:].next_to(eq_a_sub[3:5], DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(Write(eq_a))
        self.wait()
        self.play(Write(eq_a_sub[:3]))
        self.wait(0.5)
        self.play(Write(eq_a_sub[3:5]))
        self.wait(0.5)
        self.play(Write(eq_a_sub[5:]))
        self.wait()
        self.play(
            FadeOut(eq_a),
            FadeOut(eq_a_sub[:-1]),
            Transform(eq_a_sub[-1], eq_a_sub[-1].copy().to_corner(UP+LEFT, buff=0.5))
        )
        self.wait()

        # velocity of B
        # Label assumptions
        assume_text = Tex('Purple:', ' assumed direction').scale(0.6).to_corner(UP+RIGHT)
        assume_text[0].set_color(PURPLE)
        v_b_arrow = Arrow(
            start=rod_copy.get_end(),
            end=rod_copy.get_end()+RIGHT,
            color=PURPLE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        v_b_label = MathTex('\\vec{v}_B', color=PURPLE).scale(0.6).next_to(v_b_arrow, RIGHT, buff=0.15)
        omega_ab_arrow = Arc(
            arc_center=rod_copy.get_center(),
            radius=0.2,
            start_angle=PI,
            angle=1.5*PI,
            color=PURPLE
        ).add_tip(tip_length=0.15)
        omega_ab_arrow.move_arc_center_to(rod_copy.get_center())
        omega_ab_annot = MathTex('\\omega_{AB}', color=PURPLE).scale(0.6).next_to(omega_ab_arrow, UP, buff=0.15)
        self.play(
            Write(assume_text),
            Write(v_b_arrow),
            Write(v_b_label),
            Write(omega_ab_arrow),
            Write(omega_ab_annot)
        )
        self.wait()

        eq_b = MathTex(
            '\\vec{v}_B = \\vec{v}_A + \\vec{v}_{B/A}'
        ).scale(0.55).next_to(eq_a_sub[-1], DOWN, aligned_edge=LEFT)
        eq_b_sub = MathTex(
            '|\\vec{v}_B|\\hat{i}',
            '=',
            '-a\\omega\\hat{i}-a\\omega\\hat{j} + \\vec{\\omega}_{AB}\\times\\vec{r}_{B/A}',
            '=',
            '-a\\omega\\hat{i}-a\\omega\\hat{j} + |\\vec{\\omega}_{AB}|\\hat{k} \\times (-2a\\cos(30^\\circ)\\hat{i} + -a\\hat{j})',
            '=',
            '-a\\omega\\hat{i}-a\\omega\\hat{j} + a|\\vec{\\omega}_{AB}|\\hat{i}-2a\\cos(30^\\circ)|\\vec{\\omega}_{AB}|\\hat{j}',
        ).scale(0.55).next_to(eq_b, DOWN, buff=0.2, aligned_edge=LEFT)
        eq_b_sub[3:].next_to(eq_b_sub[1:3], DOWN, aligned_edge=LEFT, buff=0.15)
        eq_b_sub[5:].next_to(eq_b_sub[3:5], DOWN, aligned_edge=LEFT, buff=0.15)
        eq_b_dir_i = MathTex(
            '\\hat{i}:',
            '|\\vec{v}_B|',
            '=',
            '-a\\omega+a|\\vec{\\omega}_{AB}|'
        ).scale(0.55).next_to(eq_b_sub, DOWN, aligned_edge=LEFT, buff=0.2).shift(0.5*RIGHT)
        eq_b_dir_i[0].set_color(YELLOW)
        eq_b_dir_j = MathTex(
            '\\hat{j}:',
            '0',
            '=',
            '-a\\omega-2a\\cos(30^\\circ)|\\vec{\\omega}_{AB}|',
        ).scale(0.55).next_to(eq_b_dir_i, DOWN, aligned_edge=LEFT, buff=0.2)
        eq_b_dir_j[0].set_color(YELLOW)

        omega_ab_ans = MathTex(
            '|\\vec{\\omega}_{AB}| = \\frac{-\\omega}{2\\cos(30^\\circ)}',
            '\\Rightarrow',
            '\\vec{\\omega}_{AB} = -0.577\\omega\\hat{k}'
        ).scale(0.55).next_to(eq_b_dir_j, DOWN, aligned_edge=LEFT)
        v_b_ans = MathTex(
            '|\\vec{v}_B| = -a\\omega \\left(1 + \\frac{1}{2\\cos(30^\\circ)}\\right)',
            '\\Rightarrow',
            '\\vec{v}_B = -1.58a\\omega\\hat{i}'
        ).scale(0.55).next_to(omega_ab_ans, DOWN, aligned_edge=LEFT)
        ansbox1 = SurroundingRectangle(v_b_ans[2])
        ansgroup1 = Group(v_b_ans[2], ansbox1)

        omega_ab_ans_newpos = omega_ab_ans[-1].copy().next_to(eq_a_sub[-1], DOWN, aligned_edge=LEFT)
        ansgroup1_newpos = ansgroup1.copy().next_to(omega_ab_ans_newpos, DOWN, aligned_edge=LEFT)

        self.play(Write(eq_b))
        self.wait()
        self.play(Write(eq_b_sub[:3]))
        self.wait(0.5)
        self.play(Write(eq_b_sub[3:5]))
        self.wait(0.5)
        self.play(Write(eq_b_sub[5:]))
        self.wait(0.5)
        self.play(
            Write(eq_b_dir_i),
            Write(eq_b_dir_j)
        )
        self.wait(0.5)
        self.play(
            Write(v_b_ans[0]),
            Write(omega_ab_ans[0])
        )
        self.wait(0.5)
        self.play(
            Write(v_b_ans[1:]),
            Write(omega_ab_ans[1:])
        )
        self.play(ShowCreation(ansbox1))
        self.wait()
        self.play(
            FadeOut(eq_b),
            FadeOut(eq_b_sub),
            FadeOut(eq_b_dir_i),
            FadeOut(eq_b_dir_j),
            FadeOut(omega_ab_ans[:-1]),
            FadeOut(v_b_ans[:-1]),
            Transform(omega_ab_ans[-1], omega_ab_ans_newpos),
            Transform(ansgroup1, ansgroup1_newpos)
        )
        self.wait()
        #endregion

        #region Acceleration

        #region Explain pure rolling acceleration
        point_O = Dot(
            point=disk_copy.get_center(),
            color=YELLOW
        )
        point_O_annot = MathTex('O', color=YELLOW).scale(0.6).next_to(point_O, UP+RIGHT, buff=0)
        self.play(
            FadeIn(point_O),
            Write(point_O_annot)
        )
        for _ in range(2):
            self.play(Flash(point_O))
        a_O_arrow = Arrow(
            start=point_O.get_center(),
            end=point_O.get_center()+0.75*LEFT,
            color=TEAL_D,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        a_O_label = MathTex('a_O', color=TEAL_D).scale(0.6).next_to(a_O_arrow.get_center(), UP, buff=0.15)
        self.play(
            Write(a_O_arrow),
            Write(a_O_label)
        )
        self.wait()

        a_O_eq = MathTex(
            '\\vec{a}_O = \\vec{r}_{R/O}\\times\\vec{\\alpha}',
            '\\Rightarrow',
            '\\vec{a}_O = -a\\alpha\\hat{i}'
        ).scale(0.55).next_to(ansgroup1, DOWN, aligned_edge=LEFT)
        self.play(Write(a_O_eq[0]))
        self.wait()
        self.play(Write(a_O_eq[1:]))
        self.wait()
        #endregion

        # Acceleration of A
        eq_a_accel = MathTex(
            '\\vec{a}_A = \\vec{a}_O + \\vec{\\alpha}_{OA}\\times\\vec{r}_{A/O} - |\\vec{\\omega}_{OA}|^2\\vec{r}_{A/O}'
        ).scale(0.55).next_to(a_O_eq, DOWN, aligned_edge=LEFT)
        eq_a_accel_sub = MathTex(
            '\\vec{a}_A',
            '=',
            '-a\\alpha\\hat{i} + (\\alpha\\hat{k}\\times (-a\\hat{i})) - \\omega^2 (-a\\hat{i})',
            '=',
            '-a\\alpha\\hat{i} - a\\alpha\\hat{j} + a\\omega^2\\hat{i}',
            '\\Rightarrow',
            '\\vec{a}_A = a(\\omega^2-\\alpha)\\hat{i} - a\\alpha\\hat{j}',
        ).scale(0.55).next_to(eq_a_accel, DOWN, buff=0.2, aligned_edge=LEFT)
        eq_a_accel_sub[3:].next_to(eq_a_accel_sub[1:3], DOWN, aligned_edge=LEFT, buff=0.15)
        eq_a_accel_sub[5:].next_to(eq_a_accel_sub[3:5], DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(Write(eq_a_accel))
        self.wait()
        self.play(Write(eq_a_accel_sub[:3]))
        self.wait(0.5)
        self.play(Write(eq_a_accel_sub[3:5]))
        self.wait(0.5)
        self.play(Write(eq_a_accel_sub[5:]))
        self.wait()
        self.play(
            FadeOut(eq_a_accel),
            FadeOut(eq_a_accel_sub[:-1]),
            Transform(eq_a_accel_sub[-1], eq_a_accel_sub[-1].copy().next_to(a_O_eq, DOWN, aligned_edge=LEFT))
        )
        self.wait()
        #endregion

