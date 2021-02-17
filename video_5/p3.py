from manim import *
import numpy as np

MED_DARK_GREY = '#666666'
RED_E_DARK = '#752d27'

PIVOT_RADIUS = 0.1
BOB_RADIUS = 0.2

class T5P2(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region Scene objects
        testspring = generate_spring()
        self.add(testspring)
        self.wait()

        testspring_2 = generate_spring(start=2*DOWN+2*LEFT, end=0.5*RIGHT)

        for _ in range(5):
            self.play(Transform(testspring, testspring_2, rate_func=there_and_back, run_time=1.5))
        self.wait()
        #endregion

def generate_spring(start=LEFT, end=RIGHT, num_coils=10, radius=0.2, compression_factor=1.5):
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
    spring = VMobject()
    for i in range(num_subpoints+1):
        base_position = dl*i*RIGHT
        base_angle = starting_rotation - dtheta*i
        tip_position = base_position + radius*np.array([np.cos(base_angle)/compression_factor, np.sin(base_angle), 0])
        if i == 0:
            spring.set_points_as_corners([tip_position, tip_position])
        else:
            spring.add_points_as_corners([tip_position])

    # Rotate the spring to the desired angle
    # and move it to the desired position
    spring.rotate_about_origin(spring_angle)
    spring.shift(start)

    return spring