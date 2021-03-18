from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

DSCALE = 1/3
IMGSCALE = 5/500


class T9P1(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        reserved_area = Rectangle(
            width=IMGSCALE*466,
            height=IMGSCALE*572,
            color=YELLOW
        ).to_corner(UP+RIGHT, buff=0.5)
        self.add(reserved_area)

        #region Free body diagram of weight
        block = Rectangle(
            height=1,
            width=0.75,
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1
        )
        fbd_tension_arrow = Arrow(
            start=block.get_edge_center(UP),
            end=block.get_edge_center(UP)+UP,
            color=RED,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_tension_label = MathTex('2T', color=RED).scale(0.6).next_to(fbd_tension_arrow, UP, buff=0.1)
        mg_a_arrow = Arrow(
            start=block.get_edge_center(DOWN),
            end=block.get_edge_center(DOWN)+DOWN,
            color=PURPLE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        mg_a_label = MathTex('m_ag', color=PURPLE).scale(0.6).next_to(mg_a_arrow, DOWN, buff=0)
        accel_a_arrow = Arrow(
            start=block.get_edge_center(RIGHT)+0.25*RIGHT,
            end=block.get_edge_center(RIGHT)+0.25*RIGHT+UP,
            color=BLUE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        accel_a_label = MathTex('\\frac{a}{2}', color=BLUE).scale(0.6).next_to(accel_a_arrow, UP, buff=0.1)

        fbd = Group(
            block,
            fbd_tension_arrow,
            fbd_tension_label,
            mg_a_arrow,
            mg_a_label,
            accel_a_arrow,
            accel_a_label
        ).move_to(ORIGIN)

        self.add(block)
        self.wait()
        self.play(
            Write(mg_a_arrow),
            Write(mg_a_label)
        )
        self.wait(0.5)
        self.play(
            Write(fbd_tension_arrow),
            Write(fbd_tension_label)
        )
        self.wait(0.5)
        self.play(
            Write(accel_a_arrow),
            Write(accel_a_label)
        )
        self.wait()

        self.play(
            Transform(fbd, fbd.copy().scale(0.75).next_to(reserved_area, LEFT, aligned_edge=UP))
        )
        self.wait()

        fbd_eq = MathTex(
            '\\Sigma F_y = m\\frac{a}{2} = 2T - m_ag'
        ).scale(0.6).to_corner(UP+LEFT, buff=0.75)
        fbd_eq_sub = MathTex(
            'T=43.24\\,\\mathrm{kN}'
        ).scale(0.6).next_to(fbd_eq, DOWN, aligned_edge=LEFT)

        self.play(Write(fbd_eq))
        self.wait()
        self.play(Write(fbd_eq_sub))
        self.wait()
        self.play(
            FadeOut(fbd_eq),
            Transform(fbd_eq_sub, fbd_eq_sub.copy().to_corner(UP+LEFT, buff=0.75))
        )
        self.wait()
        #endregion

        #region Beam
        beam = Line(
            start=ORIGIN,
            end=DSCALE*12*np.array([np.cos(PI/3), np.sin(PI/3), 0]),
            stroke_width=15,
            color=GREY
        )
        mg_b_arrow = Arrow(
            start=beam.get_center(),
            end=beam.get_center()+DOWN,
            color=PURPLE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        mg_b_label = MathTex('m_bg', color=PURPLE).scale(0.6).next_to(mg_b_arrow, DOWN, buff=0.1)
        tension_1_arrow = Arrow(
            start=beam.get_end()+beam.get_unit_vector(),
            end=beam.get_end(),
            color=RED,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        tension_1_label = MathTex('T', color=RED).scale(0.6).next_to(tension_1_arrow, beam.get_unit_vector(), buff=0.1)
        tension_2_arrow = Arrow(
            start=beam.get_end(),
            end=beam.get_end()+DOWN,
            color=RED,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        tension_2_label = MathTex('2T', color=RED).scale(0.6).next_to(tension_2_arrow, DOWN, buff=0.1)
        f_A_x_arrow = Arrow(
            start=beam.get_start()+LEFT,
            end=beam.get_start(),
            color=BLUE,
            buff=0.05,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        f_A_x_label = MathTex('F_{Ax}', color=BLUE).scale(0.6).next_to(f_A_x_arrow, LEFT, buff=0.1)
        f_A_y_arrow = Arrow(
            start=beam.get_start()+DOWN,
            end=beam.get_start(),
            color=BLUE,
            buff=0.05,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        f_A_y_label = MathTex('F_{Ay}', color=BLUE).scale(0.6).next_to(f_A_y_arrow, DOWN, buff=0.1)
        f_C_y_arrow = Arrow(
            start=DSCALE*4*np.array([np.cos(PI/3), np.sin(PI/3), 0])+DOWN,
            end=DSCALE*4*np.array([np.cos(PI/3), np.sin(PI/3), 0]),
            color=BLUE,
            buff=0.,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        f_C_y_label = MathTex('F_{Cy}', color=BLUE).scale(0.6).next_to(f_C_y_arrow, DOWN, buff=0.1)

        beam_fbd = Group(
            beam,
            mg_b_arrow,
            mg_b_label,
            tension_1_arrow,
            tension_1_label,
            tension_2_arrow,
            tension_2_label,
            f_A_x_arrow,
            f_A_x_label,
            f_A_y_arrow,
            f_A_y_label,
            f_C_y_arrow,
            f_C_y_label,
        ).scale(0.75).next_to(fbd, DOWN, aligned_edge=RIGHT)

        self.play(FadeIn(beam))
        self.wait()
        self.play(
            Write(mg_b_arrow),
            Write(mg_b_label)
        )
        self.wait()
        self.play(
            Write(tension_1_arrow),
            Write(tension_1_label)
        )
        self.wait()
        self.play(
            Write(tension_2_arrow),
            Write(tension_2_label)
        )
        self.wait()
        self.play(
            Write(f_A_x_arrow),
            Write(f_A_x_label),
            Write(f_A_y_arrow),
            Write(f_A_y_label)
        )
        self.wait()
        self.play(
            Write(f_C_y_arrow),
            Write(f_C_y_label)
        )
        self.wait()


        moment_eq_base = MathTex(
            '\\Sigma',
            'M',
            '=',
            '0'
        ).scale(0.6).next_to(fbd_eq_sub, DOWN, aligned_edge=LEFT)
        self.play(Write(moment_eq_base))
        self.wait()
        for _ in range(2):
            self.play(Flash(beam.get_start()))

        self.play(
            Transform(f_A_x_arrow, f_A_x_arrow.copy().set_opacity(0.33)),
            Transform(f_A_x_label, f_A_x_label.copy().set_opacity(0.33)),
            Transform(f_A_y_arrow, f_A_y_arrow.copy().set_opacity(0.33)),
            Transform(f_A_y_label, f_A_y_label.copy().set_opacity(0.33)),
            Transform(tension_1_arrow, tension_1_arrow.copy().set_opacity(0.33)),
            Transform(tension_1_label, tension_1_label.copy().set_opacity(0.33))
        )
        self.wait()

        moment_eq = MathTex(
            '\\Sigma',
            'M_A',
            '=',
            '0',
            '=',
            'b\\cos(\\theta) F_{Cy}',
            '-(b+c)\\cos(\\theta) m_bg',
            '-(b+c+d)\\cos(\\theta) 2T',
        ).scale(0.6).next_to(fbd_eq_sub, DOWN, aligned_edge=LEFT)
        moment_eq[6:].next_to(moment_eq[5], DOWN, aligned_edge=LEFT)
        moment_eq[7:].next_to(moment_eq[6], DOWN, aligned_edge=LEFT)
        self.play(*[ReplacementTransform(moment_eq_base[i], moment_eq[i]) for i in range(len(moment_eq_base))])
        self.wait()
        self.play(Write(moment_eq[4:6]))
        self.wait()
        self.play(Write(moment_eq[6]))
        self.wait()
        self.play(Write(moment_eq[7]))
        self.wait()

        ans_eq = MathTex(
            'F_{Cy} = 289\\,\\mathrm{kN}'
        ).scale(0.8).next_to(moment_eq, DOWN, buff=0.3, aligned_edge=LEFT)
        ansbox = SurroundingRectangle(ans_eq, buff=0.15)
        self.play(Write(ans_eq))
        self.play(ShowCreation(ansbox))
        self.wait()

        #endregion