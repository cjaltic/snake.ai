## Snake class
import Coordinate

class Snake:
  def __init__(self, head, width, height):
  	# head is the initial coordinate
    self.head = head
    # here is the key for the direction code
    # 0 : right
    # 1 : down
    # 2 : left
    # 3 : up
    self.dir = 0
    self.body = []
    self.length = 1
    self.alive = True
    self.width = width
    self.height = height
    self.growCount = 0

  def isAlive(self):
  	if self.head in self.body:
  		self.alive = False
  		return False
  	elif self.head.x < 0:
  		self.alive = False
  		return False
  	elif self.head.x > self.width:
  		self.alive = False
  		return False
  	elif self.head.y < 0 :
  		self.alive = False
  		return False
  	elif self.head.y > self.height:
  		self.alive = False
  		return False
  	else:
  		return True

  def changeDirection(self, direction = 0):
  	if direction < 0 or direction > 3:
  		return False
  	self.direction = direction


  def move(self):
  	if self.growCount > 0:
  		self.growCount = self.growCount - 1
  		if self.dir == 0:
  			self.body.append(head)
  			self.length = self.length + 1
  			self.head = self.head.modX(self.head.x + 1)
  		if self.dir == 1:
  			self.body.append(head)
  			self.length = self.length + 1
  			self.head = self.head.modY(self.head.y - 1)
  		if self.dir == 2:
  			self.body.append(head)
  			self.length = self.length + 1
  			self.head = self.head.modX(self.head.x - 1)
  		if self.dir == 3:
  			self.body.append(head)
  			self.length = self.length + 1
  			self.head = self.head.modY(self.head.y + 1)
  	else:
  		if self.dir == 0:
  			self.body.append(head)
  			self.body.remove(self.body[0])
  			self.head = self.head.modX(self.head.x + 1)
  		if self.dir == 1:
  			self.body.append(head)
  			self.body.remove(self.body[0])
  			self.head = self.head.modY(self.head.y - 1)
  		if self.dir == 2:
  			self.body.append(head)
  			self.body.remove(self.body[0])
  			self.head = self.head.modX(self.head.x - 1)
  		if self.dir == 3:
  			self.body.append(head)
  			self.body.remove(self.body[0])
  			self.head = self.head.modY(self.head.y + 1)


  	def eat(self):
  		self.growCount = self.growCount + 3
