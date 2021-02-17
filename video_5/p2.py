from manim import *
import numpy as np

MED_DARK_GREY = '#666666'
RED_E_DARK = '#752d27'

PIVOT_RADIUS = 0.1
BOB_RADIUS = 0.2

class T5P2(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021. www.robinliu.me', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Scene objects
        position_A = 2*DOWN
        position_B = 2*LEFT
        position_C = 2*RIGHT+4*UP

        pivot = Circle(
            color=BLUE_D,
            radius=PIVOT_RADIUS,
            stroke_width=8,
            fill_color=BLUE_E,
            fill_opacity=1
        )
        pivot.shift(PIVOT_RADIUS*(RIGHT+DOWN))

        bob_A = Dot(point=position_A, color=BLUE_D, radius=BOB_RADIUS)
        bob_B = Dot(point=position_B, color=BLUE_D, radius=BOB_RADIUS)
        bob_C = Dot(point=position_C, color=BLUE_D, radius=BOB_RADIUS)


        wall = Line(
            start=2.1*RIGHT+0.5*UP,
            end=2.1*RIGHT+2.5*DOWN,
            color=GREY
        )
        tie_dot = Dot(point=2*RIGHT, radius=PIVOT_RADIUS, color=BLUE_E)
        tie_connect = Rectangle(
            width=0.1,
            height=2*PIVOT_RADIUS,
            fill_color=BLUE_E,
            fill_opacity=1,
            stroke_opacity=0
        ).next_to(tie_dot.get_center(), RIGHT, buff=0)
        tie = Group(tie_connect, tie_dot)

        string_A1 = Line(
            start=bob_A.get_edge_center(UP),
            end=pivot.get_edge_center(LEFT),
            color=YELLOW_A
        )
        string_A2 = Line(
            start=pivot.get_edge_center(UP),
            end=tie.get_center(),
            color=YELLOW_A
        )
        string_B = Line(
            start=bob_B.get_edge_center(RIGHT),
            end=pivot.get_edge_center(UP),
            color=YELLOW_A
        )
        string_C = Line(
            start=bob_C.get_edge_center(DOWN),
            end=tie_dot.get_edge_center(UP),
            color=YELLOW_A
        )

        spring = generate_spring(start=position_A+BOB_RADIUS*RIGHT, end=position_A+2.1*RIGHT, num_coils=8, radius=0.13)
        spring.set_color(TEAL_A)
        spring_plate = Line(
            start=position_A+BOB_RADIUS*RIGHT+0.2*UP,
            end=position_A+BOB_RADIUS*RIGHT+0.2*DOWN,
            color=TEAL_E,
            stroke_width=10
        ).shift(0.05*RIGHT)


        path_1 = Arc(
            radius=2,
            start_angle=-PI/2,
            angle=-PI/2,
        )
        path_2 = Arc(
            radius=4,
            start_angle=PI,
            angle=-PI/2
        ).shift(2*RIGHT)
        path = path_1.copy()
        path.add_points_as_corners(path_2.get_all_points())
        path.set_color(RED_E_DARK)

        diagram = Group(wall, string_A1, string_A2, string_B, string_C, pivot, tie, spring, spring_plate, bob_A, bob_B, bob_C, path)
        diagram.scale(0.8).to_corner(RIGHT+DOWN, buff=1)
        self.add(diagram)
        self.remove(path, string_B, string_C, bob_B, bob_C)
        # Adjusting some objects to always be in the foreground
        self.remove(bob_A, pivot)
        self.add_foreground_mobjects(bob_A, pivot)
        self.wait()
        #endregion

        # Label some things
        spring_label = MathTex('k', color=TEAL_A).scale(0.8).next_to(spring, DOWN)

        self.play(Write(spring_label))
        self.wait()
        self.play(ShowCreation(path))
        self.bring_to_back(path)
        self.wait()

        position_A_label = Tex('A', color=YELLOW_A).scale(0.8).next_to(bob_A, DOWN, buff=0.15)
        position_B_label = Tex('B', color=YELLOW_A).scale(0.8).next_to(bob_B, LEFT, buff=0.15)
        position_C_label = Tex('C', color=YELLOW_A).scale(0.8).next_to(bob_C, UP, buff=0.15)

        self.play(Write(position_A_label))
        self.wait()

        h_ref_line = Line(
            start=path.get_start()+2*LEFT,
            end=path.get_start()+3*RIGHT,
            color=PURPLE_A,
        )
        h_ref_label = MathTex('h=0', color=PURPLE_A).scale(0.8).next_to(h_ref_line, LEFT, buff=0.15)
        #endregion

        #region Energy at B
        self.play(
            FadeIn(bob_B),
            FadeIn(string_B),
            Write(position_B_label),
            Transform(bob_A, bob_A.copy().set_opacity(0.5)),
            Transform(string_A1, string_A1.copy().set_opacity(0.5))
        )
        self.wait()
        energy = MathTex(
            '\\Delta W',
            '=',
            '\\Delta E_{grav}',
            '+',
            '\\Delta E_{kin}',
            '+',
            '\\Delta E_{spring}'
        ).scale(0.75).to_corner(UP+LEFT, buff=0.75)
        spring_energy = MathTex(
            'E_{spring}=\\frac{1}{2}k\\delta^2'
        ).scale(0.75).next_to(energy, RIGHT, buff=1)
        spring_expl = Tex(
            '$\\delta$ is the deflection of the spring from its \\textit{neutral} position', color=YELLOW
        ).scale(0.5).next_to(spring_energy, DOWN, buff=0.15)
        self.play(Write(energy[:5]))
        self.wait()
        self.play(Write(energy[5:]))
        self.wait()
        self.play(Write(spring_energy))
        self.play(Write(spring_expl))
        self.wait()

        energy_equate_B = MathTex(
            '0 = Mgr - \\frac{1}{2}k_a\\delta^2'
        ).scale(0.8).next_to(energy, DOWN, aligned_edge=LEFT, buff=0.75)
        self.play(Write(energy_equate_B))
        self.wait()
        sol_B = MathTex('k_a=3.53\\,\\mathrm{kN/m}').scale(0.8).next_to(energy_equate_B, DOWN, aligned_edge=LEFT)
        ansbox_B = SurroundingRectangle(sol_B, buff=0.15)
        self.play(Write(sol_B))
        self.play(ShowCreation(ansbox_B))
        self.wait()
        #endregion

        #region Energy at C
        self.play(
            FadeIn(bob_C),
            FadeIn(string_C),
            Write(position_C_label),
            Transform(bob_B, bob_B.copy().set_opacity(0.5)),
            Transform(string_B, string_B.copy().set_opacity(0.5)),
            Transform(string_A2, string_A2.copy().set_opacity(0.5)),
            Transform(energy_equate_B, energy_equate_B.copy().set_opacity(0.5))
        )
        self.wait()
        energy_equate_C = MathTex(
            '0 = Mg3r - \\frac{1}{2}Mv_c^2 - \\frac{1}{2}k_a\\delta^2'
        ).scale(0.8).next_to(sol_B, DOWN, aligned_edge=LEFT, buff=0.75)
        self.play(Write(energy_equate_C))
        # Finding v_C
        bob_fbd = bob_B.copy().shift(2*LEFT+2*UP)
        g_vect = Arrow(
            start=bob_fbd.get_edge_center(DOWN),
            end=bob_fbd.get_edge_center(DOWN)+1.5*DOWN,
            color=BLUE,
            buff=0.0,
            stroke_width=8,
            tip_length=0.3,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(0.02*RIGHT)
        g_label = MathTex('Mg', color=BLUE).scale(0.7).next_to(g_vect.get_end(), RIGHT, buff=0.1)
        T_vect = Arrow(
            start=bob_fbd.get_edge_center(DOWN),
            end=bob_fbd.get_edge_center(DOWN)+1*DOWN,
            color=RED,
            buff=0.0,
            stroke_width=8,
            tip_length=0.3,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(0.02*LEFT)
        T_label = MathTex('T', color=RED).scale(0.7).next_to(T_vect.get_end(), LEFT, buff=0.1)
        fbd = Group(bob_fbd, g_vect, g_label, T_vect, T_label)
        self.play(FadeIn(fbd))
        self.wait()
        self.play(
            FadeOut(T_vect),
            FadeOut(T_label),
            Transform(g_vect, g_vect.copy().shift(0.02*LEFT)),
            Transform(g_label, g_label.copy().shift(0.02*LEFT))
        )
        self.wait()
        fbd_eq = MathTex(
            'M\\frac{v_C^2}{2r}=Mg',
            '\\Rightarrow v_C=\\sqrt{2gr}'
        ).scale(0.8).next_to(energy_equate_C, DOWN).shift(RIGHT)
        self.play(Write(fbd_eq[0]))
        self.wait()
        self.play(Write(fbd_eq[1]))
        self.wait()

        sol_C = MathTex('k_b=14.13\\,\\mathrm{kN/m}').scale(0.8).next_to(energy_equate_C, DOWN, aligned_edge=LEFT, buff=1.5)
        ansbox_C = SurroundingRectangle(sol_C, buff=0.15)
        self.play(Write(sol_C))
        self.play(ShowCreation(ansbox_C))
        self.wait()
        #endregion

def generate_spring(start=LEFT, end=RIGHT, num_coils=10, radius=0.2):
    '''
    Create a VMObject that resembles a spring.

        Parameters:
            start = start point (numpy array)
            end = end point (numpy array)
            num_coils = total coils in the spring (positive int)
            radius = spring radius
    '''

    # points per coil should be constant because otherwise,
    # transformation of a spring from one position to another
    # would not be 1:1 and it wouldn't look right.
    points_per_coil = 20
    num_subpoints = num_coils * points_per_coil

    length = np.linalg.norm(end-start)
    dl = length / num_subpoints
    spring_dir = (end - start) / length

    total_rotations = num_coils*TAU
    dtheta = total_rotations / num_subpoints
    starting_rotation = np.arctan2(spring_dir[1], spring_dir[0]) + PI/2

    spring = VMobject()

    for i in range(num_subpoints+1):
        base_position = start + dl*i*spring_dir
        base_angle = starting_rotation - dtheta*i
        tip_position = base_position + radius*np.array([np.cos(base_angle), np.sin(base_angle), 0])
        if i == 0:
            spring.set_points_as_corners([tip_position, tip_position])
        else:
            spring.add_points_as_corners([tip_position])

    return spring