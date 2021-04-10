from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
GREEN_DARK = '#2b4022'
BLUE_DARK = '#26545e'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

BALL_RADIUS = 0.75
BALL_HEIGHT = 2
BALL_OFFSET = 0.5

class T12P1(Scene):
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
        disk = Circle(
            radius=1,
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1,
            stroke_width=8
        )
        disk_hinge = Dot(
            color=BLUE_E,
            radius=0.2
        ).move_to(disk.get_center())

        string_left1 = Line(
            start=disk.get_edge_center(LEFT),
            end=disk.get_edge_center(LEFT) + 1.5*DOWN,
            color=YELLOW_A
        )
        spring = generate_spring(
            start=string_left1.get_end(),
            end=string_left1.get_end()+DOWN,
            num_coils=5.5
        )
        spring.set_color(BLUE_A)
        string_left2 = Line(
            start=spring.get_end(),
            end=spring.get_end()+0.25*DOWN,
            color=YELLOW_A
        )
        ground_left = Line(
            start=string_left2.get_end()+0.2*LEFT,
            end=string_left2.get_end()+0.2*RIGHT,
            color=GREY
        )

        string_right = Line(
            start=disk.get_edge_center(RIGHT),
            end=disk.get_edge_center(RIGHT) + 1.5*DOWN,
            color=YELLOW_A
        )
        block = Rectangle(
            width=0.75,
            height=0.75,
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1,
            stroke_width=8
        ).next_to(string_right.get_end(), DOWN, buff=0)

        fbd_objects = Group(
            string_right,
            block,
            disk,
            disk_hinge
        )
        diagram = Group(
            string_left1,
            string_left2,
            spring,
            ground_left,
            fbd_objects
        ).move_to(ORIGIN)

        self.add(diagram)
        self.wait()
        #endregion

        #region Annotate diagram
        self.play(
            FadeOut(string_left1),
            FadeOut(string_left2),
            FadeOut(spring),
            FadeOut(ground_left),
            Transform(fbd_objects, fbd_objects.copy().to_corner(DOWN+RIGHT, buff=2).shift(UP))
        )
        self.wait()
        self.play(
            FadeOut(string_right),
            Transform(block, block.copy().shift(DOWN))
        )
        self.wait()

        theta_arrow = Arc(
            start_angle=0,
            angle=3*PI/4,
            radius=1.25,
            color=YELLOW
        ).add_tip(tip_length=0.15)
        theta_arrow.move_arc_center_to(disk.get_center())
        theta_annot = MathTex('\\theta', color=YELLOW).scale(0.6).next_to(theta_arrow, UP, buff=0.15)
        spring_arrow = Arrow(
            start=disk.get_edge_center(LEFT),
            end=disk.get_edge_center(LEFT)+1.5*DOWN,
            color=RED,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        spring_annot = MathTex('F_s = -k(\\theta+\\theta_{st}) r', color=RED).scale(0.6).next_to(spring_arrow.get_end(), DOWN, buff=0.15)
        grav_arrow = Arrow(
            start=block.get_edge_center(DOWN),
            end=block.get_edge_center(DOWN)+1*DOWN,
            color=TEAL,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        grav_annot = MathTex('W_A', color=grav_arrow.get_color()).scale(0.6).next_to(grav_arrow, DOWN, buff=0.15)

        tension_arrow1 = Arrow(
            start=disk.get_edge_center(RIGHT),
            end=disk.get_edge_center(RIGHT)+1*DOWN,
            color=PURPLE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        tension_arrow2 = Arrow(
            start=block.get_edge_center(UP),
            end=block.get_edge_center(UP)+1*UP,
            color=PURPLE,
            buff=0.0,
            stroke_width=5,
            tip_length=0.15,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        tension_annot = MathTex('T', color=PURPLE).scale(0.6).move_to(np.mean([tension_arrow1.get_end(), tension_arrow2.get_end()], axis=0))

        self.play(
            Write(theta_arrow),
            Write(theta_annot),
            Write(spring_arrow),
            Write(spring_annot),
            Write(grav_arrow),
            Write(grav_annot),
            Write(tension_arrow1),
            Write(tension_arrow2),
            Write(tension_annot)
        )
        self.wait()
        #endregion

        #region Math
        tex0 = Tex('FBD for block:', color=YELLOW).scale(0.6).to_corner(UP+LEFT, buff=0.5)
        self.play(FadeIn(tex0))
        self.wait()
        tension0 = MathTex(
            'T - W_A = \\frac{W_A}{g}\\ddot{\\theta}r',
            '\\,\\Rightarrow\\,',
            'T = \\frac{W_A}{g}\\ddot{\\theta}r + W_A'
        ).scale(0.6).next_to(tex0, RIGHT)
        self.play(Write(tension0))
        self.wait()

        tex1 = Tex('FBD for Disk:', color=YELLOW).scale(0.6).next_to(tex0, DOWN, aligned_edge=LEFT).shift(0.2*DOWN)
        self.play(FadeIn(tex1))
        self.wait()
        sum_torque1 = MathTex(
            'F_s r - Tr = I_{disk}\\ddot{\\theta}'
        ).scale(0.6).next_to(tex1, RIGHT)
        self.play(Write(sum_torque1))
        self.wait()

        tex2 = Tex('Static condition:', color=YELLOW).scale(0.6).next_to(tex1, DOWN, aligned_edge=LEFT).shift(0.2*DOWN)
        self.play(FadeIn(tex2))
        self.wait()
        static = MathTex(
            '\\ddot{\\theta}=0,\\,\\theta=0',
            '\\,\\Rightarrow\\,',
            'F_s r = Tr',
            '\\,\\Rightarrow\\,',
            '-k\\theta_{st}r = W_A'
        ).scale(0.6).next_to(tex2, RIGHT)
        self.play(Write(static))
        self.wait()

        sum_torque2 = MathTex(
            '(-k(\\theta+\\theta_{st}) r)r - \\left(\\frac{W_A}{g}\\ddot{\\theta}r + W_A\\right)r = \\frac{W}{2g}r^2\\ddot{\\theta}'
        ).scale(0.6).next_to(tex2, DOWN, aligned_edge=LEFT)
        self.play(Write(sum_torque2))
        self.wait()
        sum_torque3 = MathTex(
            '-k\\theta r^2',
            '-k\\theta_{st}r^2 - W_Ar',
            '-\\frac{W_A}{g}\\ddot{\\theta}r^2',
            '='
            '\\frac{W}{2g}r^2\\ddot{\\theta}'
        ).scale(0.6).next_to(sum_torque2, DOWN, aligned_edge=LEFT)
        self.play(Write(sum_torque3))
        self.wait()
        hlbox = SurroundingRectangle(sum_torque3[1], buff=0.1)
        self.play(Create(hlbox))
        self.wait()
        self.play(
            FadeOut(sum_torque3[1]),
            FadeOut(hlbox)
        )
        self.play(
            Transform(sum_torque3[2:], sum_torque3[2:].copy().next_to(sum_torque3[0], RIGHT, buff=0.1).shift(0.05*DOWN))
        )
        self.wait()

        sum_torque_rearr = MathTex(
            '\\ddot{\\theta} + \\frac{kg}{\\frac{W}{2}+W_A}\\theta = 0'
        ).scale(0.6).next_to(sum_torque3, DOWN, aligned_edge=LEFT)
        self.play(Write(sum_torque_rearr))
        self.wait()
        self.play(
            FadeOut(sum_torque2),
            FadeOut(sum_torque3[0]),
            FadeOut(sum_torque3[2:]),
            Transform(sum_torque_rearr, sum_torque_rearr.copy().next_to(tex2, DOWN, aligned_edge=LEFT))
        )
        self.wait()
        general_vib = MathTex(
            '\\ddot{\\theta} + 2\\zeta \\omega_n\\dot{\\theta} + \\omega_n^2 \\theta = 0'
        ).scale(0.6).next_to(sum_torque_rearr, DOWN, aligned_edge=LEFT)
        self.play(Write(general_vib))
        self.wait()

        omega_solve = MathTex(
            '\\omega_n^2 = \\frac{kg}{\\frac{W}{2}+W_A}',
            '\\,\\Rightarrow\\,',
            '\\omega_n = 14.688\\,\\mathrm{rad/s}'
        ).scale(0.6).next_to(general_vib, DOWN, aligned_edge=LEFT)
        self.play(Write(omega_solve[0]))
        self.wait()
        self.play(Write(omega_solve[1:]))
        self.wait()

        period = MathTex(
            '\\tau = \\frac{2\\pi}{\\omega_n} = 0.428\\,\\mathrm{s}'
        ).scale(0.6).next_to(omega_solve, DOWN, aligned_edge=LEFT).shift(0.15*RIGHT+0.15*DOWN)
        self.play(Write(period))
        ansbox = SurroundingRectangle(period, buff=0.15)
        self.play(Create(ansbox))
        self.wait()


        #endregion

def generate_spring(start=LEFT, end=RIGHT, num_coils=10, radius=0.15):
    '''
    Create a VMObject that resembles a spring.

        Parameters:
            start = start point (numpy array)
            end = end point (numpy array)
            num_coils = total coils in the spring. must be in the form i+0.5 where i is an integer > 0
            radius = spring radius
    '''

    # points per coil should be constant because otherwise,
    # transformation of a spring from one position to another
    # would not be 1:1 and it wouldn't look right.
    points_per_coil = 30
    parallax_factor = 0.5 # between 0 and 1.

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