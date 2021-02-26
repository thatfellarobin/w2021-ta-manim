from manim import *
import numpy as np

GOLD_DARK = '#5c4326'
EVERGREEN = '#077319'
BROWN = '#8f4a04'
MED_DARK_GREY = '#666666'
BLUE_E_DARK = '#0c343d'

T1 = 1800
t1 = 3
t0 = 2.48
graph_yscale = 2.5/T1
graph_xscale = 1

class T6P1(Scene):
    def construct(self):
        attribution = Tex('Robin Liu, 2021', color=MED_DARK_GREY).scale(0.4).to_corner(DOWN+RIGHT, buff=0.2)
        self.add(attribution)

        #region physical diagram objects
        Log = Rectangle(
            width=2,
            height=1,
            color=BROWN,
            fill_color=GOLD_DARK,
            fill_opacity=1
        )
        Log_label = MathTex('M').move_to(Log.get_center())
        string_log = Line(
            start=Log.get_edge_center(RIGHT),
            end=Log.get_edge_center(RIGHT) + 1*RIGHT,
            color=YELLOW_A
        )
        pulley_outer = Circle(
            radius=0.25,
            arc_center=string_log.get_end(),
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1.0,
            stroke_width=10.0
        )
        pulley_center = Circle(
            radius=0.1,
            arc_center=pulley_outer.get_center(),
            color=BLUE_E,
            fill_color=BLUE_E_DARK,
            fill_opacity=1.0,
            stroke_width=5.0
        )
        pulley = Group(pulley_outer, pulley_center)
        string_upper = Line(
            start=pulley.get_edge_center(UP),
            end=pulley.get_edge_center(UP)+1.5*RIGHT,
            color=YELLOW_A
        )
        tension_arrow = Arrow(
            start=string_upper.get_end(),
            end=string_upper.get_end()+RIGHT,
            color=BLUE,
            buff=0.0,
            stroke_width=8,
            tip_length=0.3,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        tension_label = MathTex('T', color=BLUE).scale(0.8).next_to(tension_arrow, RIGHT, buff=0.15)
        string_lower = Line(
            start=pulley.get_edge_center(DOWN),
            end=pulley.get_edge_center(DOWN)+1.25*RIGHT,
            color=YELLOW_A
        )
        string_fix = Line(
            start=ORIGIN,
            end=0.5*UP,
            color=GREY
        ).move_to(string_lower.get_end())
        ground = Line(
            start=Log.get_edge_center(DOWN)+2*LEFT,
            end=string_fix.get_start(),
            color=GREY
        )

        Diagram = Group(
            ground,
            string_upper,
            string_lower,
            string_fix,
            pulley,
            string_log,
            Log,
            Log_label,
            tension_arrow,
            tension_label
        ).move_to(2*DOWN)
        self.add(Diagram)
        self.wait()
        #endregion

        #region graph objects
        def pathfunction_T_p1(t):
            return np.array([graph_xscale*t, graph_yscale*T1*(t/t1)**2, 0])
        def pathfunction_T_p2(t):
            return np.array([graph_xscale*t, graph_yscale*T1, 0])

        yaxis = Line(
            start=ORIGIN,
            end=3*UP,
            color=GREY
        )
        yaxis_label = MathTex('T(\\mathrm{N})').scale(0.8).next_to(yaxis, UP, buff=0.15)
        xaxis = Line(
            start=ORIGIN,
            end=5*RIGHT,
            color=GREY
        )
        xaxis_label = MathTex('t(\\mathrm{s})').scale(0.8).next_to(xaxis, RIGHT, buff=0.15)
        graphfunc_1 = ParametricFunction(
            function=pathfunction_T_p1,
            t_min=0,
            t_max=t1,
            fill_opacity=0,
            color=BLUE
        )
        graphfunc_2 = ParametricFunction(
            function=pathfunction_T_p2,
            t_min=t1,
            t_max=t1+2,
            fill_opacity=0,
            color=BLUE
        )
        graphfunc_label = MathTex('T=T_1\\left(\\frac{t}{t_1}\\right)^2', color=BLUE).scale(0.8).next_to(graphfunc_2.get_end(), RIGHT, buff=0.15)
        T1_line = Line(
            start=2.5*UP,
            end=graphfunc_1.get_end(),
            color=GOLD,
            stroke_width=5,
            stroke_opacity=0.6
        )
        T1_label = MathTex('T1', color=GOLD).scale(0.8).next_to(T1_line, LEFT, buff=0.15)
        t1_line = Line(
            start=3*RIGHT,
            end=graphfunc_1.get_end(),
            color=GOLD,
            stroke_width=5,
            stroke_opacity=0.6
        )
        t1_label = MathTex('t_1', color=GOLD).scale(0.8).next_to(t1_line, DOWN, buff=0.15)

        Graph = Group(
            yaxis,
            yaxis_label,
            xaxis,
            xaxis_label,
            graphfunc_1,
            graphfunc_2,
            graphfunc_label,
            T1_line,
            T1_label,
            t1_line,
            t1_label
        ).move_to(UP)
        self.play(
            ShowCreation(yaxis),
            ShowCreation(xaxis),
            Write(yaxis_label),
            Write(xaxis_label)
        )
        self.wait()
        self.play(ShowCreation(graphfunc_1, run_time=0.5))
        self.play(ShowCreation(graphfunc_2, run_time=0.5))
        self.play(Write(graphfunc_label))
        self.wait()
        self.play(
            ShowCreation(T1_line),
            Write(T1_label),
            ShowCreation(t1_line),
            Write(t1_label),
        )
        self.wait()
        #endregion

        #region Animate the friction increasing until static friction is overcome
        subpath = ParametricFunction(
            function=pathfunction_T_p1,
            t_min=0,
            t_max=t0,
        ).shift(graphfunc_1.get_start())
        indicator = Dot(
            point=subpath.get_start(),
            color=YELLOW
        )
        indicator_x0 = indicator.get_center()[0]
        friction_static_arrow = Arrow(
            start=Log.get_corner(DOWN+LEFT),
            end=Log.get_corner(DOWN+LEFT) + 2*LEFT,
            color=MAROON,
            buff=0.0,
            stroke_width=8,
            tip_length=0.3,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        friction_static_label = MathTex('F_{fs}', color=MAROON).scale(0.8).next_to(friction_static_arrow.get_end(), UP+LEFT, buff=0.15)

        self.play(
            Write(friction_static_arrow),
            Write(friction_static_label)
        )
        self.wait()
        def friction_static_arrow_updater(arrow):
            arrowscale = 1.5/T1
            indicator_x = indicator.get_center()[0]
            tvalue = indicator_x - indicator_x0
            Tvalue = T1 * (tvalue/t1)**2
            newarrow = Arrow(
                start=arrow.get_start(),
                end=arrow.get_start() + 2*Tvalue*arrowscale*LEFT,
                color=MAROON,
                buff=0.0,
                stroke_width=8,
                tip_length=0.3,
                max_stroke_width_to_length_ratio=999,
                max_tip_length_to_length_ratio=1
            )
            arrow.become(newarrow)
        def tension_arrow_updater(arrow):
            arrowscale = 1.5/T1
            indicator_x = indicator.get_center()[0]
            tvalue = indicator_x - indicator_x0
            Tvalue = T1 * (tvalue/t1)**2
            newarrow = Arrow(
                start=arrow.get_start(),
                end=arrow.get_start() + Tvalue*arrowscale*RIGHT,
                color=BLUE,
                buff=0.0,
                stroke_width=8,
                tip_length=0.3,
                max_stroke_width_to_length_ratio=999,
                max_tip_length_to_length_ratio=1
            )
            arrow.become(newarrow)
        def friction_static_label_updater(label):
            label.next_to(friction_static_arrow.get_end(), UP+LEFT, buff=0.15)
        def tension_label_updater(label):
            label.next_to(tension_arrow, RIGHT, buff=0.15)

        tension_arrow.add_updater(tension_arrow_updater)
        friction_static_arrow.add_updater(friction_static_arrow_updater)
        tension_label.add_updater(tension_label_updater)
        friction_static_label.add_updater(friction_static_label_updater)
        self.wait()
        self.play(FadeIn(indicator))
        self.play(MoveAlongPath(indicator, subpath, run_time=4, rate_func=linear))
        self.wait()
        tension_arrow.clear_updaters()
        friction_static_arrow.clear_updaters()
        tension_label.clear_updaters()
        friction_static_label.clear_updaters()
        # I don't know why but removal and adding it back in fixes an animation issue where it doesn't transform with the rest of the graph
        self.remove(indicator)
        self.add(indicator)

        t0_line = Line(
            start=indicator.get_center(),
            end=np.array([indicator.get_center()[0], xaxis.get_center()[1], 0]),
            color=YELLOW
        )
        t0_label = MathTex('t_0', color=YELLOW).scale(0.8).next_to(t0_line.get_end(), DOWN, buff=0.15)
        self.play(
            ShowCreation(t0_line),
            Write(t0_label)
        )
        self.wait()

        friction_kinetic_arrow = Arrow(
            start=friction_static_arrow.get_start(),
            end=friction_static_arrow.get_start() + friction_static_arrow.get_length()*(0.4/0.5)*LEFT,
            color=RED,
            buff=0.0,
            stroke_width=8,
            tip_length=0.3,
            max_stroke_width_to_length_ratio=999,
            max_tip_length_to_length_ratio=1
        )
        friction_kinetic_label = MathTex('F_{fk}', color=RED).scale(0.8).next_to(friction_kinetic_arrow.get_end(), UP+LEFT, buff=0.15)
        self.play(
            ReplacementTransform(friction_static_arrow, friction_kinetic_arrow),
            ReplacementTransform(friction_static_label, friction_kinetic_label),
        )
        for _ in range(3):
            self.play(CircleIndicate(friction_kinetic_label))
        self.wait()

        Diagram = Group(Diagram, friction_kinetic_arrow, friction_kinetic_label)
        Graph = Group(Graph, indicator, t0_line, t0_label)
        #endregion


        Diagram_target = Diagram.copy().scale(0.8).to_corner(DOWN+LEFT, buff=0.5)
        Graph_target = Graph.copy().scale(0.6).next_to(Diagram_target, UP, aligned_edge=LEFT, buff=1)
        self.play(
            Transform(Diagram, Diagram_target),
            Transform(Graph, Graph_target)
        )
        self.wait()

