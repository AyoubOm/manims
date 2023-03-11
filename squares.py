from manim import *

FONT_SIZE = 32

class Squares(Scene):
	def construct(self):
		size = 5
		smallSize = 3

		sideLength = 0.6
		xShift = -1
		yShift = 1.5

		squares = []

		# Big Square formula
		bigSquareTex = MathTex(r'{ 5 }\times{ 5 }', font_size=FONT_SIZE)
		bigSquareTex.move_to([sideLength*2 + xShift, 1.5 + yShift, 0])

		self.play(Create(bigSquareTex))
		self.wait()


		# Draw Squares
		for i in range(size):
			for j in range(size):
				square = Square(side_length=sideLength, color=BLUE, fill_opacity=0.8)
				square.move_to([sideLength*j + xShift, -sideLength*i + yShift, 0])
				squares.append(square)

		vgroup = VGroup(*squares)

		self.play(Create(vgroup))
		self.wait()



		smallVgroup = VGroup()
		for i in range(smallSize):
			for j in range(size-smallSize, size):
				smallVgroup.add(squares[i*size + j])


		# small square braces
		lengthBrace = Brace(smallVgroup, direction=UP).set_color(GREEN_B)
		widthBrace = Brace(smallVgroup, direction=RIGHT).set_color(GREEN_B)

		braceVgroup = VGroup(lengthBrace, widthBrace)
		for brace in [lengthBrace, widthBrace]:
			smallSizeTex = MathTex(r'{ 3 }', font_size=FONT_SIZE-2)
			smallSizeTex.next_to(brace, brace.get_direction())
			if brace == lengthBrace:
				smallSizeTex.shift(LEFT*(sideLength*3/2))
			else:
				smallSizeTex.shift(UP*(sideLength*3/2))
			braceVgroup.add(smallSizeTex)


		self.add(braceVgroup)
		self.play(Create(braceVgroup))


		# Fade out small group
		self.play(smallVgroup.animate.set_opacity(0.3), run_time=1.6)
		self.play(FadeOut(smallVgroup), run_time=1.5)
		self.remove(*smallVgroup)
		self.wait()

		# Move remaining small group
		remainingSmallGroup = VGroup()
		for i in range(smallSize, size):
			for j in range(size-smallSize, size):
				remainingSmallGroup.add(squares[i*size + j])

		self.play(Rotate(remainingSmallGroup, angle=PI/2), run_time=1)
		self.play(remainingSmallGroup.animate.move_to([sideLength-1.3, 1.5-sideLength*6, 0]), run_time=1)
		self.wait()

		# Move and transform braces
		self.play(ScaleInPlace(widthBrace, (size/smallSize + 1)))
		self.play(widthBrace.animate.shift(DOWN*sideLength*2.4).shift(LEFT*sideLength*2.8))
		