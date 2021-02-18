from manim import *
import numpy as np

MED_DARK_GREY = '#666666'
GOLD_DARK = '#4f3313'


class T5P3(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Scene objects
        block = Rectangle(
            width=2.5,
            height=1,
            color=GOLD,
            fill_color=GOLD_DARK,
            fill_opacity=1
        )
        ceiling = Line(
            start=2.5*UP+2*LEFT,
            end=2.5*UP+2*RIGHT,
            color=GREY
        )
        floor = Line(
            start=2.5*DOWN+2*LEFT,
            end=2.5*DOWN+2*RIGHT,
            color=GREY
        )

        spring_1 = Spring(
            start=0.5*UP+1*LEFT,
            end=2.5*UP+1*LEFT,
            num_coils=8,
            color=BLUE_D
        )
        spring_2 = Spring(
            start=0.5*UP+1*RIGHT,
            end=2.5*UP+1*RIGHT,
            num_coils=8,
            color=BLUE_D
        )
        spring_3 = Spring(
            start=0.5*DOWN+1*LEFT,
            end=2.5*DOWN+1*LEFT,
            num_coils=8,
            color=BLUE_D
        )
        spring_4 = Spring(
            start=0.5*DOWN+1*RIGHT,
            end=2.5*DOWN+1*RIGHT,
            num_coils=8,
            color=BLUE_D
        )

        diagram = Group(spring_1, spring_2, spring_3, spring_4, floor, ceiling, block)

        shift_amt = 4.75
        diagram.shift(shift_amt*RIGHT)

        self.add(diagram)
        self.wait()

        ref_line = Line(
            start=block.get_edge_center(LEFT)+1.25*LEFT,
            end=block.get_edge_center(RIGHT)+0.5*RIGHT,
            color=GREEN,
            stroke_opacity=0.5
        )
        ref_line_label = MathTex('s=0', color=GREEN).scale(0.7).next_to(ref_line, LEFT, buff=0.15)
        self.play(
            ShowCreation(ref_line),
            Write(ref_line_label)
        )
        self.wait()
        #endregion

        #region Animate the block
        block_home = block.get_center()

        def spring_1_updater(spring):
            translation = block.get_center()-block_home
            spring_new = Spring(
                start=0.5*UP+1*LEFT+translation,
                end=2.5*UP+1*LEFT,
                num_coils=8,
                color=BLUE_D
            ).shift(shift_amt*RIGHT)
            spring.become(spring_new)
        def spring_2_updater(spring):
            translation = block.get_center()-block_home
            spring_new = Spring(
                start=0.5*UP+1*RIGHT+translation,
                end=2.5*UP+1*RIGHT,
                num_coils=8,
                color=BLUE_D
            ).shift(shift_amt*RIGHT)
            spring.become(spring_new)
        def spring_3_updater(spring):
            translation = block.get_center()-block_home
            spring_new = Spring(
                start=0.5*DOWN+1*LEFT+translation,
                end=2.5*DOWN+1*LEFT,
                num_coils=8,
                color=BLUE_D
            ).shift(shift_amt*RIGHT)
            spring.become(spring_new)
        def spring_4_updater(spring):
            translation = block.get_center()-block_home
            spring_new = Spring(
                start=0.5*DOWN+1*RIGHT+translation,
                end=2.5*DOWN+1*RIGHT,
                num_coils=8,
                color=BLUE_D
            ).shift(shift_amt*RIGHT)
            spring.become(spring_new)

        spring_1.add_updater(spring_1_updater)
        spring_2.add_updater(spring_2_updater)
        spring_3.add_updater(spring_3_updater)
        spring_4.add_updater(spring_4_updater)

        for _ in range(10):
            self.play(Transform(block, block.copy().shift(0.75*DOWN), rate_func=rate_functions.ease_in_out_sine), run_time=0.5)
            self.play(Transform(block, block.copy().shift(0.75*UP), rate_func=rate_functions.ease_in_out_sine), run_time=0.5)
        # finish off by having the block in the lower position
        self.play(Transform(block, block.copy().shift(0.75*DOWN), rate_func=rate_functions.ease_in_out_sine), run_time=0.5)
        self.wait()

        # label s_max
        s_max_line = Line(
            start=block.get_edge_center(LEFT)+1*LEFT,
            end=block.get_center(),
            color=GREEN,
            stroke_opacity=0.5
        )
        s_max_arrow_1 = Arrow(
            start=ref_line.get_start()+0.5*RIGHT+0.5*UP,
            end=ref_line.get_start()+0.5*RIGHT,
            color=GREEN,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        s_max_arrow_2 = Arrow(
            start=ref_line.get_start()+0.5*RIGHT+1.25*DOWN,
            end=ref_line.get_start()+0.5*RIGHT+0.75*DOWN,
            color=GREEN,
            buff=0.0,
            stroke_width=5,
            tip_length=0.2,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        s_max_label = MathTex('s_{max}', color=GREEN).scale(0.7).next_to(s_max_arrow_2.get_start(), LEFT, buff=0.15)
        self.play(
            ShowCreation(s_max_line),
            Write(s_max_arrow_1),
            Write(s_max_arrow_2),
            Write(s_max_label)
            )
        self.wait()
        #endregion

        #region Math it out
        energy_0 = MathTex(
            '\\Delta W',
            '=',
            '\\Delta E_{grav}',
            '+',
            '\\Delta E_{kin}',
            '+',
            '\\Delta E_{spring}'
        ).scale(0.8).to_corner(UP+LEFT, buff=0.75).shift(0.25*LEFT)
        self.play(Write(energy_0))
        self.wait()

        energy_1 = MathTex(
            '0',
            '=',
            '-Mgs_{max}',
            '+',
            '0',
            '+',
            '2\\frac{1}{2}k(l+s_{max}-\\delta)^2', # final spring energy - upper springs
            '+',
            '2\\frac{1}{2}k(l-s_{max}-\\delta)^2', # final spring energy - lower springs
            '-',
            '4\\frac{1}{2}k(l-\\delta)^2' # initial spring energy
        ).scale(0.8)
        energy_1.shift(energy_0[1].get_center()+0.75*DOWN - energy_1[1].get_center())
        energy_1[5:].next_to(energy_1[2:5], DOWN, aligned_edge=LEFT, buff=0.3)
        energy_1[7:].next_to(energy_1[5:7], DOWN, aligned_edge=LEFT, buff=0.3)
        energy_1[9:].next_to(energy_1[7:9], DOWN, aligned_edge=LEFT, buff=0.3)
        spring_final_upper = Tex('final spring energy - upper springs', color=YELLOW).scale(0.5).next_to(energy_1[6], RIGHT, buff=0.25)
        spring_final_lower = Tex('final spring energy - lower springs', color=YELLOW).scale(0.5).next_to(energy_1[8], RIGHT, buff=0.25)
        spring_initial = Tex('initial spring energy', color=YELLOW).scale(0.5).next_to(energy_1[10], RIGHT, buff=0.25)
        self.play(Write(energy_1[:5]))
        self.wait()
        self.play(Write(energy_1[5:7]))
        self.play(Write(spring_final_upper))
        self.wait()
        self.play(Write(energy_1[7:9]))
        self.play(Write(spring_final_lower))
        self.wait()
        self.play(Write(energy_1[9:]))
        self.play(Write(spring_initial))
        self.wait()

        ans = MathTex('s_{max}=49.0\\,\\mathrm{mm}').scale(0.8)
        ansbox = SurroundingRectangle(ans, buff=0.15)
        ans_group = Group(ans, ansbox)
        ans_group.next_to(energy_1, DOWN, aligned_edge=LEFT)
        self.play(Write(ans))
        self.play(ShowCreation(ansbox))
        self.wait()
        #endregion



class Spring(VMobject):
    def __init__(self, start=LEFT, end=RIGHT,  num_coils=10, radius=0.2, parallax_factor=0.5, **kwargs):
        digest_config(self, kwargs)
        VMobject.__init__(self, **kwargs)
        self.start = start
        self.end = end

        # points per coil should be constant because otherwise,
        # transformation of a spring from one position to another
        # would not be 1:1 and it wouldn't look right.
        points_per_coil = 20
        num_subpoints = num_coils * points_per_coil

        # Spring size parameters
        length = np.linalg.norm(end-start)
        dl = length / num_subpoints
        spring_dir = (end - start) / length
        spring_angle = np.arctan2(spring_dir[1], spring_dir[0])

        total_rotations = num_coils*TAU
        dtheta = total_rotations / num_subpoints

        # starting rotation of PI/2 so that the spring touches the wall on which it's attached.
        starting_rotation = PI/2

        # Assemble spring
        for i in range(num_subpoints+1):
            base_position = dl*i*RIGHT
            base_angle = starting_rotation - dtheta*i
            tip_position = base_position + radius*np.array([parallax_factor*np.cos(base_angle), np.sin(base_angle), 0])
            if i == 0:
                self.set_points_as_corners([tip_position, tip_position])
            else:
                self.add_points_as_corners([tip_position])

        # Rotate the spring to the desired angle
        # and move it to the desired position
        self.rotate_about_origin(spring_angle)
        self.shift(start)
