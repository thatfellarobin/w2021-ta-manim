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


class T8P2(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Diagram objects
        gear = Circle(
            radius=DIM_A,
            stroke_color=BLUE_E,
            fill_color=BLUE_E_DARK,
            stroke_width=10,
            fill_opacity=1
        )
        gear_center = Dot(
            point=gear.get_center(),
            radius=0.1,
            color=BLUE_E
        )
        gear_group = Group(gear, gear_center)

        rack = Rectangle(
            width=5,
            height=0.5,
            color=RED_D,
            stroke_opacity=0,
            fill_opacity=1
        ).next_to(gear_group, DOWN, buff=0)

        diagram = Group(gear_group, rack).move_to(ORIGIN)
        self.add(diagram)
        self.wait()
        #endregion

        #region annotate diagram
        point_B = SmallDot(
            point=gear.get_edge_center(UP),
            color=YELLOW
        )
        point_B_annot = MathTex('B', color=YELLOW).scale(0.7).next_to(point_B, UP, buff=0.15)
        point_O = SmallDot(
            point=gear.get_center(),
            color=YELLOW
        )
        point_O_annot = MathTex('O', color=YELLOW).scale(0.7).next_to(point_O, DOWN+LEFT, buff=0.1)
        point_A = SmallDot(
            point=gear.get_edge_center(DOWN),
            color=YELLOW
        )
        point_A_annot = MathTex('A', color=YELLOW).scale(0.7).next_to(point_A, DOWN+RIGHT, buff=0)
        point_P_annot = MathTex('P', color=WHITE).scale(0.7).next_to(rack.get_edge_center(LEFT), RIGHT, buff=0.5)


        radius_arrow = DoubleArrow(
            start=gear.get_center(),
            end=gear.get_center()+DIM_A*np.array([np.cos(PI/4), np.sin(PI/4), 0]),
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        radius_annot = MathTex('0.15\\,\\mathrm{m}', color=YELLOW).scale(0.7).next_to(radius_arrow, UP+RIGHT, buff=0.15)
        gear_move_arrow = Arrow(
            start=gear.get_center(),
            end=gear.get_center()+2*RIGHT,
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        gear_move_annot = MathTex(
            'v_O = 3\\,\\mathrm{m/s}',
            'a_O = 6\\,\\mathrm{m/s^2}',
            color=YELLOW
        ).scale(0.7)
        gear_move_annot[1].next_to(gear_move_annot[0], DOWN, aligned_edge=LEFT, buff=0.1)
        gear_move_annot.next_to(gear_move_arrow, RIGHT, buff=0.1)
        rack_move_arrow = Arrow(
            start=rack.get_corner(UP+LEFT),
            end=rack.get_corner(UP+LEFT)+LEFT,
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        rack_move_annot = MathTex(
            'v_P = 2\\,\\mathrm{m/s}',
            'a_P = 3\\,\\mathrm{m/s^2}',
            color=YELLOW
        ).scale(0.7)
        rack_move_annot[1].next_to(rack_move_annot[0], DOWN, aligned_edge=RIGHT, buff=0.1)
        rack_move_annot.next_to(rack_move_arrow, LEFT, buff=0.1)

        self.play(
            Write(point_B),
            Write(point_B_annot),
            Write(point_A),
            Write(point_A_annot),
            Write(point_O),
            Write(point_O_annot),
            Write(point_P_annot),
            Write(radius_arrow),
            Write(radius_annot),
            Write(gear_move_arrow),
            Write(gear_move_annot),
            Write(rack_move_arrow),
            Write(rack_move_annot)
        )
        self.wait()

        diagram = Group(
            diagram,
            point_B,
            point_B_annot,
            point_O,
            point_O_annot,
            point_A,
            point_A_annot,
            point_P_annot,
            radius_arrow,
            radius_annot,
            gear_move_arrow,
            gear_move_annot,
            rack_move_arrow,
            rack_move_annot
        )
        #endregion

        #region Cleanup and show coordinate system
        diagram_newpos = diagram.copy().scale(0.65).to_corner(DOWN+RIGHT, buff=0.75)
        gear_copy = gear_group.copy()
        for item in gear_copy:
            item.set_opacity(0)
        gear_newpos = gear_group.copy().scale(0.9).next_to(diagram_newpos, UP, aligned_edge=RIGHT, buff=0.5).shift(2*LEFT)

        self.play(
            Transform(gear_copy, gear_newpos),
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

        #region Math it out
        #region Solving for omega
        gear_move_arrow2 = Arrow(
            start=gear_copy.get_center(),
            end=gear_copy.get_center()+(2/3)*3*RIGHT,
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        gear_move_annot2 = MathTex(
            'v_O = 3\\,\\mathrm{m/s}',
            color=YELLOW
        ).scale(0.6).next_to(gear_move_arrow2, RIGHT, buff=0.1)
        rack_move_arrow2 = Arrow(
            start=gear_copy.get_edge_center(DOWN),
            end=gear_copy.get_edge_center(DOWN)+(2/3)*2*LEFT,
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        rack_move_annot2 = MathTex(
            'v_P = 2\\,\\mathrm{m/s}',
            color=YELLOW
        ).scale(0.6).next_to(rack_move_arrow2, LEFT, buff=0.1)
        self.play(
            Write(gear_move_arrow2),
            Write(gear_move_annot2),
            Write(rack_move_arrow2),
            Write(rack_move_annot2)
        )
        self.wait()

        ic_joinline1 = Line(
            start=gear_move_arrow2.get_start(),
            end=rack_move_arrow2.get_start(),
            color=YELLOW,
            stroke_opacity=0.5
        )
        ic_joinline2 = Line(
            start=gear_move_arrow2.get_end(),
            end=rack_move_arrow2.get_end(),
            color=YELLOW,
            stroke_opacity=0.5
        )
        self.play(ShowCreation(ic_joinline1))
        self.wait()
        self.play(ShowCreation(ic_joinline2))
        self.wait()

        ic_anim_dist = np.linalg.norm(gear_copy.get_center() - gear_copy.get_edge_center(DOWN)) * (0.09/0.15)

        point_IC = Dot(
            point=gear_copy.get_center() + ic_anim_dist*DOWN,
            color=YELLOW
        )
        point_IC_annot = MathTex('IC', color=YELLOW).scale(0.6).next_to(point_IC, UP+LEFT, buff=0)
        self.play(FadeIn(point_IC))
        for _ in range(2):
            self.play(Flash(point_IC))
        self.play(Write(point_IC_annot))
        self.wait()

        sim_triang_eq = MathTex(
            '\\frac{3}{r_{O/IC}}',
            '=',
            '\\frac{2}{r_{A/IC}}'
        ).scale(0.55).to_corner(UP+LEFT, buff=0.5)
        sim_triang_eq_subbed = MathTex(
            '\\frac{3}{r_{O/IC}}',
            '=',
            '\\frac{2}{0.15-r_{O/IC}}'
        ).scale(0.55)
        sim_triang_eq_subbed.shift(sim_triang_eq[1].get_center() - sim_triang_eq_subbed[1].get_center())
        self.play(Write(sim_triang_eq))
        self.wait()
        self.play(*[ReplacementTransform(sim_triang_eq[i], sim_triang_eq_subbed[i]) for i in range(len(sim_triang_eq))])
        self.wait()
        sim_triang_result = MathTex(
            'r_{O/IC} = 0.09\\,\\mathrm{m}'
        ).scale(0.55).next_to(sim_triang_eq_subbed, RIGHT, buff=1)
        omega_eq = MathTex(
            '\\vec{\\omega} = \\frac{v_O}{r_{O/IC}}(-\\hat{k}) = \\frac{3}{0.09}(-\\hat{k})',
            '\\vec{\\omega} = -33.33\\hat{k}\\,\\mathrm{rad/s}'
        ).scale(0.55).next_to(sim_triang_eq_subbed, DOWN, aligned_edge=LEFT)
        omega_eq[1].next_to(omega_eq[0], DOWN, aligned_edge=LEFT)

        self.play(Write(sim_triang_result))
        self.wait()
        self.play(Write(omega_eq[0]))
        self.wait()
        self.play(Write(omega_eq[1]))
        self.wait()
        sim_triang_result_newpos = sim_triang_result.copy().to_corner(UP+LEFT, buff=0.5)
        omega_eq_newpos = omega_eq[1].copy().next_to(sim_triang_result_newpos, RIGHT, aligned_edge=DOWN, buff=0.75)
        self.play(
            FadeOut(sim_triang_eq),
            FadeOut(sim_triang_eq_subbed),
            FadeOut(omega_eq[0]),
            Transform(sim_triang_result, sim_triang_result_newpos),
            Transform(omega_eq[1], omega_eq_newpos)
        )
        self.wait()
        #endregion

        #region Acceleration relation of A and O
        # Assumed directions
        assume_text = Tex('Purple:', ' assumed direction').scale(0.6).to_corner(UP+RIGHT)
        assume_text[0].set_color(PURPLE)
        a_An_arrow = Arrow(
            start=gear_copy.get_edge_center(DOWN),
            end=gear_copy.get_edge_center(DOWN)+0.75*UP,
            color=PURPLE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        a_An_label = MathTex('\\vec{a}_{A,n}', color=PURPLE).scale(0.6).next_to(a_An_arrow.get_end(), RIGHT, buff=0.15)
        alpha_ab_arrow = Arc(
            radius=0.2,
            start_angle=PI,
            angle=1.5*PI,
            color=PURPLE
        ).add_tip(tip_length=0.15)
        alpha_ab_arrow.move_arc_center_to(gear_copy.get_center())
        alpha_ab_annot = MathTex('\\alpha', color=PURPLE).scale(0.6).next_to(alpha_ab_arrow, UP, buff=0.15)
        self.play(
            Write(assume_text),
            Write(a_An_arrow),
            Write(a_An_label),
            Write(alpha_ab_arrow),
            Write(alpha_ab_annot)
        )
        self.wait()
        # Math
        eq_ab_accel = MathTex(
            '\\vec{a}_A = \\vec{a}_O + \\vec{\\alpha}\\times\\vec{r}_{A/O} - |\\vec{\\omega}|^2\\vec{r}_{A/O}'
        ).scale(0.55).next_to(sim_triang_result, DOWN, aligned_edge=LEFT)
        eq_ab_accel_sub = MathTex(
            '-3\\hat{i} + |\\vec{a}_{A,n}|\\hat{j}',
            '=',
            '6\\hat{i} + |\\vec{\\alpha}|\\hat{k} \\times (-0.15\\hat{j}) - 33.33^2 (-0.15\\hat{j})',
            '=',
            '(6+0.15|\\vec{\\alpha}|)\\hat{i} + 166.67\\hat{j}'
        ).scale(0.55).next_to(eq_ab_accel, DOWN, buff=0.2, aligned_edge=LEFT)
        eq_ab_accel_sub[3:].next_to(eq_ab_accel_sub[1:3], DOWN, aligned_edge=LEFT, buff=0.15)
        eq_ab_accel_dir_i = MathTex(
            '\\hat{i}:',
            '-3',
            '=',
            '6+0.15|\\vec{\\alpha}|'
        ).scale(0.55).next_to(eq_ab_accel_sub, DOWN, aligned_edge=LEFT, buff=0.2).shift(0.5*RIGHT)
        eq_ab_accel_dir_i[0].set_color(YELLOW)
        eq_ab_accel_dir_j = MathTex(
            '\\hat{j}:',
            '|\\vec{a}_{A,n}|',
            '=',
            '166.67',
        ).scale(0.55).next_to(eq_ab_accel_dir_i, DOWN, aligned_edge=LEFT, buff=0.2)
        eq_ab_accel_dir_j[0].set_color(YELLOW)

        alpha_ab_ans = MathTex(
            '|\\vec{\\alpha}| = -60\\,\\mathrm{rad/s^2}',
            '\\Rightarrow',
            '\\vec{\\alpha} = -60\\hat{k}'
        ).scale(0.55).next_to(eq_ab_accel_dir_j, DOWN, aligned_edge=LEFT).shift(0.5*LEFT)
        ansbox1 = SurroundingRectangle(alpha_ab_ans[-1])
        ansgroup1 = Group(alpha_ab_ans[-1], ansbox1)

        self.play(Write(eq_ab_accel))
        self.wait()
        self.play(Write(eq_ab_accel_sub[:3]))
        self.wait(0.5)
        self.play(Write(eq_ab_accel_sub[3:]))
        self.wait(0.5)
        self.play(
            Write(eq_ab_accel_dir_i),
            Write(eq_ab_accel_dir_j)
        )
        self.wait(0.5)
        self.play(Write(alpha_ab_ans[0]))
        self.wait(0.5)
        self.play(Write(alpha_ab_ans[1:]))
        self.play(ShowCreation(ansbox1))
        self.wait()

        self.play(
            FadeOut(eq_ab_accel),
            FadeOut(eq_ab_accel_sub),
            FadeOut(eq_ab_accel_dir_i),
            FadeOut(eq_ab_accel_dir_j),
            FadeOut(alpha_ab_ans[:-1]),
            Transform(ansgroup1, ansgroup1.copy().next_to(sim_triang_result, DOWN, aligned_edge=LEFT))
        )
        self.wait()
        #endregion


        #endregion