from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

DSCALE = 3

class T10P2(Scene):
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
        roof = Line(
            start=2.5*LEFT,
            end=2.5*RIGHT,
            color=GREY
        )
        hinge_l_1 = Circle(
            radius=0.2,
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1
        ).shift(1.5*LEFT)
        hinge_l_2 = Dot(
            color=BLUE_E
        ).move_to(hinge_l_1.get_center())
        hinge_l = Group(hinge_l_1, hinge_l_2)
        hinge_r = hinge_l.copy().move_to(1.5*RIGHT)
        link_l = Line(
            start=hinge_l.get_center(),
            end=hinge_l.get_center()+1.5*DOWN,
            color=RED_E,
            stroke_width=20
        )
        link_r = link_l.copy().shift(3*RIGHT)
        hinge_ld = hinge_l.copy().scale(0.75).move_to(link_l.get_end())
        hinge_rd = hinge_r.copy().scale(0.75).move_to(link_r.get_end())
        beam = Rectangle(
            height=0.25,
            width=3.5,
            color=BLUE,
            fill_color=BLUE_DARK,
            fill_opacity=1
        ).move_to((hinge_ld.get_center()+hinge_rd.get_center())/2)
        beam_group = Group(beam, hinge_ld, hinge_rd)

        diagram = Group(
            roof,
            link_l,
            link_r,
            hinge_l,
            hinge_r,
            beam_group
        ).scale(1.5).move_to(ORIGIN)
        self.add(diagram)
        self.wait()
        #endregion

        #region Annotations
        link_l_faded = link_l.copy().set_opacity(0)
        link_r_faded = link_r.copy().set_opacity(0)
        beam_group_faded = beam_group.copy()
        self.recursive_set_opacity(beam_group_faded, 0)
        beam_group_unfaded = beam_group.copy()
        self.recursive_set_opacity(beam_group_unfaded, 0.25)

        path = Arc(
            start_angle=-PI/2,
            angle=-PI/4,
            radius=link_l.get_length()
        )
        path.shift(beam_group.get_center()-path.get_start())

        self.play(
            Transform(link_l_faded, link_l_faded.copy().set_opacity(0.25), run_time=2),
            Transform(link_r_faded, link_r_faded.copy().set_opacity(0.25), run_time=2),
            Transform(beam_group_faded, beam_group_unfaded, run_time=2),
            Rotate(link_l, angle=-PI/4, about_point=hinge_l.get_center(), run_time=2),
            Rotate(link_r, angle=-PI/4, about_point=hinge_r.get_center(), run_time=2),
            MoveAlongPath(beam_group, path, run_time=2)
        )
        self.wait()
        #endregion

        #region Label diagram
        a_l = MathTex('a', color=YELLOW).scale(0.6).next_to(link_l.get_center(), UP+LEFT, buff=0.2)
        a_r = MathTex('a', color=YELLOW).scale(0.6).next_to(link_r.get_center(), UP+LEFT, buff=0.2)
        M_arrow = Arc(
            radius=0.5,
            start_angle=-PI/4,
            angle=-PI,
            color=RED
        ).add_tip(tip_length=0.15)
        M_arrow.move_arc_center_to(hinge_r.get_center())
        M_label = MathTex('M', color=RED).scale(0.6).next_to(M_arrow.get_end(), UP, buff=0.15)
        omega_arrow = Arc(
            radius=0.5,
            start_angle=-PI/4,
            angle=-PI,
            color=PURPLE
        ).add_tip(tip_length=0.15)
        omega_arrow.move_arc_center_to(hinge_l.get_center())
        omega_label = MathTex('\\omega_{AB}', color=PURPLE).scale(0.6).next_to(omega_arrow.get_end(), UP, buff=0.15)
        theta_arrow = Arc(
            radius=1.5,
            start_angle=-PI/2,
            angle=-PI/4,
            color=YELLOW
        ).add_tip(tip_length=0.15)
        theta_arrow.move_arc_center_to(hinge_l.get_center())
        theta_label = MathTex('\\theta_1', color=YELLOW).scale(0.6).next_to(theta_arrow.get_center(), DOWN+LEFT, buff=0.2)
        P_arrow = Arrow(
            start=beam.get_edge_center(RIGHT)+RIGHT,
            end=beam.get_edge_center(RIGHT),
            color=RED,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        P_label = MathTex('P', color=RED).scale(0.6).next_to(P_arrow, RIGHT, buff=0.15)

        self.play(
            Write(a_l),
            Write(a_r),
            Write(M_arrow),
            Write(M_label),
            Write(omega_arrow),
            Write(omega_label),
            Write(theta_arrow),
            Write(theta_label),
            Write(P_arrow),
            Write(P_label)
        )
        diagram = Group(
            link_l_faded,
            link_r_faded,
            beam_group_faded,
            diagram,
            a_l,
            a_r,
            M_arrow,
            M_label,
            omega_arrow,
            omega_label,
            theta_arrow,
            theta_label,
            P_arrow,
            P_label
        )
        self.wait()
        #endregion

        self.play(Transform(diagram, diagram.copy().scale(0.85).to_corner(DOWN+RIGHT, buff=1)))
        self.wait()

        #region Math
        rot_energy_kinetic = MathTex('E_{kin,\\,rot} = \\frac{1}{2}I\\omega^2').scale(0.55).to_corner(UP+LEFT, buff=0.75)
        rot_energy_work = MathTex('\\mathbb{W}_{rot} = M\\theta').scale(0.55).next_to(rot_energy_kinetic, RIGHT, buff=1)
        self.play(Write(rot_energy_kinetic))
        self.wait()
        self.play(Write(rot_energy_work))
        self.wait()

        energy = MathTex(
            '\\Delta \\mathbb{W}',
            '=',
            '\\Delta E_{grav}',
            '+',
            '\\Delta E_{kin}',
        ).scale(0.55).next_to(rot_energy_kinetic, DOWN, aligned_edge=LEFT)
        energy[0].set_color(RED_B)
        energy[2].set_color(BLUE_B)
        energy[4].set_color(GREEN_B)
        energy_0 = MathTex(
            'M\\theta_1',
            '+',
            'Pa\\sin(\\theta_1)',
            '=',
            '2W_1\\left(\\frac{a}{2} - \\frac{a}{2}\\cos(\\theta_1)\\right)',
            '+',
            'W_2(a-a\\cos(\\theta_1))',
            '+',
            '\\frac{1}{2}\\frac{W_2}{g}(a\\omega_{AB})^2 - \\frac{1}{2}\\frac{W_2}{g}(a\\omega_{0})^2',
            '+',
            '2\\left(   \\frac{1}{2}\\left(\\frac{W_1}{3g}a^2\\right)\\omega_{AB}^2 - \\frac{1}{2}\\left(\\frac{W_1}{3g}a^2\\right)\\omega_{0}^2  \\right)',
        ).scale(0.55).next_to(energy, DOWN, aligned_edge=LEFT)
        energy_0[0:3].set_color(RED_B)
        energy_0[4:7].set_color(BLUE_B)
        energy_0[8:].set_color(GREEN_B)
        energy_0[7:].next_to(energy_0[4:7], DOWN, aligned_edge=LEFT)
        self.play(Write(energy))
        self.wait()
        hlbox = SurroundingRectangle(energy[0], stroke_opacity=0.5)
        self.play(
            Write(energy_0[0]),
            ShowCreation(hlbox)
        )
        self.wait(0.5)
        self.play(
            Write(energy_0[1:3])
        )
        self.wait(0.5)
        self.play(
            Write(energy_0[3:5]),
            Transform(hlbox, SurroundingRectangle(energy[2], stroke_opacity=0.5))
        )
        self.wait(0.5)
        self.play(
            Write(energy_0[5:7])
        )
        self.wait(0.5)
        self.play(
            Write(energy_0[7:9]),
            Transform(hlbox, SurroundingRectangle(energy[4], stroke_opacity=0.5))
        )
        self.wait(0.5)
        self.play(
            Write(energy_0[9:])
        )
        self.wait()
        self.play(FadeOut(hlbox))
        self.wait()


        ans = MathTex(
            '\\omega_{AB} = 5.98\\,\\mathrm{rad/s}'
        ).scale(0.6).next_to(energy_0, DOWN, aligned_edge=LEFT)
        ansbox = SurroundingRectangle(ans)
        self.play(Write(ans))
        self.play(ShowCreation(ansbox))
        self.wait()
        #endregion
