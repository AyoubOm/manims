from manim import *

FONT_SIZE = 32

class SquareMinusOne(Scene):
	def construct(self):
		size = 5
		smallSize = 3

		sideLength = 0.6
		xShift = -1
		yShift = 1.5


		# Formula
		nSquareTex = MathTex(r'{ n }^{ 2 }', font_size=FONT_SIZE)
		nSquareTex.move_to([sideLength*2 + xShift - 4, 1 + yShift, 0])

		self.play(Create(nSquareTex))
		self.wait()

		squares = []

		# Draw Squares
		for i in range(size):
			for j in range(size):
				square = Square(side_length=sideLength, color=BLUE, fill_opacity=0.8)
				square.move_to([sideLength*j + xShift, -sideLength*i + yShift, 0])
				squares.append(square)

		vgroup = VGroup(*squares)

		self.play(Create(vgroup))
		self.wait()

		# continue on formula
		minusTex = MathTex(r'-', font_size=FONT_SIZE)
		minusTex.next_to(nSquareTex, RIGHT)

		oneTex = MathTex(r'1', font_size=FONT_SIZE)
		oneTex.next_to(minusTex, RIGHT)
		
		self.play(Create(minusTex), Create(oneTex))


		# move one square
		self.play(squares[size-1].animate.shift(UP).shift(RIGHT))
		self.wait()

		# equal
		equalTex = MathTex(r'=', font_size=FONT_SIZE)
		equalTex.next_to(oneTex, RIGHT)
		self.play(Create(equalTex))


		for line in range(1, size):
			self.play(squares[line*size + size-1].animate.next_to(squares[size * (size-1) + line - 1], DOWN, 0))

		# Result tex
		resultTex = MathTex(r'({ n } - { 1 })({ n } + { 1 })', font_size=FONT_SIZE)
		resultTex.next_to(equalTex, RIGHT)
		
		self.play(Create(resultTex))

		self.wait()
