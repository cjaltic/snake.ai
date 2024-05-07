# High Score Engine
class HighScoreEngine:
  def __init__(self, hsFile):
    self.file = hsFile
    self.highScore = self.loadScore()
  
  def checkScore(self, newScore):
    if self.file is not None:
      if newScore > self.highScore:
        self.saveScore(newScore)

  def loadScore(self):
    if self.file is not None:
      with open(self.file, "r") as file:
        return int(file.read().strip())
    else:
      return 0

  def saveScore(self, newScore):
    if self.file is not None:
      with open(self.file, "w") as file:
        self.highScore = newScore
        file.write(str(self.highScore))

  def resetHighScore(self):
    self.saveScore(0)

