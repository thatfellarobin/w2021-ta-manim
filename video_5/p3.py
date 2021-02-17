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

        shift_amt = 4.5
        diagram.shift(shift_amt*RIGHT)

        self.add(diagram)
        self.wait()

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

        for _ in range(5):
            self.play(
                Transform(block, block.copy().shift(0.5*DOWN), rate_func=rate_functions.ease_in_out_sine),
            )
            self.play(
                Transform(block, block.copy().shift(0.5*UP), rate_func=rate_functions.ease_in_out_sine),
            )
            # self.play(
            #     Transform(block, block.copy().shift(0.5*UP), rate_func=rate_functions.ease_in_out_sine),
            #     Transform(spring_1, spring_1_orig, run_time=0.7, rate_func=rate_functions.ease_in_out_sine),
            #     Transform(spring_2, spring_2_orig, run_time=0.7, rate_func=rate_functions.ease_in_out_sine),
            #     Transform(spring_3, spring_3_orig, run_time=0.7, rate_func=rate_functions.ease_in_out_sine),
            #     Transform(spring_4, spring_4_orig, run_time=0.7, rate_func=rate_functions.ease_in_out_sine),
            # )
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
