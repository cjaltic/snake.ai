# Game class -- a wrapper around the GUI to run game and control game variables
from Board import Board
from Painter import Painter
from Snake import Snake
from Coordinate import Coordinate
from Food import Food
class Game:
  # speed will be 0,1, or 2 with 0 being slowest and 2 being fastest
  def __init__(self, width, height, pixelSize, pieceSize, speed):

    # def __init__(self, width, height, snake, food = None):
    # create the board
    # def __init__(self, head, width, height, body = []):
    self.width = width
    self.height = height

    snake = Snake(Coordinate(3,1), width, height)
    board = Board(snake)


    # give board to the painter
    self.painter = Painter(board, width, height, pixelSize, pieceSize, speed)

  def startGame(self):
    running = True
    while running:
      self.painter.gameLoop()
      self.painter.board.resetSnake()
      running = self.painter.endGame()
      self.painter.resetScore()
  def startingSnake(self):
    return Snake(Coordinate(3,1),self.width, self.height)

if __name__ == "__main__":
  g = Game(20,20,26,22,1)
  g.startGame()