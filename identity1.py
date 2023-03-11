from manim import *

FONT_SIZE = 24

class myScene(Scene):
    def construct(self):
        refNumber = 5
        refSquare = refNumber * refNumber
        totalNumbers = 4
        numberToInclude = [refSquare - i*i for i in range(totalNumbers + 1)]

        axes = Axes(
            x_range=[0, 28],
            axis_config={
                "numbers_to_include": numberToInclude,
                "font_size": FONT_SIZE}
            )

        
        self.add(axes)
        self.play(axes.animate)


        for i in range(1, totalNumbers+1):
            # Formula
            formula = MathTex("{}*{}".format(refNumber-i, refNumber+i), font_size=FONT_SIZE)
            formula.move_to([axes.c2p(refSquare-i*i, 0.5, 0)])
            self.add(formula)
            self.play(formula.animate)

            # Curly Brace
            gap = Brace(Line(start=[0, 0, 0], end=[i*i/2, 0, 0]), sharpness=1).set_color(GREEN_B)
            gap.move_to([axes.c2p(refSquare-i*i/2, -i, 0)])

            # Distance number
            text = Text(str(i*i), font_size=FONT_SIZE)
            text.next_to(gap, DOWN)
            self.add(gap, text)
            self.play(Create(VGroup(gap, text)))


