from manim import *

class Squares(Scene):
	def construct(self):
		size = 5
		sideLength = 0.6

		squares = []

		for i in range(size):
			for j in range(size):
				square = Square(side_length=sideLength, color=BLUE, fill_opacity=0.8)
				square.move_to([sideLength*j-1, 1.5-sideLength*i, 0])
				squares.append(square)

		vgroup = VGroup(*squares)

		self.play(Create(vgroup))
		self.wait()

		smallSize = 3
		smallVgroup = VGroup()
		for i in range(smallSize):
			for j in range(size-smallSize, size):
				smallVgroup.add(squares[i*size + j])

		self.play(smallVgroup.animate.set_opacity(0.3), run_time=1.6)
		self.play(FadeOut(smallVgroup), run_time=1.5)
		self.remove(*smallVgroup)
		self.wait()

		remainingSmallGroup = VGroup()
		for i in range(smallSize, size):
			for j in range(size-smallSize, size):
				remainingSmallGroup.add(squares[i*size + j])

		self.play(Rotate(remainingSmallGroup, angle=PI/2), run_time=1)
		self.play(remainingSmallGroup.animate.move_to([sideLength-1.3, 1.5-sideLength*6, 0]), run_time=1)
		self.wait()


		