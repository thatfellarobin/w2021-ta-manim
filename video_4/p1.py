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
        block_A_assembly = Group(pulley_A, pulley_tie_A, block_A)
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
            pulley_mid,
            block_A_assembly,
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
        block_A_assembly.add(text_A)
        block_B_assembly = Group(block_B, text_B)

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

        # TODO:, should explain how to identify energy problem?

        #region Animate the motion d
        base_string_1 = string_1.get_end()
        base_string_2 = string_2.get_end()
        base_string_3 = string_3.get_start()
        oglength_string_1 = string_1.get_length()
        oglength_string_2 = string_2.get_length()
        oglength_string_3 = string_3.get_length()
        ogposition_block_A = block_A_assembly.get_center()
        block_halfwidth = block_B.copy().rotate(30*(PI/180)).get_width() / 2

        def update_string_3(string):
            string_tip = block_B.get_center() + block_halfwidth*np.array([np.cos(150*(PI/180)), np.sin(150*(PI/180)), 0])
            newstring = Line(
                start=base_string_3,
                end=string_tip,
                color=YELLOW_E
            )
            string.become(newstring)
        def update_string_2(string):
            dB = string_3.get_length() - oglength_string_3
            newlength = oglength_string_2 - (dB/2)
            string_tip = base_string_2 - newlength * string.get_unit_vector()
            newstring = Line(
                start=string_tip,
                end=base_string_2,
                color=YELLOW_E
            )
            string.become(newstring)
        def update_string_1(string):
            dB = string_3.get_length() - oglength_string_3
            newlength = oglength_string_1 - (dB/2)
            string_tip = base_string_1 - newlength * string.get_unit_vector()
            newstring = Line(
                start=string_tip,
                end=base_string_1,
                color=YELLOW_E
            )
            string.become(newstring)
        def update_block_A_assembly(assem):
            ds = (string_3.get_length() - oglength_string_3)/2
            newposition = ogposition_block_A + ds*np.array([np.cos(60*(PI/180)), np.sin(60*(PI/180)), 0])
            assem.shift(newposition - assem.get_center())
        def update_sa(arrow):
            arrow.scale_about_point(point=arrow.get_start(), scale_factor=string_2.get_length()/arrow.get_length())
        def update_sb(arrow):
            arrow.scale_about_point(point=arrow.get_start(), scale_factor=string_3.get_length()/arrow.get_length())

        string_1.add_updater(update_string_1)
        string_2.add_updater(update_string_2)
        string_3.add_updater(update_string_3)
        block_A_assembly.add_updater(update_block_A_assembly)
        s_A_arrow.add_updater(update_sa)
        s_B_arrow.add_updater(update_sb)

        for _ in range(10):
            self.play(
                Transform(
                    block_B_assembly,
                    block_B_assembly.copy().shift(1.5*np.array([np.cos(150*(PI/180)), np.sin(150*(PI/180)), 0])),
                    rate_func=there_and_back,
                    run_time=3
                )
            )
        self.wait()

        string_1.clear_updaters()
        string_2.clear_updaters()
        string_3.clear_updaters()
        block_A_assembly.clear_updaters()
        s_A_arrow.clear_updaters()
        s_B_arrow.clear_updaters()
        #endregion

        #region Annotate d
        d_arrow = Arrow(
            start=block_B.get_center() + block_halfwidth*np.array([np.cos(150*(PI/180)), np.sin(150*(PI/180)), 0]),
            end=block_B.get_center() + 4*block_halfwidth*np.array([np.cos(150*(PI/180)), np.sin(150*(PI/180)), 0]),
            color=PURPLE,
            buff=0.0,
            stroke_width=8,
            tip_length=0.35,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        d_half_arrow = d_arrow.copy()
        d_half_arrow.scale_about_point(point=d_arrow.get_start(), scale_factor=0.5).rotate(about_point=d_arrow.get_start(), angle=PI/2)
        d_half_arrow.shift(block_A.get_center() + block_halfwidth*np.array([np.cos(240*(PI/180)), np.sin(240*(PI/180)), 0]) - d_arrow.get_start())
        d_arrow_annot = MathTex('d', color=PURPLE).scale(0.9).next_to(d_arrow.get_center(), direction=np.array([np.cos(240*(PI/180)), np.sin(240*(PI/180)), 0]), buff=0.1)
        d_half_arrow_annot = MathTex('d/2', color=PURPLE).scale(0.9).next_to(d_half_arrow, direction=LEFT, buff=0.1)

        self.play(Write(d_arrow), Write(d_arrow_annot))
        self.wait()
        self.play(Write(d_half_arrow), Write(d_half_arrow_annot))
        self.wait()
        #endregion

        # Prepare to do math
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
            s_B_annot,
            d_arrow,
            d_arrow_annot,
            d_half_arrow,
            d_half_arrow_annot
        )
        string_sum_grouped = Group(string_sum, string_sum_d)
        self.play(
            Transform(diagram_fullyAnnot, diagram_fullyAnnot.copy().scale(0.6).shift(4*LEFT+1.5*UP)),
            Transform(string_sum_grouped, string_sum_grouped.copy().scale(0.8).to_edge(LEFT).shift(0.5*RIGHT+4*DOWN))
        )
        self.wait()

        #region explain different energy components:
        E_g = MathTex('E_g=mg\\Delta h', color=YELLOW).scale(0.7)
        E_k = MathTex('E_k=\\frac{1}{2}mv^2', color=YELLOW).scale(0.7)
        Work = MathTex('Work=Fs', color=YELLOW).scale(0.7)
        energy_primatives = VGroup(E_g, E_k, Work).arrange(buff=0.5).next_to(diagram_fullyAnnot, RIGHT, aligned_edge=UP, buff=0.75)
        self.play(Write(energy_primatives))
        self.wait()
        hlbox = SurroundingRectangle(E_g, buff=0.15)
        self.play(ShowCreation(hlbox))
        self.wait()
        self.play(Transform(hlbox, SurroundingRectangle(E_k, buff=0.15)))
        self.wait()
        self.play(Transform(hlbox, SurroundingRectangle(Work, buff=0.15)))
        self.wait()
        self.play(FadeOut(hlbox))
        self.wait()
        #endregion

        #region Write energy equation
        energycons_0 = MathTex('Work_{in} - Work_{out} = \\Delta E_g + \\Delta E_k').scale(0.7).next_to(energy_primatives, DOWN, aligned_edge=LEFT)
        self.play(Write(energycons_0))
        self.wait()
        energycons_1 = MathTex(
            '-F_{fA}\\frac{d}{2}-F_{fB}d',
            '=',
            'W_Bd\\sin(\\theta_2) - W_A\\frac{d}{2}\\sin(\\theta_1)',
            '+',
            '\\frac{1}{2}\\frac{W_A}{g}v_A^2 + \\frac{1}{2}\\frac{W_B}{g}v_B^2'
        ).scale(0.6).next_to(energycons_0, DOWN, aligned_edge=LEFT)
        energycons_1[3:].next_to(energycons_1[2], DOWN, aligned_edge=LEFT)
        self.play(Write(energycons_1))
        self.wait()
        energycons_1_simp = MathTex(
            '-\\mu_kN_A\\frac{d}{2} - \\mu_kN_Bd',
            '=',
            'W_Bd\\sin(\\theta_2) - W_A\\frac{d}{2}\\sin(\\theta_1)',
            '+',
            '\\frac{1}{2g}(W_Av_A^2 + W_Bv_B^2)',
        ).scale(0.6).next_to(energycons_0, DOWN, aligned_edge=LEFT)
        energycons_1_simp[3:].next_to(energycons_1_simp[2], DOWN, aligned_edge=LEFT)
        self.play(*[ReplacementTransform(energycons_1[i], energycons_1_simp[i]) for i in range(len(energycons_1))])
        self.wait()

        #region FBD to solve for N_A and N_B
        block_halfwidth *= 0.6 # account for scaling operation of the full diagram
        block_A_fbd = block_A.copy().move_to(1*RIGHT+1.5*DOWN)
        block_A_fbd_label = text_A.copy().move_to(block_A_fbd.get_center())
        block_B_fbd = block_B.copy().next_to(block_A_fbd, RIGHT, buff=3)
        block_B_fbd_label = text_B.copy().move_to(block_B_fbd.get_center())
        fbd_NA = Arrow(
            start=block_A_fbd.get_center() + 3*block_halfwidth*np.array([np.cos(-30*(PI/180)), np.sin(-30*(PI/180)), 0]),
            end=block_A_fbd.get_center() + block_halfwidth*np.array([np.cos(-30*(PI/180)), np.sin(-30*(PI/180)), 0]),
            color=PURPLE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_NA_label = MathTex('N_A', color=PURPLE).scale(0.6).next_to(fbd_NA.get_start(), RIGHT, buff=0.1)
        fbd_NB = Arrow(
            start=block_B_fbd.get_center() + 3*block_halfwidth*np.array([np.cos(-120*(PI/180)), np.sin(-120*(PI/180)), 0]),
            end=block_B_fbd.get_center() + block_halfwidth*np.array([np.cos(-120*(PI/180)), np.sin(-120*(PI/180)), 0]),
            color=PURPLE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_NB_label = MathTex('N_B', color=PURPLE).scale(0.6).next_to(fbd_NB.get_start(), LEFT, buff=0.1)
        fbd_WA = Arrow(
            start=block_A_fbd.get_center(),
            end=block_A_fbd.get_center() + 3*block_halfwidth*DOWN,
            color=BLUE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_WA_label = MathTex('W_A', color=BLUE).scale(0.6).next_to(fbd_WA.get_end(), DOWN, buff=0.1)
        fbd_WB = Arrow(
            start=block_B_fbd.get_center(),
            end=block_B_fbd.get_center() + 3*block_halfwidth*DOWN,
            color=BLUE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_WB_label = MathTex('W_B', color=BLUE).scale(0.6).next_to(fbd_WB.get_end(), DOWN, buff=0.1)
        fbd_TA = Arrow(
            start=block_A_fbd.get_center() + block_halfwidth*np.array([np.cos(60*(PI/180)), np.sin(60*(PI/180)), 0]),
            end=block_A_fbd.get_center() + 3*block_halfwidth*np.array([np.cos(60*(PI/180)), np.sin(60*(PI/180)), 0]),
            color=RED,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_TA_label = MathTex('2T', color=RED).scale(0.6).next_to(fbd_TA.get_end(), RIGHT, buff=0.1)
        fbd_TB = Arrow(
            start=block_B_fbd.get_center() + block_halfwidth*np.array([np.cos(150*(PI/180)), np.sin(150*(PI/180)), 0]),
            end=block_B_fbd.get_center() + 3*block_halfwidth*np.array([np.cos(150*(PI/180)), np.sin(150*(PI/180)), 0]),
            color=RED,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_TB_label = MathTex('T', color=RED).scale(0.6).next_to(fbd_TB.get_end(), LEFT, buff=0.1)
        fbd_FA = Arrow(
            start=block_A_fbd.get_center() + block_halfwidth*np.array([np.cos(-30*(PI/180)), np.sin(-30*(PI/180)), 0]),
            end=block_A_fbd.get_center() + block_halfwidth*np.array([np.cos(-30*(PI/180)), np.sin(-30*(PI/180)), 0]) + 2*block_halfwidth*np.array([np.cos(60*(PI/180)), np.sin(60*(PI/180)), 0]),
            color=MAROON,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_FA_label = MathTex('F_{fA}', color=MAROON).scale(0.6).next_to(fbd_FA.get_end(), RIGHT, buff=0.1)
        fbd_FB = Arrow(
            start=block_B_fbd.get_center() + block_halfwidth*np.array([np.cos(-120*(PI/180)), np.sin(-120*(PI/180)), 0]),
            end=block_B_fbd.get_center() + block_halfwidth*np.array([np.cos(-120*(PI/180)), np.sin(-120*(PI/180)), 0]) + 2*block_halfwidth*np.array([np.cos(-30*(PI/180)), np.sin(-30*(PI/180)), 0]),
            color=MAROON,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_FB_label = MathTex('F_{fB}', color=MAROON).scale(0.6).next_to(fbd_FB.get_end(), RIGHT, buff=0.1)

        self.play(
            FadeIn(block_A_fbd),
            FadeIn(block_A_fbd_label),
            FadeIn(block_B_fbd),
            FadeIn(block_B_fbd_label),
            FadeIn(fbd_NA),
            FadeIn(fbd_NA_label),
            FadeIn(fbd_NB),
            FadeIn(fbd_NB_label),
            FadeIn(fbd_WA),
            FadeIn(fbd_WA_label),
            FadeIn(fbd_WB),
            FadeIn(fbd_WB_label),
            FadeIn(fbd_TA),
            FadeIn(fbd_TA_label),
            FadeIn(fbd_TB),
            FadeIn(fbd_TB_label),
            FadeIn(fbd_FA),
            FadeIn(fbd_FA_label),
            FadeIn(fbd_FB),
            FadeIn(fbd_FB_label)
        )
        self.wait()
        #endregion

        energycons_2 = MathTex(
            '-\\mu_k(W_A\\cos(\\theta_1))\\frac{d}{2} - \\mu_k(W_B\\cos(\\theta_2))d',
            '=',
            'W_Bd\\sin(\\theta_2) - W_A\\frac{d}{2}\\sin(\\theta_1)',
            '+',
            '\\frac{1}{2g}(W_Av_A^2 + W_Bv_B^2)',
        ).scale(0.6).next_to(energycons_0, DOWN, aligned_edge=LEFT)
        energycons_2[1:].next_to(energycons_2[0], DOWN, aligned_edge=LEFT).shift(0.2*RIGHT)
        self.play(*[ReplacementTransform(energycons_1_simp[i], energycons_2[i]) for i in range(len(energycons_1_simp))])
        self.wait()
        hlbox = SurroundingRectangle(energycons_2, buff=0.15)
        hlbox2 = SurroundingRectangle(string_sum_d, buff=0.15)
        self.play(
            ShowCreation(hlbox),
            ShowCreation(hlbox2)
        )
        self.wait()

        v_Afinal = MathTex('v_A=0.233\\,\\mathrm{m/s}').next_to(string_sum_grouped, DOWN, aligned_edge=LEFT, buff=0.5)
        v_Bfinal = MathTex('v_B=-0.466\\,\\mathrm{m/s}').next_to(v_Afinal, DOWN, aligned_edge=LEFT)
        v_final = Group(v_Afinal, v_Bfinal)
        hlbox_final = SurroundingRectangle(v_final, buff=0.2)
        v_final_boxed = Group(v_final, hlbox_final).align_to(hlbox2, LEFT)
        self.play(
            FadeIn(v_final),
            Transform(hlbox.copy(), hlbox_final),
            Transform(hlbox2.copy(), hlbox_final)
        )
        self.wait()
        #endregion
