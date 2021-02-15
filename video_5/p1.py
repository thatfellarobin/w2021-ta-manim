from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
BROWN = '#8f4a04'

class T5P1(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
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
        diagram_full.shift(2.5*DOWN)

        self.add(diagram_full)
        self.wait()
        #endregion

        #region From A's perspective

        #endregion

        #region From B's perspective

        #endregion

