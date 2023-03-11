from manim import *

FONT_SIZE = 24

class Distances(Scene):
    def construct(self):
        refNumber = 5
        refSquare = refNumber * refNumber
        totalNumbers = 4
        numberToInclude = [refSquare - i*i for i in range(totalNumbers + 1)]

        axes = Axes(x_range=[0, 28])

        number = Text(str(refSquare), font_size=FONT_SIZE)
        number.move_to([axes.c2p(refSquare, -0.5, 0)])

        self.add(axes)
        self.play(axes.animate, number.animate)

        for i in range(1, totalNumbers+1):
            # Formula
            number = Text(str(refSquare - i*i), font_size=FONT_SIZE)
            number.move_to([axes.c2p(refSquare-i*i, -0.5, 0)])

            formula = MathTex(r'{}\times{}'.format(refNumber-i, refNumber+i), font_size=FONT_SIZE)
            formula.move_to([axes.c2p(refSquare-i*i, 0.5, 0)])


            # Curly Brace
            gap = Brace(Line(start=[0, 0, 0], end=[i*i/2, 0, 0]), sharpness=1).set_color(GREEN_B)
            gap.move_to([axes.c2p(refSquare-i*i/2, -i, 0)])

            # Distance number
            text = Text(str(i*i), font_size=18)
            text.next_to(gap, DOWN)
            self.add(formula, number, gap, text)
            self.play(Create(VGroup(formula, number, gap, text)))

            self.wait(0.5)
