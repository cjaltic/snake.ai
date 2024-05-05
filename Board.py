# Board class
from Snake import Snake
from Coordinate import Coordinate
from Food import Food
from HighScoreEngine import HighScoreEngine

class Board:
  def __init__(self, snake, highScoreFile, food = None):
    self.snake = snake
    self.food = food
    self.score = 0

    self.highScoreEngine = HighScoreEngine(highScoreFile)

    if self.food is None:
      self.spawnFood()

  def tick(self):
    # check if the snake is alive or not
    # if snake is not alive make tick() return False
    if self.snake.head.x < 0 or self.snake.head.x > self.snake.width - 1 or self.snake.head.y < 0 or self.snake.head.y > self.snake.height - 1:
      return False
    if self.snake.isTouchingSelf():
      return False
    self.snake.move()
    if self.snake.head.compare(self.food.location):
      self.score = self.score + 1
      self.highScoreEngine.checkScore(self.score)
      self.snake.eat()
      self.spawnFood()
    return True

  def isSnakeAlive(self):
    return True

  def spawnFood(self):
    self.food = Food(self.snake.width, self.snake.height)
    while self.isFoodTouchingSnake():
      self.food = Food(self.snake.width, self.snake.height)

  def resetSnake(self):
    self.snake = Snake(Coordinate(3,1), self.snake.width, self.snake.height)
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