# Computer class
from Board import Board
from Snake import Snake
from Painter import Painter
from Coordinate import Coordinate
import random
class Computer:
  
  def __init__(self, width, height, highScoreFile, gameMode, graphicsMode, pixelSize = None, pieceSize = None, speed = None):
    # must inheret from abstract class Controller.py
    self.controller = None

    self.highScoreFile = highScoreFile

    self.width = width
    self.height = height

    self.pixelSize = pixelSize
    self.pieceSize = pieceSize
    self.speed = speed
    
    self.gameMode = gameMode
    self.graphicsMode = graphicsMode
    # make sure graphics are on for human controller
    if self.gameMode == 0:
      self.graphicsMode = 1
    
    # create a Painter object if graphics are turned on
    if self.gameMode == 0:
      self.startGame_HumanPlayer()

    elif self.gameMode == 1:
      print("Computer")



  def startGame_HumanPlayer(self):
    starterSnake = Snake(Coordinate(3,1), self.width, self.height)
    board = Board(starterSnake, self.highScoreFile)
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



if __name__ == "__main__":
  # self, width, height, highScoreFile, gameMode, graphicsMode, pixelSize = None, pieceSize = None, speed = None
  c = Computer(20,20,"hs.txt",0,1,26,22,1)



