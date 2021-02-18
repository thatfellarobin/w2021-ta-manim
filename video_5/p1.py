from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'

class T5P1(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region diagram objects
        block = Rectangle(
            width=1.75,
            height=1,
            color=GOLD,
            fill_color=GOLD_DARK,
            fill_opacity=1
        )
        force_arrow = Arrow(
            start=block.get_edge_center(LEFT)+1.25*LEFT,
            end=block.get_edge_center(LEFT),
            color=RED,
            buff=0.0,
            stroke_width=8,
            tip_length=0.3,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        force_label = MathTex('F', color=RED).scale(0.8).next_to(force_arrow, LEFT, buff=0.15)
        ground = Line(
            start=7*LEFT,
            end=7*RIGHT,
            color=GREY
        ).next_to(block, DOWN, buff=0.02)

        tree_leaf_points = [
            ORIGIN,
            0.15*RIGHT + 0.4*DOWN,
            0.15*LEFT + 0.4*DOWN
        ]
        tree_leaves = Polygon(
            *tree_leaf_points,
            fill_color=EVERGREEN,
            fill_opacity=0.6,
            stroke_opacity=0
        )
        tree_stump = Line(
            start=tree_leaves.get_edge_center(DOWN),
            end=tree_leaves.get_edge_center(DOWN) + 0.2*DOWN,
            color=BROWN,
            stroke_width=9.0,
            stroke_opacity=0.6
        )
        tree = Group(tree_leaves, tree_stump)
        tree.next_to(ground, UP, buff=0).shift(2*LEFT)
        trees = Group(*[tree.copy().shift(i*1.25*RIGHT) for i in range(10)])

        diagram_block = Group(block, force_arrow, force_label)
        diagram_block.shift(3.5*LEFT)

        diagram_full = Group(ground, trees, diagram_block)
        diagram_full.shift(2*DOWN)

        self.add(diagram_full)
        self.wait()
        #endregion

        # copy some stuff for later
        block_initpos = block.copy().set_opacity(0.3)
        diagram_block_B = diagram_block.copy()

        #region From A's perspective
        d_arrow = DoubleArrow(
            start=ORIGIN,
            end=7.5*RIGHT,
            color=BLUE,
            buff=0.0,
            stroke_width=8,
            tip_length=0.3,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(block.get_edge_center(LEFT)).shift(DOWN)
        d_label = MathTex('d', color=BLUE).scale(0.8).next_to(d_arrow, DOWN)

        self.play(Transform(diagram_block, diagram_block.copy().shift(7.5*RIGHT), rate_func=rate_functions.ease_in_quad, run_time=2))
        self.play(FadeIn(block_initpos))
        self.wait()
        self.play(
            FadeIn(d_arrow),
            Write(d_label)
        )
        self.wait()

        energy_0 = MathTex(
            '\\Delta W',
            '=',
            '\\Delta E_g',
            '+',
            '\\Delta E_k'
        ).scale(0.9).to_edge(UP, buff=1)
        energy_1 = MathTex(
            'Fd',
            '=',
            '\\frac{1}{2}M(v_{1A}^2-v_0^2)'
        ).scale(0.9)
        energy_1.shift(energy_0[1].get_center()-energy_1[1].get_center())
        self.play(Write(energy_0))
        self.wait()
        self.play(ReplacementTransform(energy_0[:2], energy_1[:2]))
        self.wait()
        self.play(FadeOut(energy_0[2:4]))
        self.play(ReplacementTransform(energy_0[4], energy_1[2]))
        self.wait()
        v1A = MathTex('v_{1A} = 6.08\\,\\mathrm{m/s}').scale(0.9).next_to(energy_1, DOWN, buff=0.75)
        hlbox_v1A = SurroundingRectangle(v1A, buff=0.15)
        self.play(Write(v1A))
        self.play(ShowCreation(hlbox_v1A))
        # cleanup
        v1A_group = Group(v1A, hlbox_v1A)
        self.wait()
        self.play(
            FadeOut(energy_1),
            Transform(v1A_group, v1A_group.copy().to_corner(UP+RIGHT), buff=0.75)
        )
        self.wait()
        #endregion

        #region time of travel
        distance_eq = MathTex(
            'd',
            '=',
            'v_0t',
            '+',
            '\\frac{1}{2}at^2',
        ).scale(0.8).to_corner(UP+LEFT, buff=1)
        distance_eq_subbed = MathTex(
            'd',
            '=',
            'v_0t',
            '+',
            '\\frac{1}{2}\\frac{F}{M}t^2',
            '\\Rightarrow',
            't = 1.80\\,\\mathrm{s}'
        ).scale(0.8)
        distance_eq_subbed.shift(distance_eq[1].get_center()-distance_eq_subbed[1].get_center())
        self.play(Write(distance_eq))
        self.wait()
        self.play(*[ReplacementTransform(distance_eq[i], distance_eq_subbed[i]) for i in range(len(distance_eq))])
        self.wait()
        self.play(Write(distance_eq_subbed[-2:]))
        hlbox_t = SurroundingRectangle(distance_eq_subbed[-1], buff=0.15)
        self.play(ShowCreation(hlbox_t))
        self.wait()
        # cleanup
        self.play(FadeOut(distance_eq_subbed[:-1]))
        t_group = Group(distance_eq_subbed[-1], hlbox_t)
        self.play(Transform(t_group, t_group.copy().next_to(v1A_group, DOWN, aligned_edge=RIGHT)))
        self.wait()
        #endregion

        #region From B's perspective
        self.play(
            FadeOut(block_initpos),
            FadeOut(d_arrow),
            FadeOut(d_label),
            Transform(diagram_block, diagram_block_B)
        )
        self.wait()
        # Animate the block moving forward in B's frame
        self.play(
            Transform(trees, trees.copy().shift(3*LEFT), rate_func=linear, run_time=2),
            Transform(diagram_block, diagram_block.copy().shift(4.75*RIGHT), rate_func=rate_functions.ease_in_quad, run_time=2)
        )
        self.wait()
        self.play(FadeIn(block_initpos))
        self.wait()
        d_arrow = DoubleArrow(
            start=block_initpos.get_edge_center(LEFT),
            end=block.get_edge_center(LEFT),
            color=BLUE,
            buff=0.0,
            stroke_width=8,
            tip_length=0.3,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        ).shift(DOWN)
        d_label = MathTex('d^\\prime', color=BLUE).scale(0.8).next_to(d_arrow, DOWN)
        d_relate = MathTex('d^\\prime<d').scale(0.8).next_to(d_label, RIGHT, buff=1)
        self.play(
            FadeIn(d_arrow),
            Write(d_label)
        )
        self.wait()
        self.play(Write(d_relate))

        # Calculate d prime
        distance_prime_eq = MathTex(
            'd',
            '=',
            'v_0t',
            '+',
            '\\frac{1}{2}at^2',
        ).scale(0.8).to_corner(UP+LEFT, buff=1)
        distance_prime_eq_subbed = MathTex(
            'd^\\prime',
            '=',
            '(v_0-v_B)t',
            '+',
            '\\frac{1}{2}\\frac{F}{M}t^2',
            '\\Rightarrow',
            'd^\\prime = 6.39\\,\\mathrm{m}'
        ).scale(0.8)
        distance_prime_eq_subbed.shift(distance_prime_eq[1].get_center()+1*DOWN-distance_prime_eq_subbed[1].get_center())
        self.play(Write(distance_prime_eq))
        self.wait()
        self.play(Write(distance_prime_eq_subbed[:-2]))
        self.wait()
        self.play(Write(distance_prime_eq_subbed[-2:]))
        hlbox_d_prime = SurroundingRectangle(distance_prime_eq_subbed[-1], buff=0.15)
        self.play(ShowCreation(hlbox_d_prime))
        self.wait()

        # Energy equations
        energy_0B = MathTex(
            '\\Delta W',
            '=',
            '\\Delta E_g',
            '+',
            '\\Delta E_k'
        ).scale(0.8).next_to(distance_prime_eq_subbed, DOWN, aligned_edge=LEFT, buff=0.75)
        energy_1B = MathTex(
            'Fd^\\prime',
            '=',
            '\\frac{1}{2}Mv_{1B}^2 - \\frac{1}{2}M(v_0-v_B)^2'
        ).scale(0.8)
        energy_1B.shift(energy_0B[1].get_center()-energy_1B[1].get_center())
        self.play(Write(energy_0B))
        self.wait()
        self.play(ReplacementTransform(energy_0B[:2], energy_1B[:2]))
        self.wait()
        self.play(FadeOut(energy_0B[2:4]))
        self.play(ReplacementTransform(energy_0B[4], energy_1B[2]))
        self.wait()
        v1B = MathTex('v_{1B} = 4.08\\,\\mathrm{m/s}').scale(0.9).next_to(energy_1B, DOWN, aligned_edge=LEFT, buff=0.5)
        hlbox_v1B = SurroundingRectangle(v1B, buff=0.15)
        self.play(Write(v1B))
        self.play(ShowCreation(hlbox_v1B))
        self.wait()
        #endregion




