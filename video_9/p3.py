from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

DSCALE = 2/3




class T9P3(Scene):
    def number_equation(self, eq, n, color=YELLOW_B):
        num = MathTex('\\textbf{' + str(n) + '}', color=color).scale(0.5)
        circle = Circle(
            color=color,
            radius=0.225,
            arc_center=num.get_center()
        )
        line = Line(
            start=circle.get_edge_center(LEFT),
            end=circle.get_edge_center(LEFT)+0.5*LEFT,
            color=color
        )
        group = Group(num, circle, line)
        group.next_to(eq, RIGHT, buff=0.25)
        self.play(FadeIn(group))
        return group


    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Diagram objects
        wheel_main = Circle(
            radius=DSCALE*1.6,
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1,
            stroke_width=9
        )
        wheel_line1 = Line(
            start=wheel_main.get_edge_center(DOWN),
            end=wheel_main.get_edge_center(UP),
            color=BLUE_E
        )
        wheel_line2 = Line(
            start=wheel_main.get_edge_center(LEFT),
            end=wheel_main.get_edge_center(RIGHT),
            color=BLUE_E
        )
        wheel_inner = Circle(
            radius=DSCALE*0.8,
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1,
            stroke_width=12
        )
        wheel = Group(
            wheel_main,
            wheel_line1,
            wheel_line2,
            wheel_inner
        )

        conveyor_belt = Line(
            start=wheel.get_edge_center(DOWN)+2*LEFT,
            end=wheel.get_edge_center(DOWN)+4*RIGHT,
            color=GREY,
            stroke_width=10
        ).shift(0.05*DOWN)
        conveyor_tick = Line(
            start=conveyor_belt.get_start(),
            end=conveyor_belt.get_start()+0.15*DOWN,
            color=GREY,
            stroke_width=8
        )
        conveyor_length = conveyor_belt.get_length()
        num_ticks = 20
        tickspace = conveyor_length / num_ticks
        conveyor_ticks = Group(
            conveyor_tick,
            *[conveyor_tick.copy().shift(tickspace*(i+1)*RIGHT) for i in range(num_ticks)]
        )
        conveyor = Group(conveyor_belt, conveyor_ticks)

        string = Line(
            start=wheel_inner.get_edge_center(DOWN),
            end=wheel_inner.get_edge_center(DOWN)+4*RIGHT,
            color=YELLOW_A,
            stroke_width=10
        )
        string_tie = Line(
            start=string.get_end()+0.3*UP,
            end=string.get_end()+0.3*DOWN,
            color=GREY,
            stroke_width=15
        )

        self.add(
            conveyor,
            wheel_main,
            wheel_line1,
            wheel_line2,
            string_tie
        )
        self.add_foreground_mobjects(string,wheel_inner)
        self.wait()
        #endregion


        #region Animate movement
        # I tried updaters at first but they don't seem to work well for groups.
        # I could have made it work but I decided to try it this way instead
        conveyor_initpos = conveyor.get_center()
        wheel_initpos = wheel.get_center()
        wheel_init = wheel.copy()
        string_init = string.copy()
        string_init_start = string.get_start()
        string_init_end = string.get_end()

        duration = 3
        timestep = 1/60 #FIXME: Must match frametime. (1/15) for low quality, (1/60) for high quality.
        conveyor_movement=1.5
        for t in np.arange(start=0, stop=duration, step=timestep):
            a_conv = (conveyor_movement*2)/(duration**2)

            conveyor_pos = conveyor_initpos + LEFT*(0.5)*a_conv*t**2

            string_displacement = (np.linalg.norm(conveyor_pos-conveyor_initpos) / ((1.6/0.8)-1)) * RIGHT
            wheel_pos = wheel_initpos + string_displacement # New position of the wheel
            angle = np.linalg.norm(string_displacement) / (DSCALE*0.8) # Rotation of the wheel

            newstring = Line(
                start=string_init_start+string_displacement,
                end=string_init_end,
                color=YELLOW_A,
                stroke_width=10
            )

            self.play(
                Transform(conveyor, conveyor.copy().move_to(conveyor_pos), rate_func=linear, run_time=timestep),
                Transform(wheel, wheel_init.copy().rotate_in_place(-angle).move_to(wheel_pos), rate_func=linear, run_time=timestep),
                Transform(string, newstring, rate_func=linear, run_time=timestep)
            )
        self.wait()
        #endregion

        self.remove_foreground_mobjects(wheel_inner)
        self.add(wheel_inner)

        self.play(
            Transform(wheel, wheel_init),
            Transform(conveyor, conveyor.copy().move_to(conveyor_initpos)),
            Transform(string, string_init)
        )
        self.wait()
        self.play(
            FadeOut(conveyor),
            FadeOut(string),
            FadeOut(string_tie)
        )
        self.wait()


        #region Build fbd
        fbd_mg_arrow = Arrow(
            start=wheel.get_center()+1.5*UP,
            end=wheel.get_center(),
            color=BLUE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_mg_label = MathTex('Mg', color=BLUE).scale(0.7).next_to(fbd_mg_arrow, UP, buff=0.1)
        fbd_FN_arrow = Arrow(
            start=wheel.get_edge_center(DOWN)+DOWN,
            end=wheel.get_edge_center(DOWN),
            color=PURPLE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_FN_label = MathTex('F_N', color=PURPLE).scale(0.7).next_to(fbd_FN_arrow, DOWN, buff=0.1)
        fbd_T_arrow = Arrow(
            start=wheel_inner.get_edge_center(DOWN),
            end=wheel_inner.get_edge_center(DOWN)+1.5*RIGHT,
            color=MAROON,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_T_label = MathTex('T', color=MAROON).scale(0.7).next_to(fbd_T_arrow, RIGHT, buff=0.1)
        fbd_Ff_arrow = Arrow(
            start=wheel.get_edge_center(DOWN),
            end=wheel.get_edge_center(DOWN)+1.5*LEFT,
            color=MAROON,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_Ff_label = MathTex('F_{fs}', color=MAROON).scale(0.7).next_to(fbd_Ff_arrow, LEFT, buff=0.1)

        fbd_ax_arrow = Arrow(
            start=wheel.get_center(),
            end=wheel.get_center()+1.5*RIGHT,
            color=RED,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_ax_label = MathTex('a_x', color=RED).scale(0.7).next_to(fbd_ax_arrow, RIGHT, buff=0.1)
        fbd_aC_arrow = Arrow(
            start=wheel.get_edge_center(DOWN),
            end=wheel.get_edge_center(DOWN)+LEFT,
            color=RED,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        fbd_aC_label = MathTex('a_C', color=RED).scale(0.7).next_to(fbd_aC_arrow.get_end(), DOWN, buff=0.15)

        self.play(
            FadeIn(fbd_mg_arrow),
            Write(fbd_mg_label),
            FadeIn(fbd_FN_arrow),
            Write(fbd_FN_label),
            FadeIn(fbd_T_arrow),
            Write(fbd_T_label),
            FadeIn(fbd_Ff_arrow),
            Write(fbd_Ff_label)
        )
        self.wait()
        self.play(
            FadeIn(fbd_ax_arrow),
            Write(fbd_ax_label),
            FadeIn(fbd_aC_arrow),
            Write(fbd_aC_label)
        )
        self.wait()

        fbd = Group(
            wheel,
            fbd_mg_arrow,
            fbd_mg_label,
            fbd_FN_arrow,
            fbd_FN_label,
            fbd_T_arrow,
            fbd_T_label,
            fbd_Ff_arrow,
            fbd_Ff_label,
            fbd_ax_arrow,
            fbd_ax_label,
            fbd_aC_arrow,
            fbd_aC_label
        )
        self.play(Transform(fbd, fbd.copy().to_corner(DOWN+RIGHT, buff=0.75)))
        self.wait()
        #endregion

        #region FBD relations
        fbd_y_eq = MathTex(
            '\\Sigma F_y = 0',
            '=',
            'F_N - Mg',
            '\\Rightarrow',
            'F_N = Mg'
        ).scale(0.6).to_corner(UP+LEFT, buff=0.75)
        self.play(Write(fbd_y_eq[:3]))
        self.wait(0.5)
        self.play(Write(fbd_y_eq[3:]))
        self.wait()
        self.play(
            FadeOut(fbd_y_eq[:-1]),
            Transform(fbd_y_eq[-1], fbd_y_eq[-1].copy().to_corner(UP+LEFT, buff=0.75))
        )

        fbd_x_eq = MathTex(
            '\\Sigma F_x =',
            'Ma_x',
            '=',
            'T - F_{fs}'
        ).scale(0.6).next_to(fbd_y_eq[-1], DOWN, aligned_edge=LEFT)
        fbd_x_eq_subbed = MathTex(
            '\\Sigma F_x =',
            'Ma_x',
            '=',
            'T - \\mu_sMg'
        ).scale(0.6).next_to(fbd_y_eq[-1], DOWN, aligned_edge=LEFT)
        self.play(Write(fbd_x_eq))
        self.wait()
        self.play(*[ReplacementTransform(fbd_x_eq[i], fbd_x_eq_subbed[i]) for i in range(len(fbd_x_eq))])
        self.wait()
        self.play(
            FadeOut(fbd_x_eq_subbed[0]),
            Transform(fbd_x_eq_subbed[1:], fbd_x_eq_subbed[1:].copy().next_to(fbd_y_eq[-1], DOWN, aligned_edge=LEFT))
        )
        self.number_equation(fbd_x_eq_subbed[1:], 1)
        self.wait()

        fbd_moments_eq = MathTex(
            'Mk_G^2\\alpha',
            '=',
            '\\mu_sMgr_o - Tr_i'
        ).scale(0.6).next_to(fbd_x_eq_subbed[1:], DOWN, aligned_edge=LEFT)
        self.play(Write(fbd_moments_eq))
        self.number_equation(fbd_moments_eq, 2)
        self.wait()
        #endregion

        #region Kinematic relations
        point_of_rolling = Dot(
            point=wheel_inner.get_edge_center(DOWN),
            color=YELLOW
        )
        self.play(FadeIn(point_of_rolling))
        for _ in range(2):
            self.play(Flash(point_of_rolling))
        self.wait()

        rolling_1_eq = MathTex(
            'a_x = r_i\\alpha'
        ).scale(0.6).next_to(fbd_moments_eq, DOWN, aligned_edge=LEFT)
        rolling_2_eq = MathTex(
            'a_C = (r_o - r_i)\\alpha'
        ).scale(0.6).next_to(rolling_1_eq, DOWN, aligned_edge=LEFT)
        for _ in range(2):
            self.play(Flash(wheel.get_center()))
        self.play(Write(rolling_1_eq))
        self.number_equation(rolling_1_eq, 3)
        self.wait()
        for _ in range(2):
            self.play(Flash(wheel.get_edge_center(DOWN)))
        self.play(Write(rolling_2_eq))
        self.number_equation(rolling_2_eq, 4)
        self.wait()
        #endregion

        #region Answers
        answer = MathTex(
            'T=3.13\\,\\mathrm{kN}',
            'a_x=1.34\\,\\mathrm{m/s^2}',
            'a_C=1.35\\,\\mathrm{m/s^2}',
            '\\alpha=1.68\\,\\mathrm{rad/s^2}'
        ).scale(0.6).next_to(rolling_2_eq, DOWN, buff=0.4, aligned_edge=LEFT)
        for i in range(len(answer)-1):
            answer[i+1:].next_to(answer[i], DOWN, aligned_edge=LEFT)
        for i in range(len(answer)):
            self.play(Write(answer[i]))
        ansbox = SurroundingRectangle(answer, buff=0.15)
        self.play(ShowCreation(ansbox))
        self.wait()
        #endregion