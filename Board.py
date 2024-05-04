## Board class
import Snake
import Coordinate
import Food

class Board:
  def __init__(self, width, height, snake = None, food = None):
  	self.snake = snake
  	self.width = width
  	self.height = height
  	self.food = food