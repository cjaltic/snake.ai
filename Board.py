# Board class
import Snake
import Coordinate
from Food import Food

class Board:
  def __init__(self, width, height, snake, food = None):
    self.snake = snake
    self.width = width
    self.height = height
    self.food = food
    self.score = 0

    if self.food is None:
      self.spawnFood()

  def tick(self):
    print("Score:  ", self.score)
    self.snake.move()
    print("tick head ", self.snake.head)
    print("food ", self.food.location)
    if self.snake.head.compare(self.food.location):
      self.score = self.score + 1
      self.snake.eat()
      print("grow count ", self.snake.growCount)
      self.spawnFood()
      if not self.snake.isAlive():
        # end game
        return

  def spawnFood(self):
    self.food = Food(self.width, self.height)
    while self.isFoodTouchingSnake():
      self.food = Food(self.width, self.height)

  def isFoodTouchingSnake(self):
    if self.food.location.compare(self.snake.head):
      return True
    for c in self.snake.body:
      if self.food.location.compare(c):
        return True
    return False

  def changeSnakeDirection(self, direction):
    self.snake.changeDirection(direction)