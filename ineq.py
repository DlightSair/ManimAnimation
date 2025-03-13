from manim import *

class Ineq(Scene):
    def construct(self): 
        self.camera.background_color = DARKER_GRAY
        self.add_footer()
        self.intro()
        self.jensen_ineq()
        self.cauchy_schwarz_and_titu()
        self.example_jensen()
        self.example_titu()
        #self.thumbnail() 

    def add_footer(self):
        line = Line(start=[-6, -3.5, 0], end=[6, -3.5, 0], color=WHITE)
        name_left = Text("Aman Paudel", font_size=24).next_to(line, DOWN, buff=0.1).align_to(line, LEFT)
        name_right = Text("Mathematical Association of Nepal", font_size=24).next_to(line, DOWN, buff=0.1).align_to(line, RIGHT)

        self.add(line, name_left, name_right)

    def intro(self):
        text_ineq = Text("Inequalities", font_size=72).move_to([0,0.5,0])
        text_name = Text("by Aman Paudel", font_size=28).next_to(text_ineq, DOWN)
  
        self.wait(2)
        self.play(Write(text_ineq), run_time=1.5) 
        self.play(FadeIn(text_name))

        self.wait(1)
        self.play(FadeOut(text_name), run_time=0.5)
        self.play(text_ineq.animate.shift(2*UP+LEFT))
        text_cont_one = Text("- Jensen Inequality", font_size=38).next_to(text_ineq, 1.8*DOWN, aligned_edge=LEFT)
        text_cont_two = Text("- Cauchy Schwarz Inequality", font_size=38).next_to(text_cont_one, DOWN, aligned_edge=LEFT)
        text_cont_three = Text("- Titu's Lemma", font_size=38).next_to(text_cont_two, DOWN, aligned_edge=LEFT)
        text_cont_four = Text("- Problems", font_size=38).next_to(text_cont_three, DOWN, aligned_edge=LEFT)

        self.play(Write(text_cont_one))
        self.play(Write(text_cont_two))
        self.play(Write(text_cont_three))
        self.play(Write(text_cont_four))
        self.wait(2)
        

        self.play(FadeOut(text_ineq, text_cont_one, text_cont_two, text_cont_three, text_cont_four))

    def jensen_ineq(self):  

        def ln(x):  # Function f(x)
            return np.log(x)

        def one_over_x(x):
            return 1/x

        npl = NumberPlane(
        x_range=[-2,6,1],
        y_range=[-4,4,1],
        x_length=6,
        y_length=6,
        background_line_style={
            "stroke_color": LIGHT_GRAY,
            "stroke_width": 2,
            "stroke_opacity": 0.5,
        }   
        )
        rect = Rectangle(height=npl.get_height(), width=npl.get_width(), color=WHITE, fill_color=BLACK, fill_opacity=0.8)

        graph = npl.plot(
            ln,
            x_range=[np.exp(-4), 6, 0.1],  # x=e^y to fit y
            color=YELLOW,
        )

        dot_one = always_redraw(lambda: Dot(radius=0.08, color=WHITE).move_to(graph.point_from_proportion(0.2)))
        dot_two = always_redraw(lambda: Dot(radius=0.08, color=WHITE).move_to(graph.point_from_proportion(0.8)))
        line_dots = always_redraw(lambda: Line(dot_one.get_center(), dot_two.get_center(), color=BLUE))  # Line between two dots (Variable)

        text_jensen = Text("Jensen Inequality", font_size=72)

        vg_graph = VGroup(rect, npl, graph, dot_one, dot_two, line_dots)

        # Wrtie Jensen Inequality text
        self.play(Write(text_jensen))
        self.wait(1)
        self.play( 
            text_jensen.animate.to_edge(UP, buff=0.15).scale(0.6), # Move the text to top
            run_time=1
        )

        # Create the Numberplane
        self.play(FadeIn(rect))
        self.play(GrowFromCenter(npl))
        self.wait(1)

        # Plot the function ln(x)
        self.play(Create(graph), run_time=2)

        self.play(FadeIn(dot_one), FadeIn(dot_two))
        self.wait(1)
        self.play(GrowFromCenter(line_dots))

        # Moving the dot
        tracker = ValueTracker(0.2)
        dot_one.add_updater(lambda d: d.move_to(graph.point_from_proportion(tracker.get_value())))

        self.play(tracker.animate.set_value(0.99), run_time=5)
        self.wait(1)
        self.play(tracker.animate.set_value(0.34), run_time=3)
        self.wait(1)

        # Move graph to left
        self.play(vg_graph.animate.to_edge(LEFT))
        self.wait(1)

        #### Equations ####
        first_term = MathTex("f\\left(\\frac{a + b}{2}\\right)", font_size=40).next_to(npl, 5*RIGHT).shift(2*UP)
        inequality_geq = MathTex("\\geq", font_size=40).next_to(first_term, RIGHT)
        inequality_leq = MathTex("\\leq", font_size=40).next_to(first_term, RIGHT)
        second_term = MathTex("\\frac{f(a) + f(b)}{2}", font_size=40).next_to(inequality_geq, RIGHT)

        jensen_text = VGroup(first_term, inequality_geq, second_term)

        text_der_one = MathTex("\\ln\\left(\\frac{a + b}{2}\\right) \\geq \\frac{\\ln(a) + \\ln(b)}{2}", font_size=40).next_to(jensen_text, 1.5*DOWN)
        text_der_two = MathTex("\\ln\\left(\\frac{a + b}{2}\\right) \\geq \\ln\\left(\\sqrt{ab}\\right)",font_size=40).next_to(text_der_one, 1.5*DOWN)
        text_der_three = MathTex("\\frac{a + b}{2} \\geq \\sqrt{ab}",font_size=40).next_to(text_der_two, 1.5*DOWN)

        jensen_n_variables = MathTex(
            r"f\left(\frac{x_1 + x_2 + \dots + x_n}{n}\right) \leq \frac{f(x_1) + f(x_2) + \dots + f(x_n)}{n}",
            font_size=28
        ).next_to(jensen_text, 2.5*DOWN)
        weighted_jensen = MathTex(
            r"&f(w_1 x_1 + w_2 x_2 + \dots + w_n x_n) \\ &\leq w_1 f(x_1) + w_2 f(x_2) + \dots + w_n f(x_n)",
            font_size=32
        ).next_to(jensen_n_variables, 2.5*DOWN)
        weighted_jensen_c = MathTex(
            r"\text{Where, \quad} w_1  + w_2  + \dots + w_n =1",
            font_size=28
        ).next_to(weighted_jensen, DOWN)


        midpoint = (dot_one.get_center()+dot_two.get_center())/2

        dot_midpoint = Dot([midpoint[0],0,0], radius=0.05)
        line_a = always_redraw(lambda: DashedLine(
            [dot_one.get_center()[0], npl.c2p(0,0,0)[1], 0],
            dot_one.get_center(),
            dash_length=0.08,
            color=WHITE
        ))
        line_b = always_redraw(lambda: DashedLine(
            [dot_two.get_center()[0], npl.c2p(0,0,0)[1], 0],
            dot_two.get_center(),
            dash_length=0.08,
            color=WHITE
        ))
        line_to_line = DashedLine(
            [midpoint[0], npl.c2p(0,0,0)[1], 0],
            midpoint,
            dash_length=0.08,
            color=WHITE
        )
        line_to_curve = DashedLine(
            [midpoint[0], npl.c2p(0,0,0)[1], 0],
            [midpoint[0], npl.c2p(0,ln(npl.p2c(midpoint)[0]),0)[1], 0],
            dash_length=0.08,
            color=WHITE
        )

        label_a = MathTex("(a, 0)", font_size=28, color=WHITE).next_to(line_a.get_start(), 0.5*UP)
        label_b = MathTex("(b, 0)", font_size=28, color=WHITE).next_to(line_b.get_start(), 0.5*DOWN)
        label_mid_point = MathTex("\\left(\\frac{a + b}{2}, 0\\right)", font_size=28, color=WHITE).next_to(dot_midpoint.get_center(), 0.5*DOWN)


        self.play(Create(line_a), Create(line_b), run_time=1)
        self.play(Write(label_a), Write(label_b), run_time=2)
        self.play(FadeIn(dot_midpoint))
        self.play(Write(label_mid_point))
        self.wait(1)
        

        self.play(Create(line_to_curve))
        self.wait(1)
        self.play(ReplacementTransform(line_to_curve, first_term), run_time=2)
        self.wait(1)

        self.play(Create(line_to_line))
        self.wait(1)
        self.play(ReplacementTransform(line_to_line, second_term), run_time=2)
        self.wait(1)

        self.play(FadeIn(inequality_geq))
        self.wait(1)

        ## Convex Function
        graph_two = npl.plot(
            one_over_x,
            x_range=[1/4, 6, 0.1],  
            color=YELLOW,
        )

        graph.save_state() # For future restore
        inequality_geq.save_state()
    
        # Transform into Convex function and Restore
        self.play(
            Transform(graph, graph_two),
            Transform(inequality_geq, inequality_leq),
            run_time=3
        )
        self.wait(2)

        self.play(Write(jensen_n_variables))
        self.wait(2)
        self.play(Write(weighted_jensen))
        self.play(Write(weighted_jensen_c))

        self.wait(1)

        self.play(VGroup(jensen_n_variables, weighted_jensen, weighted_jensen_c).animate.shift(9*RIGHT), run_time=3)
        self.remove(jensen_n_variables, weighted_jensen, weighted_jensen_c)
        self.wait(2)
        
        self.play(
            Restore(graph),
            Restore(inequality_geq),
            run_time=3
        )
        self.wait(1)
        # Jensen to AM-GM text
        self.play(Write(text_der_one))
        self.wait(1)
        self.play(Write(text_der_two))
        self.wait(1)
        self.play(Write(text_der_three))
        self.wait(1)

        self.play(VGroup(vg_graph, jensen_text, text_der_one, text_der_two, text_der_three, text_jensen, label_mid_point, label_a, label_b,dot_midpoint, line_a, line_b).animate.shift(8*UP), run_time=3)
        self.remove(vg_graph, jensen_text, text_der_one, text_der_two, text_der_three, text_jensen, label_mid_point, label_a, label_b, line_a, line_b, dot_midpoint)
        self.wait(2)

    def cauchy_schwarz_and_titu(self):

        text_cauchy = Text("Cauchy Schwarz", font_size=72)

        npl = NumberPlane(
        x_range=[-2,6,1],
        y_range=[-2,6,1],
        x_length=6,
        y_length=6,
        background_line_style={
            "stroke_color": LIGHT_GRAY,
            "stroke_width": 2,
            "stroke_opacity": 0.5,
        }   
        )
        rect = Rectangle(height=npl.get_height(), width=npl.get_width(), color=WHITE, fill_color=BLACK, fill_opacity=0.8)
        VGroup(npl, rect).to_edge(LEFT)

        vector_v = Arrow(npl.c2p(0,0,0), npl.c2p(3,1,0), buff=-0.3, color=YELLOW) # Vector v = (3, 1)
        vector_w = Arrow(npl.c2p(0,0,0), npl.c2p(2,4,0), buff=-0.3, color=RED)   # Vector w = (2, 4)
        theta = Angle(vector_v, vector_w)

        label_v = MathTex("\\mathbf{v} = (a_1, a_2)", font_size=35, color=YELLOW).next_to(vector_v.get_end(), RIGHT)
        label_w = MathTex("\\mathbf{w} = (b_1, b_2)", font_size=35, color=RED).next_to(vector_w.get_end(), RIGHT)
        label_theta = MathTex("\\theta", font_size=35).next_to(theta.get_center(), RIGHT+UP)


        text_cs_one = MathTex("\\mathbf{v} \\cdot \\mathbf{w} = a_1 b_1 + a_2 b_2",font_size=40).next_to(npl, 8*RIGHT).shift(2*UP)
        text_cs_two = MathTex("\\|\\mathbf{v}\\| = \\sqrt{a_1^2 + a_2^2}, \\quad \\|\\mathbf{w}\\| = \\sqrt{b_1^2 + b_2^2}",font_size=40).next_to(text_cs_one, DOWN)
        text_cs_three = MathTex("\\mathbf{v} \\cdot \\mathbf{w} = \\|\\mathbf{v}\\| \\|\\mathbf{w}\\| \\cos(\\theta)",font_size=40).next_to(text_cs_two, DOWN)
        text_cs_four = MathTex("(\\mathbf{v} \\cdot \\mathbf{w})^2 = (\\|\\mathbf{v}\\| \\|\\mathbf{w}\\| \\cos(\\theta))^2",font_size=40).next_to(text_cs_three, DOWN)
        text_cs_five = MathTex("(\\mathbf{v} \\cdot \\mathbf{w})^2 \\leq (\\|\\mathbf{v}\\| \\|\\mathbf{w}\\|)^2",font_size=40).next_to(text_cs_four, DOWN)
        text_cs_six = MathTex("(a_1 b_1 + a_2 b_2)^2 \\leq (a_1^2 + a_2^2)(b_1^2 + b_2^2)",font_size=40).next_to(text_cs_five, DOWN)
        text_cs_sev = MathTex("(a_1^2 + a_2^2)(b_1^2 + b_2^2) \\geq (a_1 b_1 + a_2 b_2)^2 ",font_size=40)


        # Wrtie CS Inequality text
        self.play(Write(text_cauchy))
        self.wait(2)
        self.play( 
            text_cauchy.animate.to_edge(UP, buff=0.15).scale(0.6), # Move the text to top
            run_time=2
        )
        self.wait(2)

        # Create the Numberplane
        self.play(FadeIn(rect))
        self.play(GrowFromCenter(npl))
        self.wait(2)
        
        # Add the vectors to the scene
        self.play(Create(vector_v), Create(vector_w))
        self.play(Create(theta))
        self.play(FadeIn(label_v), FadeIn(label_w), FadeIn(label_theta))
        self.wait(2)

        self.play(Write(text_cs_one))
        self.wait(1)
        self.play(Write(text_cs_two))
        self.wait(1)
        self.play(Write(text_cs_three))
        self.wait(1)
        self.play(Write(text_cs_four))
        self.wait(1)
        self.play(Write(text_cs_five))
        self.wait(1)
        self.play(Write(text_cs_six))
        self.wait(1)

        text_cs_sev.next_to(text_cauchy, 2*DOWN)
        self.play(
            VGroup(rect, npl, vector_v, vector_w, theta, label_v, label_w, label_theta).animate.shift(7*LEFT),
            ReplacementTransform(text_cs_six, text_cs_sev),
            FadeOut(VGroup(text_cs_one, text_cs_two, text_cs_three, text_cs_four, text_cs_five)),
            run_time=3
        )
        self.remove(rect, npl, vector_v, vector_w, theta, label_v, label_w, label_theta)

        self.wait(2)

        ## Titu Text
        text_titu = Text("Titu's Lemma", font_size=72).to_edge(UP, buff=0.15).scale(0.6)
        text_titu_two = MathTex("a_1 \\rightarrow \\frac{a_1}{\\sqrt{b_1}}, \\quad a_2 \\rightarrow \\frac{a_2}{\\sqrt{b_2}}, \\quad b_1 \\rightarrow \\sqrt{b_1}, \\quad b_2 \\rightarrow \\sqrt{b_2}", font_size=40).next_to(text_cs_sev, DOWN)
        text_titu_three = MathTex("\\left(\\left(\\frac{a_1}{\\sqrt{b_1}}\\right)^2 + \\left(\\frac{a_2}{\\sqrt{b_2}}\\right)^2\\right)",
            "\\left((\\sqrt{b_1})^2 + (\\sqrt{b_2})^2\\right)",
            "\\geq",
            "\\left(\\frac{a_1}{\\sqrt{b_1}} \\cdot \\sqrt{b_1} + \\frac{a_2}{\\sqrt{b_2}} \\cdot \\sqrt{b_2}\\right)^2",font_size=40).next_to(text_titu_two, DOWN)
        text_titu_four = MathTex("\\left(\\frac{a_1^2}{b_1} + \\frac{a_2^2}{b_2}\\right)", "(b_1 + b_2)", "\\geq", "(a_1 + a_2)^2",font_size=40).next_to(text_titu_three, DOWN)
        text_titu_five = MathTex("\\frac{a_1^2}{b_1} + \\frac{a_2^2}{b_2} \\geq \\frac{(a_1 + a_2)^2}{b_1 + b_2}",font_size=40).next_to(text_titu_four, DOWN)

        self.play(ReplacementTransform(text_cauchy, text_titu))
        self.wait(2)
        self.play(Write(text_titu_two), run_time=6)
        self.wait(2)
        self.play(Write(text_titu_three), run_time=3)
        self.wait(2)
        self.play(Write(text_titu_four))
        self.wait(2)
        self.play(Write(text_titu_five))
        self.wait(2)

        
        self.play(VGroup(text_titu, text_cs_sev, text_titu_two, text_titu_three, text_titu_three, text_titu_four, text_titu_five).animate.shift(8*UP), run_time=3)
        self.remove(text_titu, text_cs_sev, text_titu_two, text_titu_three, text_titu_three, text_titu_four, text_titu_five)
  
    def example_jensen(self):

        ##### THE CODE BELOW IS A TOTAL MESSS#####

        text_eg_one = Tex(r"Problem: $\frac{1}{1+ab} + \frac{1}{1+bc} + \frac{1}{1+ca} \leq \frac{3}{4}$, $a+b+c=abc$",font_size=60)
        self.play(Write(text_eg_one))
        self.wait(89)
        self.play(text_eg_one.animate.scale(0.67).shift(3.5*UP+LEFT), run_time=2)

        text_eg_two = Tex(r"$\Rightarrow \frac{1}{1+ab} + \frac{1}{1+bc} + \frac{1}{1+ca} \leq \frac{3}{4}$",font_size=40).next_to(text_eg_one, DOWN)
        text_eg_three = Tex(r"$\Rightarrow \frac{c}{c+abc} + \frac{a}{a+abc} + \frac{b}{b+abc} \leq \frac{3}{4}$",font_size=40).next_to(text_eg_two, DOWN)
        text_eg_four = Tex(r"$f(x) = \frac{x}{x + abc}$, $f''(x) < 0$ for $x > 0$, $f(x)$ is concave.",font_size=40).next_to(text_eg_three, DOWN)
        text_eg_five = Tex(r"$f(a) + f(b) + f(c) \leq 3f\left(\frac{a+b+c}{3}\right)$",font_size=40).next_to(text_eg_four, DOWN)
        text_eg_six = Tex(r"$\Rightarrow \frac{c}{c+abc} + \frac{a}{a+abc} + \frac{b}{b+abc} \leq 3f\left(\frac{a+b+c}{3}\right)$",font_size=40).next_to(text_eg_five, DOWN)
        text_eg_seven = Tex(r"$= 3 \cdot \frac{\frac{a+b+c}{3}}{\frac{a+b+c}{3} + abc}$",font_size=40).next_to(text_eg_six, DOWN, aligned_edge=LEFT).shift(4*RIGHT)
        text_eg_eight = Tex(r"$= 3 \cdot \frac{a+b+c}{a+b+c + 3abc} = 3 \cdot \frac{abc}{abc + 3abc} = \frac{3}{4}$",font_size=40).next_to(text_eg_seven, DOWN, aligned_edge=LEFT)
        text_eg_nine = Tex(r"$\frac{1}{1+ab} + \frac{1}{1+bc} + \frac{1}{1+ca} \leq \frac{3}{4}$",font_size=40).next_to(text_eg_eight, DOWN).shift(3.5*LEFT)


        self.play(Write(text_eg_two), run_time=2)
        self.wait(2)
        self.play(Write(text_eg_three), run_time=2)
        self.wait(2)
        self.play(Write(text_eg_four), run_time=2)
        self.wait(10)
        self.play(Write(text_eg_five))
        self.wait(1)
        self.play(Write(text_eg_six))
        self.wait(1)
        self.play(Write(text_eg_seven))
        self.wait(1)
        self.play(Write(text_eg_eight))
        self.wait(1)
        self.play(Write(text_eg_nine))
        self.wait(1)

        self.play(VGroup(text_eg_one, text_eg_two, text_eg_three, text_eg_four, text_eg_five, text_eg_six, text_eg_seven, text_eg_eight, text_eg_nine).animate.shift(10*UP), run_time=4)
        self.remove(text_eg_one, text_eg_two, text_eg_three, text_eg_four, text_eg_five, text_eg_six, text_eg_seven, text_eg_eight, text_eg_nine)

    def example_titu(self):

        ##### THE CODE BELOW IS A TOTAL MESSS#####

        prob_titu = Tex(r"Nesbitt's Inequality: $\frac{a}{b+c} + \frac{b}{c+a} + \frac{c}{a+b} \geq \frac{3}{2}$",font_size=60)
        self.play(Write(prob_titu))
        self.wait(2)
        self.play(prob_titu.animate.scale(0.67).shift(3.5*UP+LEFT), run_time=2)

        step_one_eg = Tex(r"$\Rightarrow \frac{a^2}{a(b+c)} + \frac{b^2}{b(c+a)} + \frac{c^2}{c(a+b)}$",font_size=40).next_to(prob_titu, DOWN).shift(0.5*RIGHT)
        step_two_eg = Tex(r"Titu's Lemma: $ \frac{a^2}{a(b+c)} + \frac{b^2}{b(c+a)} + \frac{c^2}{c(a+b)} \geq \frac{(a+b+c)^2}{2(ab+bc+ca)}$",font_size=40).next_to(step_one_eg, DOWN)
        step_three_eg = Tex(r"$= \frac{a^2 + b^2 + c^2+2(ab+bc+ca)}{2(ab+bc+ca)}$",font_size=40).next_to(step_two_eg, DOWN)
        step_four_eg = Tex(r"AM-GM: $\frac{a^2 + b^2}{2} \geq ab$, $\frac{b^2 + c^2}{2} \geq bc$, $\frac{c^2 + a^2}{2} \geq ca$",font_size=40).next_to(step_three_eg, DOWN)
        step_five_eg = Tex(r"$a^2 + b^2 + c^2 \geq ab + bc + ca$",font_size=40).next_to(step_four_eg, DOWN)
        step_five_eg_2 = Tex(r"$a^2 + b^2 + c^2 \geq ab + bc + ca$",font_size=40).next_to(step_three_eg, DOWN)
        step_six_eg = Tex(r"$ \frac{a^2 + b^2 + c^2+2(ab+bc+ca)}{2(ab+bc+ca)} \geq \frac{ab+bc+ca + 2(ab+bc+ca)}{2(ab+bc+ca)}$",font_size=40).next_to(step_four_eg, DOWN)
        step_seven_eg = Tex(r"$=\frac{3(ab+bc+ca)}{2(ab+bc+ca)} = \frac{3}{2}$",font_size=40).next_to(step_six_eg, DOWN).shift(2.2*RIGHT)
        step_eight_eg = Tex(r"$\frac{a}{b+c} + \frac{b}{c+a} + \frac{c}{a+b} \geq \frac{3}{2}$",font_size=40).next_to(step_seven_eg, DOWN).shift(2.2*LEFT)


        self.play(Write(step_one_eg), run_time=2)
        self.wait(2)
        self.play(Write(step_two_eg), run_time=3)
        self.wait(2)
        self.play(Write(step_three_eg))
        self.wait(2)
        self.play(Write(step_four_eg), run_time=3)
        self.wait(2)
        self.play(Write(step_five_eg), run_time=3)
        self.wait(2)
        self.play(ReplacementTransform(VGroup(step_four_eg, step_five_eg), step_five_eg_2))
        self.wait(1)
        self.play(Write(step_six_eg))
        self.wait(1)
        self.play(Write(step_seven_eg))
        self.wait(1)
        self.play(Write(step_eight_eg))
        self.wait(1)

        self.play(VGroup(prob_titu, step_one_eg, step_two_eg, step_three_eg, step_five_eg_2, step_six_eg, step_seven_eg, step_eight_eg).animate.shift(10*UP), run_time=4)
        self.remove(prob_titu, step_one_eg, step_two_eg, step_three_eg, step_five_eg_2, step_six_eg, step_seven_eg, step_eight_eg)


        bye = Text("Thank you for watching", font_size=48)
        self.play(Write(bye))
        self.wait(6)

    def thumbnail(self):

        def ln(x):  # Function f(x)
            return np.log(x)

        text_ineq = Text("Inequalities", font_size=100).move_to([0,0.5,0])
        text_name = Text("by Aman Paudel", font_size=34).next_to(text_ineq, DOWN)

        npl = NumberPlane(
        x_range=[-2,6,1],
        y_range=[-4,4,1],
        x_length=6,
        y_length=6,
        background_line_style={
            "stroke_color": LIGHT_GRAY,
            "stroke_width": 2,
            "stroke_opacity": 0.5,
        }   
        )
        rect = Rectangle(height=npl.get_height(), width=npl.get_width(), color=WHITE, fill_color=BLACK, fill_opacity=0.8)

        graph = npl.plot(
            ln,
            x_range=[np.exp(-4), 6, 0.1],  # x=e^y to fit y
            color=YELLOW,
        )

        dot_one = Dot(radius=0.08, color=WHITE).move_to(graph.point_from_proportion(0.2))
        dot_two = Dot(radius=0.08, color=WHITE).move_to(graph.point_from_proportion(0.8))
        line_dots = Line(dot_one.get_center(), dot_two.get_center(), color=BLUE) 

        midpoint = (dot_one.get_center()+dot_two.get_center())/2

        dot_midpoint = Dot([midpoint[0],0,0], radius=0.05)
        line_a = DashedLine(
            [dot_one.get_center()[0], npl.c2p(0,0,0)[1], 0],
            dot_one.get_center(),
            dash_length=0.08,
            color=WHITE
        )
        line_b = DashedLine(
            [dot_two.get_center()[0], npl.c2p(0,0,0)[1], 0],
            dot_two.get_center(),
            dash_length=0.08,
            color=WHITE
        )
        line_to_line = DashedLine(
            [midpoint[0], npl.c2p(0,0,0)[1], 0],
            midpoint,
            dash_length=0.08,
            color=WHITE
        )
        line_to_curve = DashedLine(
            [midpoint[0], npl.c2p(0,0,0)[1], 0],
            [midpoint[0], npl.c2p(0,ln(npl.p2c(midpoint)[0]),0)[1], 0],
            dash_length=0.08,
            color=WHITE
        )

        label_a = MathTex("(a, 0)", font_size=28, color=WHITE).next_to(line_a.get_start(), 0.5*UP)
        label_b = MathTex("(b, 0)", font_size=28, color=WHITE).next_to(line_b.get_start(), 0.5*DOWN)
        label_mid_point = MathTex("\\left(\\frac{a + b}{2}, 0\\right)", font_size=28, color=WHITE).next_to(dot_midpoint.get_center(), 0.5*DOWN)

        step_one_eg = Tex(r"$\Rightarrow \frac{a^2}{a(b+c)} + \frac{b^2}{b(c+a)} + \frac{c^2}{c(a+b)}$",font_size=50).shift(6*UP+5*RIGHT)
        step_two_eg = Tex(r"Titu's Lemma: $ \frac{a^2}{a(b+c)} + \frac{b^2}{b(c+a)} + \frac{c^2}{c(a+b)} \geq \frac{(a+b+c)^2}{2(ab+bc+ca)}$",font_size=50).next_to(step_one_eg, DOWN)
        step_three_eg = Tex(r"$= \frac{a^2 + b^2 + c^2+2(ab+bc+ca)}{2(ab+bc+ca)}$",font_size=50).next_to(step_two_eg, DOWN)
        step_four_eg = Tex(r"AM-GM: $\frac{a^2 + b^2}{2} \geq ab$, $\frac{b^2 + c^2}{2} \geq bc$, $\frac{c^2 + a^2}{2} \geq ca$",font_size=50).next_to(step_three_eg, DOWN)
        step_five_eg = Tex(r"$a^2 + b^2 + c^2 \geq ab + bc + ca$",font_size=50).next_to(step_four_eg, DOWN)
        step_six_eg = Tex(r"$ \frac{a^2 + b^2 + c^2+2(ab+bc+ca)}{2(ab+bc+ca)} \geq \frac{ab+bc+ca + 2(ab+bc+ca)}{2(ab+bc+ca)}$",font_size=40).next_to(step_five_eg, DOWN)
    

        text_eg_four = Tex(r"$f(x) = \frac{x}{x + abc}$, $f''(x) > 0$ for $x > 0$, $f(x)$ is concave.",font_size=40).shift(4*RIGHT)
        text_eg_five = Tex(r"$f(a) + f(b) + f(c) \leq 3f\left(\frac{a+b+c}{3}\right)$",font_size=40).next_to(text_eg_four, DOWN)
        text_eg_six = Tex(r"$\Rightarrow \frac{c}{c+abc} + \frac{a}{a+abc} + \frac{b}{b+abc} \leq 3f\left(\frac{a+b+c}{3}\right)$",font_size=40).next_to(text_eg_five, DOWN)
        text_eg_seven = Tex(r"$= 3 \cdot \frac{\frac{a+b+c}{3}}{\frac{a+b+c}{3} + abc}$",font_size=40).next_to(text_eg_six, DOWN, aligned_edge=LEFT).shift(4*RIGHT)
 

        self.add(VGroup(rect, npl, graph, dot_one, dot_two, line_dots, dot_midpoint, line_a, line_b, line_to_curve, line_to_line, label_a, label_b, label_mid_point).to_edge(LEFT, buff=0.1).set_opacity(0.35))
        self.add(VGroup(text_eg_four, text_eg_five, text_eg_six, text_eg_seven, step_five_eg, step_four_eg, step_one_eg, step_two_eg, step_three_eg, step_six_eg).set_opacity(0.35))
        self.add(text_ineq, text_name)










        


        



            

