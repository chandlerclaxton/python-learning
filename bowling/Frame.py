class Frame(object):
	def __init__(self, *args):
		self.totalScore = 0
		self.firstThrow = 0
		if args[0] > 10:
			args[0] = 10

		self.firstThrow = args[0]

		try:
			args[1]
		except IndexError:
			self.secondThrow = 0
		else:
			self.secondThrow = args[1]

		try:
			args[2]
		except IndexError:
			self.thirdThrow = 0
		else:
			self.thirdThrow = args[2]

	def getScore(self):
		return self.firstThrow + self.secondThrow + self.thirdThrow

	def isStrike(self):
		return self.firstThrow == 10

	def isSpare(self):
		return self.firstThrow != 10 and self.secondThrow > 10

#MyFrame = Frame(4, 5)
#print MyFrame.firstThrow
			
		
