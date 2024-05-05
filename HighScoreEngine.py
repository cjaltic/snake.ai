# High Score Engine
class HighScoreEngine:
  def __init__(self, file):
    self.file = file
    self.highScore
  
  def checkScore(self, newScore):
    if newScore > self.highScore:
      self.highScore = newScore
      self.saveScore()

  def loadScore(self):
    with open(self.file, "r") as file:
      self.highScore = int(file.read().strip())

  def saveScore(self):
    with open(self.file, "w") as file:
      file.write(str(self.highScore))

