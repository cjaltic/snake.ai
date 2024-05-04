## Food class
import Coordinate

class Food:
  def __init__(self, width, height):
        cord = Coordinate(0,0)
        cord.randomCoordinate(width, height)
        self.location = cord
