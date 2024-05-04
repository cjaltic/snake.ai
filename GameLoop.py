# main game loop class

#  Not being used right now but don't want to delete just yet
from Painter import Painter
from Board import Board
from Snake import Snake
from Food import Food
from Coordinate import Coordinate

class GameLoop:
  def __init__(self, gui, width=20, height=20, pixelSize=26, pieceSize=22):
  	self.painter = gui

  def paintScreen(self):
  	self.painter.paint()

# (self, width, height, snake = None, food = None):
# Board
f = Food(20,20)
testSnakeStraightTop = Snake(Coordinate(4,0), 20, 20, [Coordinate(3,0), Coordinate(2,0), Coordinate(1,0), Coordinate(0,0)])

# (self, width, height, snake = None, food = None):
b = Board(20,20,testSnakeStraightTop,f)
g = Painter(b)

test = GameLoop(g)
while True:
  test.paintScreen()
