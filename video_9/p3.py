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
            stroke_width=10
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
            stroke_width=15
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
        )
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
            start=string.get_end()+0.25*UP,
            end=string.get_end()+0.25*DOWN,
            color=DARK_GREY
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
        string_init_start = string.get_start()
        string_init_end = string.get_end()

        duration = 3
        timestep = 1/15 #FIXME: change this to 1/60 when rendering HQ
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


