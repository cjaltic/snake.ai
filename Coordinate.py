# Coordinate class
import random

class Coordinate:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def randomCoordinate(self, width, height):
  	self.x = random.randint(0, width -1)
  	self.y = random.randint(0, height -1)

  def compare(self, c):
  	if self.x == c.x and self.y == c.y:
  		return True
  	return False