from manim import *
import numpy as np

ROD_LENGTH = 4.0
BLUE_E_DARK = '#0c343d'

class Q2(Scene):
    def construct(self):
        #region Diagram imagery
        particle = Dot(radius=0.2, color=YELLOW)
        track_up = Rectangle(
            height=0.1,
            width=5.0,
            fill_color=GREY,
            fill_opacity=1,
            stroke_opacity=0
        ).next_to(particle, UP, buff=0).shift(1*LEFT)
        track_down = Rectangle(
            height=0.1,
            width=5.0,
            fill_color=GREY,
            fill_opacity=1,
            stroke_opacity=0
        ).next_to(particle, DOWN, buff=0).shift(1*LEFT)
        rod = Line(
            start=np.array([0.8*np.sin(30*(np.pi/180)), 0.8*np.cos(30*(np.pi/180)), 0]),
            end=np.array([-ROD_LENGTH*np.sin(30*(np.pi/180)), -ROD_LENGTH*np.cos(30*(np.pi/180)), 0]),
            color=BLUE_E,
            stroke_width=20.0
        )
        rod.shift(0.34*LEFT)
        hinge = Circle(
            arc_center=rod.get_end(),
            radius=0.2,
            stroke_width=10.0,
            fill_color=BLUE_E,
            stroke_color=BLUE_E_DARK,
            fill_opacity=1.0,
            stroke_opacity=1.0,
        )
        diagram = Group(track_up, track_down, particle, rod, hinge).move_to(ORIGIN)
        self.add(diagram)
        self.wait()
        #endregion

        #region Diagram annotations
        # Fade out diagram
        mask = Rectangle(width=diagram.get_width()+0.2, height=diagram.get_height()+0.2, color=BLACK, stroke_opacity=0, fill_opacity=0.3).move_to(diagram.get_center())
        self.play(FadeIn(mask))

        r_arrow = Arrow(
            start=rod.get_end(),
            end=particle.get_center(),
            color=GREEN,
            buff=0.0,
            stroke_width=8,
            tip_length=0.3,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        r_arrow_angle = np.arctan(r_arrow.get_unit_vector()[1] / r_arrow.get_unit_vector()[0])
        r_annot = MathTex('r', color=GREEN).next_to(r_arrow.get_center(), np.array([np.cos(-np.pi/4), np.sin(-np.pi/4), 0]))
        self.play(ShowCreation(r_arrow, run_time=1.5), Write(r_annot))
        self.wait()

        theta_ref = Line(
            start=hinge.get_center(),
            end=hinge.get_center()+2.5*UP,
            color=GREY
        )
        theta_arrow = Arc(
            start_angle=PI/2,
            angle=-(PI/2)+r_arrow_angle,
            radius=2,
            arc_center=hinge.get_center(),
            color=YELLOW
        ).add_tip(tip_length=0.2)
        theta_annot = MathTex('\\theta=30^{\\circ}', color=YELLOW).scale(0.7).next_to(theta_arrow, UP, buff=0.1).shift(0.1*RIGHT)
        self.play(
            ShowCreation(theta_ref),
            ShowCreation(theta_arrow),
            Write(theta_annot)
        )
        self.wait()

        h_ref = Line(
            start=hinge.get_center(),
            end=hinge.get_center()+4*RIGHT,
            color=GREY
        )
        h_value = np.array([0, (particle.get_center() - hinge.get_center())[1], 0])
        h_arrow = DoubleArrow(
            start=particle.get_center() - h_value,
            end=particle.get_center(),
            color=GREEN,
            buff=0.0,
            stroke_width=8,
            tip_length=0.3,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(0.75*RIGHT)
        h_annot = MathTex('h=0.5\\,\\mathrm{m}').scale(0.7).next_to(h_arrow, RIGHT, buff=0.1)
        self.play(
            ShowCreation(h_ref),
            ShowCreation(h_arrow),
            ShowCreation(h_annot)
        )
        self.wait()
        #endregion

        full_diagram = Group(diagram, mask, r_arrow, r_annot, theta_ref, theta_arrow, theta_annot, h_ref, h_arrow, h_annot)
        self.play(Transform(full_diagram, full_diagram.copy().scale(0.7).shift(4.75*LEFT+1.5*UP)))
        given_theta_dot = MathTex('\\dot{\\theta}=2\\,\\mathrm{rad/s}').scale(0.7).next_to(full_diagram, DOWN, aligned_edge=LEFT)
        given_theta_ddot = MathTex('\\ddot{\\theta}=3\\,\\mathrm{rad/s^2}').scale(0.7).next_to(given_theta_dot, DOWN, aligned_edge=LEFT)
        self.play(
            Write(given_theta_dot),
            Write(given_theta_ddot)
        )
        self.wait()

        #region Calculations arising from the geometry
        geom_1 = MathTex(
            'h=r\\cos(\\theta)',
            '\\Rightarrow',
            'r',
            '=',
            '\\frac{h}{\\cos(\\theta)}',
            '=',
            '0.58\\,\\mathrm{m}'
        ).scale(0.7).to_edge(UP).shift(1.25*RIGHT)
        geom_1[2:].set_color(YELLOW)
        self.play(Write(geom_1[0]))
        self.wait()
        self.play(Write(geom_1[1:]))
        self.wait()

        hlbox = SurroundingRectangle(geom_1[0], buff=0.1)
        self.play(ShowCreation(hlbox))
        self.wait()

        # First derivative
        geom_d1 = MathTex(
            '0=\\dot{r}\\cos(\\theta)-r\\sin(\\theta)\\dot{\\theta}',
            '\\Rightarrow',
            '\\dot{r}',
            '=',
            '\\frac{r\\sin(\\theta)}{\\cos(\\theta)}\\dot{\\theta}',
            '=',
            '0.67\\,\\mathrm{m/s}'
        ).scale(0.7).next_to(geom_1, DOWN, aligned_edge=LEFT)
        geom_d1[2:].set_color(YELLOW)
        self.play(FadeOut(hlbox), Write(geom_d1))
        self.wait()

        # Second derivative
        geom_d2 = MathTex(
            '0',
            '=',
            '\\ddot{r}\\cos(\\theta) - 2\\dot{r}\\sin(\\theta)\\dot{\\theta} - r\\cos(\\theta)\\dot{\\theta}^2 - r\\sin(\\theta)\\ddot{\\theta}',
            '\\Rightarrow',
            '\\ddot{r}',
            '=',
            '2\\dot{r}\\dot{\\theta}\\tan(\\theta) + r\\dot{\\theta}^2 + r\\tan(\\theta)\\ddot{\\theta}',
            '\\ddot{r}',
            '=',
            '4.85\\,\\mathrm{m/s^2}'
        ).scale(0.7).next_to(geom_d1, DOWN, aligned_edge=LEFT)
        geom_d2[-3:].set_color(YELLOW)
        geom_d2[4:].shift((geom_d2[1].get_center()+0.7*DOWN)-geom_d2[5].get_center())
        geom_d2[7:].shift((geom_d2[5].get_center()+0.7*DOWN)-geom_d2[8].get_center())
        self.play(Write(geom_d2[:7]))
        self.wait()
        self.play(Write(geom_d2[7:]))
        self.wait()

        # Cleanup
        self.play(
            FadeOut(geom_1[:2]),
            FadeOut(geom_1[4:6]),
            FadeOut(geom_d1[:2]),
            FadeOut(geom_d1[4:6]),
            FadeOut(geom_d2[:-3]),
            Transform(geom_1[-1], geom_1[-1].copy().shift(geom_1[3].get_center() - geom_1[-2].get_center())),
            Transform(geom_d1[-1], geom_d1[-1].copy().shift(geom_d1[3].get_center() - geom_d1[-2].get_center()))
        )
        self.wait()
        geom_1_result = Group(geom_1[2:4], geom_1[-1])
        geom_d1_result = Group(geom_d1[2:4], geom_d1[-1])
        geom_d2_result = Group(geom_d2[-3:])
        geom_1_result_newpos = geom_1_result.copy().to_edge(UP, buff=0.75).shift(2*LEFT)
        geom_d1_result_newpos = geom_d1_result.copy().next_to(geom_1_result_newpos, RIGHT, buff=0.75).shift(0.04*DOWN)
        geom_d2_result_newpos = geom_d2_result.copy().next_to(geom_d1_result_newpos, RIGHT, buff=0.75).shift(0.02*UP)
        self.play(
            Transform(geom_1_result, geom_1_result_newpos),
            Transform(geom_d1_result, geom_d1_result_newpos),
            Transform(geom_d2_result, geom_d2_result_newpos)
        )
        self.wait()
        #endregion

        #region Free body diagram
        p_fbd_radius = 0.25
        arrow_lengths = 1.5
        def get_particle_edge(angle, radians=False):
            if not radians:
                angle = angle * (PI/180)
            return np.array([p_fbd_radius*np.cos(angle), p_fbd_radius*np.sin(angle), 0])

        particle_fbd = Dot(
            radius=p_fbd_radius,
            color=YELLOW
        ).shift(2.5*RIGHT)
        r_dir = Line(
            start=get_particle_edge(60),
            end=get_particle_edge(60)*(arrow_lengths/p_fbd_radius),
            color=GREY
        ).shift(particle_fbd.get_center())
        r_dir_annot = MathTex('+r', color=YELLOW_B).scale(0.6).next_to(r_dir, direction=r_dir.get_unit_vector(), buff=0.1)
        theta_dir = Line(
            start=get_particle_edge(60-90),
            end=get_particle_edge(60-90)*(arrow_lengths/p_fbd_radius),
            color=GREY
        ).shift(particle_fbd.get_center())
        theta_dir_annot = MathTex('+\\theta', color=YELLOW_B).scale(0.6).next_to(theta_dir, direction=theta_dir.get_unit_vector(), buff=0.1)
        rod_force_arrow = Arrow(
            start=get_particle_edge(60+90)*(arrow_lengths/p_fbd_radius),
            end=get_particle_edge(60+90),
            color=RED,
            buff=0.0,
            stroke_width=6,
            tip_length=0.3,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(particle_fbd.get_center())
        rod_force_arrow_annot = MathTex('F_{rod}', color=RED).scale(0.7).next_to(rod_force_arrow, direction=-rod_force_arrow.get_unit_vector(), buff=0.1)
        gravity_arrow = Arrow(
            start=get_particle_edge(90)*(arrow_lengths/p_fbd_radius),
            end=get_particle_edge(90),
            color=BLUE,
            buff=0.0,
            stroke_width=6,
            tip_length=0.3,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(particle_fbd.get_center())
        gravity_arrow_annot = MathTex('Mg', color=BLUE).scale(0.7).next_to(gravity_arrow, direction=-gravity_arrow.get_unit_vector(), buff=0.1)
        slot_normal_force = Arrow(
            start=get_particle_edge(-90)*(arrow_lengths/p_fbd_radius),
            end=get_particle_edge(-90),
            color=PURPLE,
            buff=0.0,
            stroke_width=6,
            tip_length=0.3,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(particle_fbd.get_center())
        slot_normal_force_annot = MathTex('F_N', color=PURPLE).scale(0.7).next_to(slot_normal_force, direction=-slot_normal_force.get_unit_vector(), buff=0.1)

        self.play(
            FadeIn(particle_fbd),
            ShowCreation(r_dir),
            ShowCreation(theta_dir),
            Write(r_dir_annot),
            Write(theta_dir_annot)
        )
        self.wait()
        self.play(
            ShowCreation(gravity_arrow),
            Write(gravity_arrow_annot)
        )
        self.wait()
        self.play(
            ShowCreation(rod_force_arrow),
            Write(rod_force_arrow_annot)
        )
        self.wait()
        self.play(
            ShowCreation(slot_normal_force),
            Write(slot_normal_force_annot)
        )
        self.wait()

        fbd = Group(
            particle_fbd,
            r_dir,
            theta_dir,
            r_dir_annot,
            theta_dir_annot,
            gravity_arrow,
            gravity_arrow_annot,
            rod_force_arrow,
            rod_force_arrow_annot,
            slot_normal_force,
            slot_normal_force_annot
        )
        self.play(
            Transform(fbd, fbd.copy().scale(0.75).shift(5*LEFT+2*DOWN))
        )
        self.wait()
        #endregion

        #region FBD Math
        # 2nd law: radial direction
        sum_fr_0 = MathTex(
            '\\Sigma F_r',
            '=',
            'Ma_r',
            '=',
            'F_N\\cos(\\theta)',
            '-',
            'Mg\\cos(\\theta)'
        ).scale(0.7).next_to(geom_d1_result, DOWN, buff=1).shift(0.35*LEFT)
        sum_fr_1 = MathTex(
            '\\Sigma F_r',
            '=',
            'M(\\ddot{r}-r\\dot{\\theta}^2)',
            '=',
            'F_N\\cos(\\theta)',
            '-',
            'Mg\\cos(\\theta)'
        ).scale(0.7)
        sum_fr_1.shift(sum_fr_0[1].get_center() - sum_fr_1[1].get_center())
        self.play(Write(sum_fr_0))
        self.wait()
        self.play(*[ReplacementTransform(sum_fr_0[i], sum_fr_1[i]) for i in range(len(sum_fr_1))])
        self.wait()
        sum_fr_1_rearr = MathTex(
            'F_N',
            '=',
            'Mg',
            '+',
            'M\\frac{\\ddot{r}-r\\dot{\\theta}^2}{\\cos(\\theta)}',
            '=',
            '6.37\\,\\mathrm{N}'
        ).scale(0.7)
        sum_fr_1_rearr[0].set_color(YELLOW)
        sum_fr_1_rearr[-2:].set_color(YELLOW)
        sum_fr_1_rearr.shift((sum_fr_1[1].get_center()+0.9*DOWN)-sum_fr_1_rearr[1].get_center())
        self.play(Write(sum_fr_1_rearr[:5]))
        self.wait()
        self.play(Write(sum_fr_1_rearr[5:]))
        self.wait()
        ansbox1 = SurroundingRectangle(sum_fr_1_rearr, buff=0.1)
        self.play(ShowCreation(ansbox1))
        self.wait()

        # 2nd law: theta direction
        sum_ft_0 = MathTex(
            '\\Sigma F_\\theta',
            '=',
            'Ma_\\theta',
            '=',
            'F_{rod}',
            '-',
            'F_N\\sin(\\theta)',
            '+',
            'Mg\\sin(\\theta)'
        ).scale(0.7).next_to(sum_fr_1_rearr, DOWN, aligned_edge=LEFT, buff=0.5).shift(0.15*LEFT)
        sum_ft_1 = MathTex(
            '\\Sigma F_\\theta',
            '=',
            'M(r\\ddot{\\theta}+2\\dot{r}\\dot{\\theta})',
            '=',
            'F_{rod}',
            '-',
            'F_N\\sin(\\theta)',
            '+',
            'Mg\\sin(\\theta)'
        ).scale(0.7)
        sum_ft_1.shift(sum_ft_0[1].get_center() - sum_ft_1[1].get_center())
        self.play(Write(sum_ft_0))
        self.wait()
        self.play(*[ReplacementTransform(sum_ft_0[i], sum_ft_1[i]) for i in range(len(sum_ft_1))])
        self.wait()
        sum_ft_1_rearr = MathTex(
            'F_{rod}',
            '=',
            '(F_N-Mg)\\sin(\\theta)',
            '+',
            'M(r\\ddot{\\theta}+2\\dot{r}\\dot{\\theta})',
            '=',
            '2.93\\,\\mathrm{N}'
        ).scale(0.7)
        sum_ft_1_rearr[0].set_color(YELLOW)
        sum_ft_1_rearr[-2:].set_color(YELLOW)
        sum_ft_1_rearr.shift((sum_ft_1[1].get_center()+0.9*DOWN)-sum_ft_1_rearr[1].get_center())
        self.play(Write(sum_ft_1_rearr[:5]))
        self.wait()
        self.play(Write(sum_ft_1_rearr[5:]))
        self.wait()
        ansbox1 = SurroundingRectangle(sum_ft_1_rearr, buff=0.1)
        self.play(ShowCreation(ansbox1))
        self.wait()
        #endregion