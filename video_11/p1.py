from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

DSCALE = 2

class T10P3(Scene):
    def number_equation(self, eq, n, color=YELLOW_B):
        num = MathTex('\\textbf{' + str(n) + '}', color=color).scale(0.5)
        circle = Circle(
            color=color,
            radius=0.225,
            arc_center=num.get_center()
        )
        line = Line(
            start=circle.get_edge_center(LEFT),
            end=circle.get_edge_center(LEFT)+0.6*LEFT,
            color=color
        )
        group = Group(num, circle, line)
        group.next_to(eq, RIGHT, buff=0.25)
        self.play(FadeIn(group))
        return group

    def recursive_set_opacity(self, mobj, opacity=0):
        for item in mobj:
            if len(item) > 1:
                self.recursive_set_opacity(mobj=item, opacity=opacity)
            else:
                item.set_opacity(opacity)
        return mobj

    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Diagram objects
        pulley_1 = Circle(
            radius=0.5,
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1,
            stroke_width=10
        ).shift(2*UP)
        pulley_2 = Dot(
            color=BLUE_E
        ).move_to(pulley_1.get_center())
        pulley = Group(pulley_1, pulley_2)

        string_left = Line(
            start=pulley.get_edge_center(LEFT),
            end=pulley.get_edge_center(LEFT)+DSCALE*1*DOWN,
            color=YELLOW_B,
        )
        string_right = Line(
            start=pulley.get_edge_center(RIGHT),
            end=pulley.get_edge_center(RIGHT)+DSCALE*2*DOWN
        )
        string_right.set_color([BLACK, YELLOW_B, YELLOW_B])

        block = Rectangle(
            width=0.5,
            height=0.75,
            color=BLUE,
            fill_color=BLUE_DARK,
            fill_opacity=1
        ).next_to(string_left, DOWN, buff=0)

        diagram = Group(
            string_left, string_right, pulley, block
        )

        self.add(diagram)
        self.wait()
        #endregion

        #region Annotate diagram
        s_base = Line(
            start=pulley.get_edge_center(LEFT),
            end=pulley.get_edge_center(LEFT)+0.4*LEFT,
            color=GREEN
        ).shift(0.2*LEFT)
        s_arrow = Arrow(
            start=s_base.get_center(),
            end=np.array([s_base.get_center()[0], block.get_edge_center(UP)[1], 0]),
            color=GREEN,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        s_label = MathTex('s', color=GREEN).scale(0.6).next_to(s_arrow, LEFT, buff=0.15)
        r_arrow = Arrow(
            start=pulley.get_center(),
            end=pulley_1.point_at_angle(PI/4),
            color=YELLOW,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        r_label = MathTex('r', color=YELLOW).scale(0.6).next_to(r_arrow.get_end(), UP+RIGHT, buff=0.15)

        self.play(
            ShowCreation(s_base),
            Write(s_arrow),
            Write(s_label),
            Write(r_arrow),
            Write(r_label)
        )
        self.wait()
        diagram = Group(
            diagram,
            s_base,
            s_arrow,
            s_label,
            r_arrow,
            r_label
        )
        #endregion

        #region Animate falling
        self.play(Transform(s_label, MathTex('s_1', color=GREEN).scale(0.6).move_to(s_label.get_center())))
        self.wait()

        block_faded = block.copy().set_opacity(0)
        new_string_left = string_left.copy().set_length(DSCALE*2)
        new_string_left.shift(pulley.get_edge_center(LEFT)-new_string_left.get_start())
        new_s_base = s_base.copy().scale(2.5)
        new_s_base.shift(s_base.get_start()-new_s_base.get_start())
        s2_arrow = Arrow(
            start=new_s_base.get_end()+0.2*RIGHT,
            end=np.array([(new_s_base.get_end()+0.2*RIGHT)[0], (block.get_edge_center(UP)+2*DOWN)[1], 0]),
            color=GREEN,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        s2_label = MathTex('s_2', color=GREEN).scale(0.6).next_to(s2_arrow, LEFT, buff=0.15)

        self.play(
            Transform(block_faded, block_faded.copy().set_opacity(0.25), run_time=2),
            Transform(string_left, new_string_left, run_time=2),
            Transform(block, block.copy().shift(DSCALE*1*DOWN), run_time=2),
            Transform(s_base, new_s_base, run_time=2)
        )
        self.play(
            Write(s2_arrow),
            Write(s2_label)
        )
        self.wait()

        diagram = Group(
            diagram,
            block_faded,
            s2_arrow,
            s2_label
        )
        #endregion

        # Cleanup
        self.play(Transform(diagram, diagram.copy().scale(0.9).to_corner(DOWN+RIGHT, buff=1)))
        self.wait()

        #region Math
        energy = MathTex(
            '\\Delta {W}',
            '=',
            '\\Delta E_{grav}',
            '+',
            '\\Delta E_{kin}',
        ).scale(0.65).to_corner(UP+LEFT, buff=0.75)
        energy_0 = MathTex(
            '0',
            '=',
            '-m_Ag(s_2-s_1)',
            '+',
            '\\frac{1}{2}m_Av_A^2',
            '+',
            '\\frac{1}{2}m_Sk_O^2\\omega_S^2',
        ).scale(0.65).next_to(energy, DOWN, aligned_edge=LEFT)
        self.play(Write(energy))
        self.wait()
        self.play(
            Write(energy_0[0])
        )
        self.wait(0.5)
        self.play(
            Write(energy_0[1:3])
        )
        self.wait(0.5)
        self.play(
            Write(energy_0[3:5])
        )
        self.wait(0.5)
        self.play(
            Write(energy_0[5:7])
        )
        self.number_equation(energy_0, 1)
        self.wait()

        kin_eq = MathTex(
            'v_A = r\\omega_S'
        ).scale(0.55).next_to(energy_0, DOWN, aligned_edge=LEFT)
        self.play(Write(kin_eq))
        self.number_equation(kin_eq, 2)
        self.wait()


        ans = MathTex(
            '\\omega_S = 41.8\\,\\mathrm{rad/s}'
        ).scale(0.7).next_to(kin_eq, DOWN, aligned_edge=LEFT, buff=0.5).shift(0.15*RIGHT)
        ansbox = SurroundingRectangle(ans, buff=0.15)
        self.play(Write(ans))
        self.play(ShowCreation(ansbox))
        self.wait()
        #endregion
