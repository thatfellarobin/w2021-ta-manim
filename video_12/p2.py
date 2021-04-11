from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

GLOBAL_STROKE_WIDTH = 8


class T12P2(Scene):
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
        block = Rectangle(
            width=2.5,
            height=1,
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1,
            stroke_width=GLOBAL_STROKE_WIDTH
        )
        spring = generate_spring(
            start=block.get_edge_center(UP),
            end=block.get_edge_center(UP)+2*UP
        )
        spring.set_color(WHITE)
        spring.set_stroke(width=GLOBAL_STROKE_WIDTH)

        ground_up = Line(
            start=spring.get_end()+0.5*LEFT,
            end=spring.get_end()+0.5*RIGHT,
            color=GREY,
            stroke_width=GLOBAL_STROKE_WIDTH
        )

        dampercolor = LIGHT_GREY
        damper1 = Line(
            start=block.get_edge_center(DOWN),
            end=block.get_edge_center(DOWN)+DOWN,
            color=dampercolor,
            stroke_width=GLOBAL_STROKE_WIDTH
        )
        damper2 = Line(
            start=0.2*LEFT,
            end=0.2*RIGHT,
            color=dampercolor,
            stroke_width=GLOBAL_STROKE_WIDTH
        ).move_to(damper1.get_end())
        damper3 = Line(
            start=0.3*LEFT,
            end=0.3*RIGHT,
            color=dampercolor,
            stroke_width=GLOBAL_STROKE_WIDTH
        ).move_to(damper2.get_center() + 0.25*DOWN)
        damper4 = Line(
            start=damper3.get_start(),
            end=damper3.get_start()+0.4*UP,
            color=dampercolor,
            stroke_width=GLOBAL_STROKE_WIDTH
        )
        damper5 = damper4.copy().shift(damper3.get_end()-damper4.get_start())
        damper6 = Line(
            start=damper3.get_center(),
            end=damper3.get_center()+0.5*DOWN,
            color=dampercolor,
            stroke_width=GLOBAL_STROKE_WIDTH
        )
        damper = Group(damper1, damper2, damper3, damper4, damper5, damper6)

        ground_down = Line(
            start=damper6.get_end()+0.5*LEFT,
            end=damper6.get_end()+0.5*RIGHT,
            color=GREY,
            stroke_width=GLOBAL_STROKE_WIDTH
        )

        diagram = Group(
            spring,
            damper,
            block,
            ground_up,
            ground_down
        )
        self.add(diagram)
        self.wait()

def generate_spring(start=LEFT, end=RIGHT, num_coils=5.5, radius=0.15, parallax_factor=0.5):
    '''
    Create a VMObject that resembles a spring.

        Parameters:
            start = start point (numpy array)
            end = end point (numpy array)
            num_coils = total coils in the spring. must be in the form i+0.5 where i is an integer > 0
            radius = spring radius
            parallax_factor = value between 0 and 1, inclusive. If you're looking at the spring along its axis, this is 1. if you were looking at it from the side, it's 0
    '''

    # points per coil should be constant because otherwise,
    # transformation of a spring from one position to another
    # would not be 1:1 and it wouldn't look right.
    points_per_coil = 30

    num_subpoints = int(num_coils * points_per_coil)

    if abs((num_coils - np.floor(num_coils)) - 0.5) > 0.001 or num_coils < 0:
        # num_coils not of the form i+0.5
        raise ValueError("num_coils not of the form i+0.5 where i is a positive integer")

    length = np.linalg.norm(end-start)
    dl = (length - 2*radius*parallax_factor) / num_subpoints # subtract 2 radius because the coil rotations cover an extra half rotation
    spring_dir = (end - start) / length

    total_rotations = num_coils*TAU

    dtheta = total_rotations / num_subpoints
    starting_rotation = PI

    spring = VMobject()
    for i in range(num_subpoints+1):
        base_position = RIGHT*(radius*parallax_factor + dl*i)
        base_angle = starting_rotation - dtheta*i
        tip_position = base_position + radius*np.array([parallax_factor*np.cos(base_angle), np.sin(base_angle), 0])
        if i == 0:
            spring.set_points_as_corners([tip_position, tip_position])
        else:
            spring.add_points_as_corners([tip_position])
    spring.rotate_about_origin(np.arctan2(spring_dir[1], spring_dir[0])).shift(start)
    return spring