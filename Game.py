# Game class -- a wrapper around the GUI to run game and control game variables
from Board import Board
from Painter import Painter
from Snake import Snake
from Coordinate import Coordinate
from Food import Food
from Computer import Computer
class Game:
  # speed will be 0,1, or 2 with 0 being slowest and 2 being fastest
  # gameMode is 0 or 1 for human or computer player
  # graphicsMode is 0 or 1 for on or off
  # graphics can only be turned off for computer player
  def __init__(self, width, height, pixelSize, pieceSize, speed, highScoreFile, gameMode=0, graphicsMode=1):
    # create the board
    # gameMode 0 for human
    # gameMode 1 for computer
    self.gameMode = gameMode

    self.graphicsMode = 1
    if self.gameMode == 1:
      self.graphicsMode = graphicsMode

    snake = Snake(Coordinate(3,1), width, height)
    self.board = Board(snake, highScoreFile)
    # width, height, highscorefile
    if self.gameMode == 0:
      # pass to computer
      Computer(width, height, highScoreFile, gameMode, graphicsMode, pixelSize, pieceSize, speed)
      # give board to the painter
      # self.painter = Painter(self.board, width, height, pixelSize, pieceSize, speed)
      # self.startGameHuman()
    else:
      self.startGameComputer()

  def startGameHuman(self):
    running = True
    while running:
      self.painter.gameLoop()
      self.painter.board.resetSnake()
      running = self.painter.endGame()
      self.painter.resetScore()

  def startGameComputer(self):
    if self.graphicsMode == 0:
      c = Computer(self.board)
      c.runManyGames()
    else:
      # TODO :  graphics on for computer
      print("Sorry this feature has not beein implemented yet")

  def startingSnake(self):
    return Snake(Coordinate(3,1),self.width, self.height)

if __name__ == "__main__":
  g = Game(40,26,26,22,1,"hs.txt",0,0)