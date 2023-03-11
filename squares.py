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
		bigSquareTex.move_to([sideLength*2 + xShift - 6, 1.5 + yShift, 0])

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

		
		minusTex = MathTex(r'-', font_size=FONT_SIZE)
		minusTex.next_to(bigSquareTex, RIGHT)
		
		self.play(Create(minusTex))


		smallSquareTex = MathTex(r'{ 3 }\times{ 3 }', font_size=FONT_SIZE)
		smallSquareTex.next_to(minusTex, RIGHT)

		self.play(Create(smallSquareTex))

		smallVgroup = VGroup()
		for i in range(smallSize):
			for j in range(size-smallSize, size):
				smallVgroup.add(squares[i*size + j])


		# small square braces
		lengthBrace = Brace(smallVgroup, direction=UP).set_color(GREEN_B)
		widthBrace = Brace(smallVgroup, direction=RIGHT).set_color(GREEN_B)

		braces = [lengthBrace, widthBrace]
		braceTexts = []

		for brace in braces:
			smallSizeTex = MathTex(r'{ 3 }', font_size=FONT_SIZE-2)
			smallSizeTex.next_to(brace, brace.get_direction())
			if brace == lengthBrace:
				smallSizeTex.shift(LEFT*(sideLength*3/2))
			else:
				smallSizeTex.shift(UP*(sideLength*3/2))
			
			braceTexts.append(smallSizeTex)

		braceVgroup = VGroup(*(braces+braceTexts))



		self.add(braceVgroup)
		self.play(Create(braceVgroup))


		# Fade out small group
		self.play(smallVgroup.animate.set_opacity(0.3), run_time=1.6)
		self.play(FadeOut(smallVgroup), run_time=1.5)
		self.remove(*smallVgroup)
		self.wait()

		# Equal sign
		equalTex = MathTex(r'=', font_size=FONT_SIZE)
		equalTex.next_to(smallSquareTex, RIGHT)
		
		self.play(Create(equalTex))

		# Move remaining small group
		remainingSmallGroup = VGroup()
		for i in range(smallSize, size):
			for j in range(size-smallSize, size):
				remainingSmallGroup.add(squares[i*size + j])

		self.play(Rotate(remainingSmallGroup, angle=PI/2), run_time=1)
		self.play(remainingSmallGroup.animate.move_to([sideLength-1.3, 1.5-sideLength*6, 0]), run_time=1)
		self.wait()

		# Move and transform braces and their tex
		for (brace, braceTex) in zip(braces, braceTexts):

			if brace == widthBrace:
				self.play(ScaleInPlace(widthBrace, (size/smallSize + 1)), run_time=0.5)
				self.play(widthBrace.animate.shift(DOWN*sideLength*2.4).shift(LEFT*sideLength*2.8), run_time=0.5)
			else:
				self.play(ScaleInPlace(lengthBrace, (size-smallSize)/smallSize), run_time=0.5)
				self.play(lengthBrace.animate.shift(LEFT*sideLength*2.5), run_time=0.5)

			if brace == lengthBrace:
				text = r'{ 5 } - { 3 }'
				shiftDirection = LEFT*sideLength*1.5
			else:
				text = r'{ 5 } + { 3 }'
				shiftDirection = UP*(sideLength*(size+smallSize)/2)

			newBraceTex = MathTex(text, font_size=FONT_SIZE-2)
			newBraceTex.next_to(brace, brace.get_direction())
			newBraceTex.shift(shiftDirection)

			self.add(newBraceTex)
			self.play(FadeTransform(braceTex, newBraceTex))

		# Result tex
		resultTex = MathTex(r'({ 5 } - { 3 })({ 5 } + { 3 })', font_size=FONT_SIZE)
		resultTex.next_to(equalTex, RIGHT)
		
		self.play(Create(resultTex))
		self.wait()

		