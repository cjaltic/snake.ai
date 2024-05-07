# Board class
from Snake import Snake
from Coordinate import Coordinate
from Food import Food
from HighScoreEngine import HighScoreEngine

class Board:
  def __init__(self, snake, width, height, highScoreFile = None, food = None):
    self.snake = snake
    self.food = food

    self.width = width
    self.height = height

    self.score = 0

    self.tickCount = 0

    self.highScoreEngine = None
    if highScoreFile != None:
      self.highScoreEngine = HighScoreEngine(highScoreFile)

    if self.food is None:
      self.spawnFood()

  def tick(self):
    print("X, Y:  ", self.snake.head.x, " ", self.snake.head.y)
    self.tickCount = self.tickCount + 1
    # check if the snake is alive or not
    # if snake is not alive make tick() return False
    if self.snake.head.x < 0 or self.snake.head.x > self.width - 1 or self.snake.head.y < 0 or self.snake.head.y > self.height - 1:
      return False
    if self.snake.isTouchingSelf():
      return False
    self.snake.move()
    if self.snake.head.compare(self.food.location):
      self.score = self.score + 1
      if self.highScoreEngine is not None:
        self.highScoreEngine.checkScore(self.score)
      self.snake.eat()
      self.spawnFood()
    return True

  def isSnakeAlive(self):
    return True

  def spawnFood(self):
    self.food = Food(self.width, self.height)
    while self.isFoodTouchingSnake():
      self.food = Food(self.width, self.height)

  def resetBoard(self):
    self.resetSnake()
    self.resetScore()
    self.tickCount = 0

  def resetSnake(self):
    self.snake = Snake(Coordinate(3,1))
    self.snake.length = 0
    self.snake.body = []

  def resetScore(self):
    self.score = 0

  def isFoodTouchingSnake(self):
    if self.food.location.compare(self.snake.head):
      return True
    for c in self.snake.body:
      if self.food.location.compare(c):
        return True
    return False

  def changeSnakeDirection(self, direction):
    self.snake.changeDirection(direction)