from manim import *
import numpy as np


class AccPrimer(Scene):

    def construct(self):
        # Core objects
        path = Circle(radius=1.5, color=BLUE_B)
        particle = Dot(color=WHITE).shift(1.5*RIGHT)
        origin = Dot(color=YELLOW_A, radius=0.04)

        # Dynamic variables
        self.position = particle.get_center()
        self.oldposition = particle.get_center()
        self.vel = 0

        self.max_tllratio=0.5 # Max tip length to length ratio for arrows
        self.max_swlratio=10 # Max stroke width to length ratio
        self.arrow_scale=0.5 # Scaling the arrows cause they be beeg otherwise

        # Arrows
        acc_vector = Arrow(
            start=particle.get_center(),
            end=ORIGIN,
            buff=0,
            max_tip_length_to_length_ratio=self.max_tllratio,
            max_stroke_width_to_length_ratio=self.max_swlratio,
            color=RED
        )
        vel_vector = Arrow(
            start=particle.get_center(),
            end=particle.get_center()+UP,
            buff=0,
            max_tip_length_to_length_ratio=self.max_tllratio,
            max_stroke_width_to_length_ratio=self.max_swlratio,
            color=BLUE
        )

        # Text
        title = Tex('\\textbf{Particle velocity and centripetal accelerations}').shift(3*UP)
        vel_label = MathTex('v(t)', color=BLUE).shift(4*RIGHT + 0.5*UP)
        acc_label = MathTex('a_c(t)', color=RED).shift(4*RIGHT + 0.5*DOWN)

        # Updater functions
        def update_vel(vel, dt):
            # Update velocity
            self.position = particle.get_center()
            if abs(dt) > 0:
                self.vel = (self.position - self.oldposition) / dt
            self.oldposition = self.position

            # New arrow
            new_vel_vector = Arrow(
                start=self.position,
                end=self.position + self.arrow_scale * self.vel,
                buff=0,
                max_tip_length_to_length_ratio=self.max_tllratio,
                max_stroke_width_to_length_ratio=self.max_swlratio,
                color=BLUE
            )
            vel.become(new_vel_vector)

        def update_acc(acc):
            base = particle.get_center()
            new_acc_vector_math = self.arrow_scale * (-base / np.linalg.norm(base)) * (np.linalg.norm(self.vel)**2 / np.linalg.norm(base)) # Direction * magnitude
            new_acc_vector = Arrow(
                start=base,
                end=base+new_acc_vector_math,
                buff=0,
                max_tip_length_to_length_ratio=self.max_tllratio,
                max_stroke_width_to_length_ratio=self.max_swlratio,
                color=RED
            )
            acc.become(new_acc_vector)

        # Attach updaters
        vel_vector.add_updater(update_vel)
        acc_vector.add_updater(update_acc)

        # Run animations
        self.add(title, origin, path, acc_vector, vel_vector, particle, vel_label, acc_label)
        self.wait(0.5)
        self.play(Rotating(particle, radians=0.8*TAU, about_point=ORIGIN, rate_func=smooth),  run_time=5)
        self.wait(0.1)
        self.play(Rotating(particle, radians=-0.3*TAU, about_point=ORIGIN, rate_func=smooth), run_time=3)
        self.wait(0.1)
        self.play(Rotating(particle, radians=1*TAU, about_point=ORIGIN, rate_func=smooth), run_time=7)
        self.wait(0.1)
        self.play(Rotating(particle, radians=-0.5*TAU, about_point=ORIGIN, rate_func=smooth), run_time=3)
        self.wait()
