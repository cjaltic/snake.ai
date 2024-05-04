## Coordinate class
import random

class Coordinate:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def randomCoordinate(self, start, end):
  	self.x = random.randint(start, end)
  	self.y = random.randint(start, end)