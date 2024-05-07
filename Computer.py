# Computer class
# use the following to create a computer for a standard human player game
# c = Computer(20,20,0,1,"hs.txt",26,22,1)
from Board import Board
from Snake import Snake
from Painter import Painter
from Coordinate import Coordinate
import random
class Computer:
  
  def __init__(self, width, height, highScoreFile = None, pixelSize = None, pieceSize = None, speed = None):
    # must inheret from abstract class Controller.py
    self.controller = None

    self.highScoreFile = highScoreFile

    self.width = width
    self.height = height

    self.pixelSize = pixelSize
    self.pieceSize = pieceSize
    self.speed = speed

  def startGame_HumanPlayer(self):
    starterSnake = Snake(Coordinate(3,1))
    board = Board(starterSnake, self.width, self.height, self.highScoreFile)
    painter = Painter(board, self.width, self.height, self.pixelSize, self.pieceSize, self.speed)
    start = True
    while start:
      game = True
      while game:
        playerInput = painter.pygameEventHandler()
        if playerInput == "UP":
          board.changeSnakeDirection(3)
        elif playerInput == "DOWN":
          board.changeSnakeDirection(1)
        elif playerInput == "RIGHT":
          board.changeSnakeDirection(0)
        elif playerInput == "LEFT":
          board.changeSnakeDirection(2)
        
        if not board.tick():
          game = False
        painter.paint()

      painter.board.resetSnake()
      running = painter.endGame()
      painter.resetScore()

  def startGame_ComputerPlayer(self):
    starterSnake = Snake(Coordinate(3,1), [])
    board = Board(starterSnake, self.width, self.height)
    count = 0

    game = True
    while game:
      count = count + 1
      controllerInput = self.randomMove()
      if controllerInput != 4:
        # print("MOVING:  ", controllerInput)
        board.changeSnakeDirection(controllerInput)
      if not board.tick():
        game = False
    # print("SCORE:  ", count)
    return count


  def randomMove(self):
    num = random.randint(0,10)
    if num > 4:
      num = 4
    return num




if __name__ == "__main__":
  # (self, width, height, gameMode, graphicsMode, highScoreFile = None, pixelSize = None, pieceSize = None, speed = None):

  # start human player game
  # c = Computer(20,20,0,1,"hs.txt",26,22,1)
  """  data = []
  condition = True
  count = 0
  while condition:
    count = count + 1
    c = Computer(20,20,1,0)
    data.append(c.startGame_ComputerPlayer())
    if 400 < max(data):
      condition = False
  print(max(data))
  print(count)
  """

  c = Computer(20,20,"hs.txt",26,22,1)
  c.startGame_HumanPlayer()

  # c = Computer(20,20,1,0)



