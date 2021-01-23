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
        self.oldvel = 0
        self.acc_tan = 0

        self.max_tllratio=0.5 # Max tip length to length ratio for arrows
        self.max_swlratio=10 # Max stroke width to length ratio
        self.arrow_scale=0.5 # Scaling the arrows cause they be beeg otherwise

        # Arrows
        vel_vector = Arrow(
            start=particle.get_center(),
            end=particle.get_center()+UP,
            buff=0,
            max_tip_length_to_length_ratio=self.max_tllratio,
            max_stroke_width_to_length_ratio=self.max_swlratio,
            color=BLUE
        )
        acc_vector = Arrow(
            start=particle.get_center(),
            end=ORIGIN,
            buff=0,
            max_tip_length_to_length_ratio=self.max_tllratio,
            max_stroke_width_to_length_ratio=self.max_swlratio,
            color=RED
        )
        acc_tan_vector = Arrow(
            start=particle.get_center(),
            end=particle.get_center()+UP,
            buff=0,
            max_tip_length_to_length_ratio=self.max_tllratio,
            max_stroke_width_to_length_ratio=self.max_swlratio,
            color=MAROON
        )

        # Text and annotations
        title = Tex('\\textbf{Particle velocity and centripetal accelerations}').shift(3*UP)
        vel_label = MathTex('v(t)', color=BLUE).shift(4.25*LEFT + 0.6*UP)
        acc_label = MathTex('a_c(t)', '=', '\\frac{v^2}{\\rho}', color=RED).next_to(vel_label, DOWN, aligned_edge=LEFT)
        acc_tan_label = MathTex('a_t(t)', color=MAROON).next_to(acc_label, DOWN, aligned_edge=LEFT)
        equation_explain = Tex('$\\rho$ is the', '\\textit{instantaneous}', 'path radius').shift(5.5*RIGHT + 0.25*UP).scale(0.9)
        equation_explain[1].set_color(YELLOW).shift(0.1*RIGHT)
        equation_explain[2].shift(0.5*DOWN).align_to(equation_explain[0], LEFT)
        rho = MathTex('\\rho').shift(0.4*RIGHT + 0.8*DOWN)
        rho_arrow = DoubleArrow(start=ORIGIN, end=[1.5/2**0.5, -1.5/2**0.5, 0], color=GREEN, buff=0.1, stroke_width = 3, max_tip_length_to_length_ratio=0.15)

        # Updater functions
        def update_vel(vel, dt):
            # Update velocity and tangential acceleration
            self.position = particle.get_center()
            if abs(dt) > 0:
                self.vel = (self.position - self.oldposition) / dt
            if abs(dt) > 0 and np.linalg.norm(self.vel) > 0:
                self.acc_tan = \
                    (self.vel / np.linalg.norm(self.vel)) * \
                    ((np.linalg.norm(self.vel) - np.linalg.norm(self.oldvel)) / dt)
            else:
                self.acc_tan = 0
            self.oldposition = self.position
            self.oldvel = self.vel

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
        def update_acc_tan(acc):
            base = particle.get_center()
            new_acc_vector = Arrow(
                start=base,
                end=base + self.arrow_scale * self.acc_tan,
                buff=0,
                max_tip_length_to_length_ratio=self.max_tllratio,
                max_stroke_width_to_length_ratio=self.max_swlratio,
                color=MAROON
            )
            acc.become(new_acc_vector)

        # Attach updaters
        vel_vector.add_updater(update_vel)
        acc_vector.add_updater(update_acc)
        # acc_tan_vector.add_updater(update_acc_tan)

        # Run animations
        self.add(title, origin, path, acc_vector, vel_vector, particle, vel_label, acc_label[0], acc_tan_label)
        self.wait(0.5)
        self.play(Rotating(particle, radians=0.8*TAU, about_point=ORIGIN, rate_func=smooth),  run_time=5)
        self.wait(0.1)
        self.play(Rotating(particle, radians=-0.55*TAU, about_point=ORIGIN, rate_func=smooth), run_time=3)
        self.wait(0.1)
        self.play(
            Rotating(particle, radians=1*TAU, about_point=ORIGIN, rate_func=smooth, run_time=6),
            Write(acc_label[1:])
        )
        self.wait(0.1)
        self.play(
            Rotating(particle, radians=-0.5*TAU, about_point=ORIGIN, rate_func=smooth, run_time=3),
            Write(equation_explain),
            Write(rho),
            ShowCreation(rho_arrow)
        )
        self.wait(0.1)
        self.play(Rotating(particle, radians=1.1*TAU, about_point=ORIGIN, rate_func=smooth), run_time=5)
        self.wait()
