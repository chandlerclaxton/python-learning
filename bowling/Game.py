from Frame import Frame

class Game:
	def __init__(self, *args):
		self.totalScore = 0
		for Frame in args:
			self.totalScore += Frame.getScore()

	

	def getTotalScore(self):
		return self.totalScore


MyGame = Game(Frame(3, 1), Frame(4, 2), Frame(10), Frame(2, 7))
print MyGame.getTotalScore()
