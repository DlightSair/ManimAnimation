from manim import *

class SnC(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY
        height = 2.7
        a_length = 3.2
        b_length = 1.5
        mid_ab = (a_length+b_length)/2
        buff =0.17
        stroke = 5
        dashed_length = mid_ab*2/35

        cords = [[-mid_ab,0,0],[a_length-mid_ab,0,0], [mid_ab,0,0]]

        ### !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ###
        ### ONLY PAST ME KNOWS WHAT I WAS DOING WHEN I WROTE THE CODE BELOW ###
        ### !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ###


        def colorfun(st):
            text1 = MathTex(rf"{st}", font_size=84)
            temp = 0
            for i in list(st):
                if i == "a":
                    text1[0][temp].set(color=RED)
                if i == "b":
                    text1[0][temp].set(color=YELLOW)
                if i != " " and i != "^":
                    temp+=1
            return text1

        st = "(a+b)^2=a^2+2ab+b^2"
        text = colorfun(st)
        line_a = Line(cords[0], cords[1], color=RED, stroke_width= stroke)
        line_b = Line(cords[1], cords[2], color=YELLOW, stroke_width= stroke)
        brace_a = BraceBetweenPoints(cords[1], cords[0], buff=buff)
        brace_b = BraceBetweenPoints(cords[2], cords[1], buff=buff)
        brace_ab = BraceBetweenPoints(cords[2], cords[0], buff=buff)
        text_a = MathTex("a", font_size= 56, color=RED).next_to(brace_a, UP, buff=buff)
        text_b = MathTex("b", font_size=56, color=YELLOW).next_to(brace_b, UP, buff=buff)
        text_ab = MathTex("a","+","b", font_size=56).next_to(brace_ab, UP, buff=buff)
        text_ab[0].set(color=RED)
        text_ab[2].set(color=YELLOW)

        vis = Text("Visual interpretation of", font_size=72).move_to([0,1,0])
        text.next_to(vis, 3*DOWN)

        self.play(Write(vis))
        self.play(Write(text))
        self.play(FadeOut(text), FadeOut(vis))
        self.play(Create(line_a))
        self.play(GrowFromCenter(brace_a), Write(text_a))
        self.play(Create(line_b))
        self.play(GrowFromCenter(brace_b), Write(text_b))
        self.play(
                ReplacementTransform(VGroup(brace_a, brace_b), brace_ab),
                TransformMatchingShapes(VGroup(text_a, text_b), text_ab)
                )
        VGroup(brace_a, brace_b, text_a, text_b).shift([0,height,0])
        self.play(VGroup(line_a, line_b, brace_ab, text_ab).animate.shift([0,height,0]))

        
        line_ab = VGroup(line_a, line_b)
        line_ab2 = line_ab.copy()
        bt_ab = VGroup(brace_ab, text_ab)
        self.play(Rotate(line_ab2, angle= -np.pi/2, about_point= [-mid_ab,height,0]))
        bt_ab2 = bt_ab.copy().rotate(np.pi/2).next_to(line_ab2, LEFT, buff=buff)
        self.play(Transform(bt_ab.copy(), bt_ab2))
        self.play(FadeIn(line_ab.copy().shift([0,-mid_ab*2,0])), FadeIn(line_ab2.copy().shift([mid_ab*2,0,0])))
        text_group = VGroup(bt_ab[1], bt_ab2[1])

        blue_square = Square(side_length=mid_ab*2, stroke_width=0, fill_color=BLUE, fill_opacity=0.5).align_to(line_ab, UP)
        text_sq = MathTex("(","a","+","b",")",r"^2", font_size= 56).move_to(blue_square.get_center())
        text_sq[1].set(color=RED)
        text_sq[3].set(color=YELLOW)
        self.play(ReplacementTransform(VGroup(bt_ab[1].copy(), bt_ab2[1].copy()), text_sq), FadeIn(blue_square))
        self.wait()
        self.play(FadeOut(blue_square), text_sq.animate.next_to(blue_square, 2*DOWN))

        cords2 = [-b_length/2, a_length/2, height-a_length/2, height-a_length-b_length/2]
        dline1 = DashedLine([-mid_ab, height-a_length, 0], [mid_ab, height-a_length, 0], dash_length=dashed_length, stroke_opacity=0.9)
        dline2 = DashedLine([a_length-mid_ab, height, 0], [a_length-mid_ab, height-mid_ab*2,0], dash_length=dashed_length, stroke_opacity=0.9)
        self.play(GrowFromPoint(dline1, [-mid_ab, height-a_length, 0]), GrowFromPoint(dline2, [-mid_ab+a_length, height, 0]))
        red_square = Square(side_length=a_length, stroke_width=0, fill_color=RED, fill_opacity=0.5).move_to([cords2[0], cords2[2],0])
        yellow_square = Square(side_length=b_length, stroke_width=0, fill_color=YELLOW, fill_opacity=0.5).move_to([cords2[1], cords2[3],0])
        orange_rec1 = Rectangle(height=b_length, width=a_length, stroke_opacity=0, fill_color=GREEN, fill_opacity=0.5).move_to([cords2[0], cords2[3], 0])
        orange_rec2 = Rectangle(height=a_length, width=b_length, stroke_opacity=0, fill_color=GREEN, fill_opacity=0.5).move_to([cords2[1], cords2[2], 0])

        text_a2 = MathTex(r"a^2", font_size=56).move_to(red_square.get_center())
        text_ab1 = MathTex(r"ab", font_size=56).move_to(orange_rec1.get_center())
        text_ab2 = MathTex(r"ab", font_size=56).move_to(orange_rec2.get_center())
        text_b2 = MathTex(r"b^2", font_size=56).move_to(yellow_square.get_center())       


        self.play(FadeIn(red_square), ReplacementTransform(text_group.copy(), text_a2))
        self.play(FadeIn(yellow_square), ReplacementTransform(text_group.copy(), text_b2))
        self.play(FadeIn(orange_rec1), FadeIn(orange_rec2), ReplacementTransform(text_group.copy(), text_ab1), ReplacementTransform(text_group.copy(), text_ab2))

        self.play(text_sq.animate.shift([-3,0,0]))
        eqn = VGroup(
            MathTex(r"=", font_size=56),
            Square(side_length=0.75, stroke_width=0, fill_color=RED, fill_opacity=0.8),
            MathTex(r"+", font_size=56),
            Rectangle(height=0.75, width=0.45, stroke_opacity=0, fill_color=GREEN, fill_opacity=0.8),
            Rectangle(height=0.45, width=0.75, stroke_opacity=0, fill_color=GREEN, fill_opacity=0.8),
            MathTex(r"+", font_size=56),
            Square(side_length=0.5, stroke_width=0, fill_color=YELLOW, fill_opacity=0.8)
        ).arrange(RIGHT).next_to(text_sq, RIGHT)

        eqn_2 = MathTex("=","a^2","+","2ab","+","b^2", font_size=56).next_to(text_sq, RIGHT)
        eqn_2[1][0].set(color=RED)
        eqn_2[3][1].set(color=RED)
        eqn_2[3][2].set(color=YELLOW)
        eqn_2[5][0].set(color=YELLOW)

        self.play(Write(eqn[0]), run_time=0.3)
        self.play(ReplacementTransform(red_square.copy(), eqn[1]))
        self.play(Write(eqn[2]), run_time=0.3)
        self.play(ReplacementTransform(orange_rec2.copy(), eqn[3]), ReplacementTransform(orange_rec1.copy(), eqn[4]))
        self.play(Write(eqn[5]), run_time=0.3)
        self.play(ReplacementTransform(yellow_square.copy(), eqn[6]))
        
        self.play(Transform(eqn[1], eqn_2[1].copy().move_to(eqn[1].get_center()).shift([0,0.08,0])))
        self.play(Transform(VGroup(eqn[3], eqn[4]), eqn_2[3].copy().move_to(VGroup(eqn[3], eqn[4]).get_center())))
        self.play(Transform(eqn[6], eqn_2[5].copy().move_to(eqn[6].get_center()).shift([0,0.08,0])))

        self.wait(5)