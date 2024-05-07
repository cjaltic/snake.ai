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

  def startGame_ComputerPlayer(self, graphicsOn):
    starterSnake = Snake(Coordinate(3,0), [])
    board = Board(starterSnake, self.width, self.height, self.highScoreFile)
    count = 0
    
    if graphicsOn:
      painter = Painter(board, self.width, self.height, self.pixelSize, self.pieceSize, self.speed)

    game = True
    while game:
      if graphicsOn:
        painter.delayGame()
      count = count + 1
      controllerInput = self.sophisticatedMove(board)
      if controllerInput != 4:
        # print("X,Y:", board.snake.head.x, ",", board.snake.head.y)
        # print("MOVING:  ", controllerInput)
        board.changeSnakeDirection(controllerInput)
      if not board.tick():
        game = False
      if graphicsOn:
        painter.paint()
    # print("SCORE:  ", count)
    return board.score


  def randomMove(self):
    num = random.randint(0,10)
    if num > 4:
      num = 4
    return num


  def sophisticatedMove(self, board):
    # Corners
    if board.snake.head.x == 0 and board.snake.head.y == 0:
      if board.snake.dir == 3:
        return 0
      elif board.snake.dir == 2:
        return 1
    elif board.snake.head.x == board.width - 1 and board.snake.head.y == 0:
      if board.snake.dir == 0:
        return 1
      elif board.snake.dir == 3:
        return 2
    elif board.snake.head.x == 0 and board.snake.head.y == board.height - 1:
      if board.snake.dir == 1:
        return 0
      elif board.snake.dir == 2:
        return 3
    elif board.snake.head.x == board.width - 1 and board.snake.head.y == board.height - 1:
      if board.snake.dir == 0:
        return 3
      elif board.snake.dir == 1:
        return 2
    # Rims
    # Left
    elif board.snake.head.x == 0:
      # heading into the wall
      if board.snake.dir == 2:
        return random.choice((1,3))
      else:
        move = self.randomMove()
        if move == 2:
          return 4
        return move
    
    # Top
    elif board.snake.head.y == 0:
      if board.snake.dir == 3:
        return random.choice((0,2))
      else:
        move = self.randomMove()
        if move == 3:
          return 4
        return move

    # Right
    elif board.snake.head.x == board.width - 1:
      if board.snake.dir == 0:
        return random.choice((1,3))
      else:
        move = self.randomMove()
        if move == 0:
          return 4
        return move

    # Down
    elif board.snake.head.y == board.height - 1:
      if board.snake.dir == 1:
        return random.choice((0,2))
      else:
        move = self.randomMove()
        if move == 1:
          return 4
        return move

    else:
      return self.goToFood(board)

  def goToFood(self, board):
    if board.food.location.x > board.snake.head.x:
      return 0
    elif board.food.location.x < board.snake.head.x:
      return 2
    elif board.food.location.y > board.snake.head.y:
      return 1
    elif board.food.location.y < board.snake.head.y:
      return 3
    else:
      return self.randomMove()





if __name__ == "__main__":
  
  # (self, width, height, highScoreFile = None, pixelSize = None, pieceSize = None, speed = None):
  data = []
  while True:
    computer = Computer(20,20,"aihs.txt",26,22,1)
    data.append(computer.startGame_ComputerPlayer(True))
    print("SCORE: ", max(data))

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

  # c = Computer(20,20,"hs.txt",26,22,1)
  # c.startGame_HumanPlayer()

  # c = Computer(20,20,1,0)



