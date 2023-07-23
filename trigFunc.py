from manim import *

class Test(Scene):
    def construct(self): 
        self.bias_height = 0.1
        self.camera.background_color = DARKER_GRAY
        self.intro()
        self.CreateGraph()
        self.CreateCircle()
        self.do_stuffs()
        self.sin_c()
        self.cos_c()
        self.dot_mov_fi()
        self.wait(2)

    def intro(self):
        vio = Text("Visual interpretation of", font_size=72).move_to([0,1,0])
        snc = Tex(r"$\sin(\theta)$", " and ", r"$\cos(\theta)$", font_size=90).next_to(vio, 2*DOWN)
        snc[0].set(color=YELLOW)
        snc[2].set(color=BLUE)
        
        self.play(Write(vio))
        self.play(Write(snc))
        self.play(FadeOut(vio), FadeOut(snc))

    def CreateGraph(self):  # Create Graph and animate it
        npl = NumberPlane(
        x_range=[-4,4,1],
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
        self.play(FadeIn(rect))
        self.play(GrowFromCenter(npl))
        self.npl = npl
        self.rect = rect
            
    def CreateCircle(self): # Create the circle
        circle = Circle(radius=self.npl.c2p(3,3,0)[0], stroke_width=6, color=RED)
        circle.rotate(np.pi/3)  # Rotation for MoveAlongPath()
        self.play(Create(circle))
        self.circle = circle
    
    def do_stuffs(self):
        start_angle = np.pi/3
        position = self.npl.c2p(np.cos(start_angle)*3, np.sin(start_angle)*3, 0)
        dot = Dot(radius=0.08, color=WHITE).move_to([position[0], position[1],0])
        self.dot = dot

        def angle_value(): #Get angle and it's value
            angle = Angle(Line(self.npl.c2p(0,0,0), RIGHT,0), radius, radius=0.4)
            value = DecimalNumber(angle.get_value(degrees=True), unit="^{\circ}", num_decimal_places=0).scale(0.8).next_to(angle,UR, buff=0)
            return VGroup(angle, value)

        radius = always_redraw(lambda: Line(self.circle.get_center(), dot.get_center()))
        x_line = always_redraw(lambda: DashedLine(dot.get_center(), [self.npl.c2p(0,0,0)[0], dot.get_center()[1], 0], dash_length=0.1, color=BLUE, stroke_width=5))
        y_line = always_redraw(lambda: DashedLine(dot.get_center(), [dot.get_center()[0], self.npl.c2p(0,0,0)[1], 0], dash_length=0.1, color=YELLOW, stroke_width=5))
        angle_v = always_redraw(angle_value)

        self.play(FadeIn(dot), Create(radius)) # Animating Dots, Lines and Angles
        self.play(Create(x_line), Create(y_line), run_time=0.8)
        self.play(FadeIn(angle_v))

        self.play(MoveAlongPath(dot, self.circle), run_time=3.5) # Making dot go around circle

        # Sine Brace and Text
        brace_sin = BraceBetweenPoints(y_line.get_end(), y_line.get_start(), buff=0.12)
        tex_sin = MathTex(r"\sin(\theta)").set(color=YELLOW).scale(0.9).next_to(brace_sin, RIGHT, buff=0.1)
        # Cosine Brace and Text
        brace_cos = BraceBetweenPoints(x_line.get_start(), x_line.get_end(), buff=0.12)
        tex_cos = MathTex(r"\cos(\theta)").set(color=BLUE).scale(0.9).next_to(brace_cos, UP, buff=0.1)

        v_sin = VGroup(brace_sin, tex_sin)
        v_cos = VGroup(brace_cos, tex_cos)
        self.play(GrowFromCenter(v_sin))
        self.play(GrowFromCenter(v_cos))
        self.wait()

        self.allMobject = VGroup(self.rect, self.npl, self.circle, radius, x_line, y_line, angle_v, dot, v_sin, v_cos)
        self.play(self.allMobject.animate.to_edge(LEFT)) # Move all shit to left of the screen
    
    def sin_c(self): 
        sin_rect = Rectangle(height=self.rect.get_height()/2-self.bias_height, width=self.rect.get_width(), color=WHITE, fill_color=BLACK, fill_opacity=0.8).to_edge(RIGHT).align_to(self.rect, UP)
        sin_line = Line(sin_rect.get_left(), sin_rect.get_right(), stroke_opacity=0.6)
        sin_curve = FunctionGraph(lambda x: np.sin(x), x_range=[np.pi/3, 2*np.pi+np.pi/3], color=YELLOW, stroke_width=5)
        sin_curve.stretch_to_fit_width(sin_rect.get_width()-1).move_to(sin_rect.get_center())
        sin_xl = DashedLine([sin_curve.get_start()[0], sin_line.get_center()[1], 0], sin_curve.get_start(), dash_length=0.1, stroke_width=5, color=YELLOW)
        self.play(GrowFromCenter(VGroup(sin_rect, sin_line))) # Creates Rectangle

        self.sin_rect = sin_rect
        self.sin_curve = sin_curve
        self.sin_xl = sin_xl

    def cos_c(self):
        cos_rect = Rectangle(height=self.rect.get_height()/2-self.bias_height, width=self.rect.get_width(), color=WHITE, fill_color=BLACK, fill_opacity=0.8).to_edge(RIGHT).align_to(self.rect, DOWN)
        cos_line = Line(cos_rect.get_left(), cos_rect.get_right(), stroke_opacity=0.6)
        cos_curve = FunctionGraph(lambda x: np.cos(x), x_range=[np.pi/3, 2*np.pi+np.pi/3], color=BLUE, stroke_width=5)
        cos_curve.stretch_to_fit_width(cos_rect.get_width()-1).move_to(cos_rect.get_center())
        cos_yl = DashedLine([cos_curve.get_start()[0], cos_line.get_center()[1], 0], cos_curve.get_start(), dash_length=0.1, stroke_width=5, color=BLUE)
        self.play(GrowFromCenter(VGroup(cos_rect, cos_line))) # Creates Rectangele

        self.cos_rect = cos_rect
        self.cos_curve = cos_curve
        self.cos_yl = cos_yl

    def dot_mov_fi(self):
        self.play(
            ReplacementTransform(VGroup(self.allMobject[5].copy(), self.allMobject[8][0]), self.sin_xl),
            self.allMobject[8][1].animate.rotate(np.pi/2).scale(1.1).next_to(self.sin_rect, LEFT, buff=0.15)
        )
        self.play(
            ReplacementTransform(VGroup(self.allMobject[4].copy(), self.allMobject[9][0]), self.cos_yl),
            self.allMobject[9][1].animate.rotate(np.pi/2).scale(1.1).next_to(self.cos_rect, LEFT, buff=0.15)
        )

        self.play(MoveAlongPath(self.dot, self.circle), Create(self.sin_curve), Create(self.cos_curve), run_time=7)
        self.wait(2)







        














