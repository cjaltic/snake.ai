# Board class
import Snake
import Coordinate
from Food import Food

class Board:
  def __init__(self, snake, food = None):
    self.snake = snake
    self.food = food
    self.score = 0

    if self.food is None:
      self.spawnFood()

  def tick(self):
    self.snake.move()
    if self.snake.head.compare(self.food.location):
      self.score = self.score + 1
      self.snake.eat()
      self.spawnFood()
      if not self.snake.isAlive():
        # end game
        return

  def spawnFood(self):
    self.food = Food(self.snake.width, self.snake.height)
    while self.isFoodTouchingSnake():
      self.food = Food(self.snake.width, self.snake.height)

  def isFoodTouchingSnake(self):
    if self.food.location.compare(self.snake.head):
      return True
    for c in self.snake.body:
      if self.food.location.compare(c):
        return True
    return False

  def changeSnakeDirection(self, direction):
    self.snake.changeDirection(direction)