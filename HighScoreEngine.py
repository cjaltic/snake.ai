# High Score Engine
class HighScoreEngine:
  def __init__(self, file):
    self.file = file
    self.highScore = self.loadScore()
  
  def checkScore(self, newScore):
    if newScore > self.highScore:
      self.saveScore(newScore)

  def loadScore(self):
    with open(self.file, "r") as file:
      return int(file.read().strip())

  def saveScore(self, newScore):
    with open(self.file, "w") as file:
      self.highScore = newScore
      file.write(str(self.highScore))

  def resetHighScore(self):
    self.saveScore(0)

