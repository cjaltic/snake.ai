# Snake class
from Coordinate import Coordinate

class Snake:
  def __init__(self, head, body = []):
    # head is the initial coordinate
    self.head = head
    # here is the key for the direction code
    # 0 : right
    # 1 : down
    # 2 : left
    # 3 : up
    self.dir = 0
    self.body = body
    self.length = 1
    self.alive = True
    self.growCount = 0

  def changeDirection(self, direction = 0):
    if self.canChangeDirection(direction):
      self.dir = direction

  def move(self):
    if self.growCount > 0:
      self.growCount = self.growCount - 1
      if self.dir == 0:
        self.body.append(self.head)
        self.length = self.length + 1
        self.head = Coordinate(self.head.x + 1, self.head.y)
      if self.dir == 1:
        self.body.append(self.head)
        self.length = self.length + 1
        self.head = Coordinate(self.head.x, self.head.y + 1)
      if self.dir == 2:
        self.body.append(self.head)
        self.length = self.length + 1
        self.head = Coordinate(self.head.x - 1, self.head.y)
      if self.dir == 3:
        self.body.append(self.head)
        self.length = self.length + 1
        self.head = Coordinate(self.head.x, self.head.y - 1)
    else:
      if self.dir == 0:
        self.body.append(self.head)
        self.body.remove(self.body[0])
        self.head = Coordinate(self.head.x + 1, self.head.y)
      if self.dir == 1:
        self.body.append(self.head)
        self.body.remove(self.body[0])
        self.head = Coordinate(self.head.x, self.head.y + 1)
      if self.dir == 2:
        self.body.append(self.head)
        self.body.remove(self.body[0])
        self.head = Coordinate(self.head.x - 1, self.head.y)
      if self.dir == 3:
        self.body.append(self.head)
        self.body.remove(self.body[0])
        self.head = Coordinate(self.head.x, self.head.y - 1)

  def isTouchingSelf(self):
    for c in self.body:
      if c.compare(self.head):
        return True
    return False

  def canChangeDirection(self, direction):
    if self.dir == direction:
      return False
    elif self.length == 1:
      return True
    elif self.dir < 0:
      return False
    elif self.dir > 3:
      return False
    elif self.dir == 0 and direction == 2:
      return False
    elif self.dir == 1 and direction == 3:
      return False
    elif self.dir == 2 and direction == 0:
      return False
    elif self.dir == 3 and direction == 1:
      return False
    return True

  def eat(self):
    self.growCount = self.growCount + 3
