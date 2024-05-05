# Painter GUI class
import pygame
from Board import Board
from Snake import Snake
from Food import Food
from Coordinate import Coordinate
class Painter:
  # eventually implement so there are discrete screen sizes
  # 20x20 would be a good "medium" size.  for now we will mostly
  # use 20 as the default size
  def __init__(self, board, width=20, height=20, pixelSize=26, pieceSize=22, speed=0):
    pygame.init()
    self.width = width
    self.height = height
    self.running = True

    self.board = board

    self.pixelSize = pixelSize
    self.pieceSize = pieceSize

    self.pixelPadding = (self.pixelSize - self.pieceSize) / 2

    self.paddingSize = 70

    # Convert speed value to buffer
    self.speed = 10
    if speed == 0:
      self.speed = 5
    if speed == 1:
      self.speed = 10
    if speed == 2:
      self.speed = 15

    # Set up colors
    DARK_BROWN = (135,112,80)
    BROWN = (159,130,92)
    GREEN = (101,188,79)
    LILAC = (234, 215, 237)
    WHITE = (249,234,251)
    RED = (136,8,8)

    # Set colors
    self.BORDER_COLOR = BROWN
    self.BACKGROUND_COLOR = GREEN
    self.SNAKE_COLOR = LILAC
    self.FOOD_COLOR = RED
    self.TEXT_COLOR = WHITE

    # Set up fonts
    self.bigFont = pygame.font.Font(None, 50)
    self.font = pygame.font.Font(None, 36)

    self.screen = pygame.display.set_mode((self.width*self.pixelSize + self.paddingSize, self.height*self.pixelSize + self.paddingSize))
    pygame.display.set_caption("snake")
    self.clock = pygame.time.Clock()

  def gameLoop(self):
    running = True
    while running:
      # add delay
      self.clock.tick(self.speed)
      # Event handling
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            key_pressed = "UP"
            self.board.changeSnakeDirection(3)
            break
          elif event.key == pygame.K_DOWN:
            key_pressed = "DOWN"
            self.board.changeSnakeDirection(1)
            break
          elif event.key == pygame.K_LEFT:
            key_pressed = "LEFT"
            self.board.changeSnakeDirection(2)
            break
          elif event.key == pygame.K_RIGHT:
            key_pressed = "RIGHT"
            self.board.changeSnakeDirection(0)
            break
          else:
            key_pressed = "UNKNOWN"
          print("Key pressed:", key_pressed)
      
      if not self.board.tick():
        running = False

      self.paint()
        
  def resetSnake(self):
    self.board.resetSnake()

  def resetScore(self):
    self.board.resetScore()

  def paint(self):
    self.paintBackground()
    self.paintSnake()
    self.paintFood()
    self.paintScore()
    pygame.display.flip()

  def paintScore(self):
    self.screen.blit(self.font.render("Score: " + str(self.board.score), False, self.TEXT_COLOR, self.BORDER_COLOR), (self.paddingSize/6, ((self.height - 1)*self.pixelSize + self.paddingSize) - self.pixelPadding))

  def paintBackground(self):
    # Paint background (border)
    self.screen.fill(self.BORDER_COLOR)
    # Paint playing field
    pygame.draw.rect(self.screen, self.BACKGROUND_COLOR, (self.paddingSize/2, self.paddingSize/2, self.width*self.pixelSize, self.height*self.pixelSize))

  def paintEndGame(self):
    self.screen.blit(self.bigFont.render("GAME OVER", False, self.TEXT_COLOR, self.BACKGROUND_COLOR), (50,50))
    self.screen.blit(self.bigFont.render("SCORE:  " + str(self.board.score), False, self.TEXT_COLOR, self.BACKGROUND_COLOR), (50,100))
    self.screen.blit(self.font.render("press q to quit or", False, self.TEXT_COLOR, self.BACKGROUND_COLOR), (50,200))
    self.screen.blit(self.font.render("press any other key to play again", False, self.TEXT_COLOR, self.BACKGROUND_COLOR), (50,2500))
  def paintFood(self):
     pygame.draw.rect(self.screen, self.FOOD_COLOR, (self.paddingSize/2 + (self.board.food.location.x * self.pixelSize) + self.pixelPadding, self.paddingSize/2 + (self.board.food.location.y * self.pixelSize) + self.pixelPadding, self.pieceSize, self.pieceSize))

  def paintSnake(self):
    # for now just passing in a snake to test painting
    # later will get this snake object from self.board

    # paint head
    pygame.draw.rect(self.screen, self.SNAKE_COLOR, (self.paddingSize/2 + (self.board.snake.head.x * self.pixelSize) + self.pixelPadding, self.paddingSize/2 + (self.board.snake.head.y * self.pixelSize) + self.pixelPadding, self.pieceSize, self.pieceSize))

    # paint body
    for piece in self.board.snake.body:
      pygame.draw.rect(self.screen, self.SNAKE_COLOR, (self.paddingSize/2 + (piece.x * self.pixelSize) + self.pixelPadding, self.paddingSize/2 + (piece.y * self.pixelSize) + self.pixelPadding, self.pieceSize, self.pieceSize))

  def endGame(self):
    self.paintBackground()
    self.paintEndGame()
    pygame.display.flip()
    
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          pygame.quit()
          quit()
          return False
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            running = False
            pygame.quit()
            quit()
            return False
          else:
            running = False
            break
    return True

    """
    pygame.draw.rect(self.screen, self.SNAKE_COLOR, (self.paddingSize/2 + self.pixelPadding, self.paddingSize/2 + self.pixelPadding, self.pieceSize, self.pieceSize))
    pygame.draw.rect(self.screen, self.SNAKE_COLOR, (self.paddingSize/2 + self.pixelSize + self.pixelPadding, self.paddingSize/2 + self.pixelPadding, self.pieceSize, self.pieceSize))
    pygame.draw.rect(self.screen, self.SNAKE_COLOR, (self.paddingSize/2 + (2 * self.pixelSize) + self.pixelPadding, self.paddingSize/2 + self.pixelPadding, self.pieceSize, self.pieceSize))


    pygame.draw.rect(self.screen, self.SNAKE_COLOR, (self.paddingSize/2 + self.pixelPadding, self.paddingSize/2 + self.pixelPadding, self.pieceSize, self.pieceSize))
    pygame.draw.rect(self.screen, self.SNAKE_COLOR, (self.paddingSize/2 + self.pixelPadding, self.paddingSize/2 + self.pixelSize + self.pixelPadding, self.pieceSize, self.pieceSize))
    pygame.draw.rect(self.screen, self.SNAKE_COLOR, (self.paddingSize/2 + self.pixelPadding, self.paddingSize/2 + (2 * self.pixelSize) + self.pixelPadding, self.pieceSize, self.pieceSize))
    """


# (self, width, height, snake = None, food = None):
# Board
"""
f = Food(20,20)
testSnakeStraightTop = Snake(Coordinate(4,0), 20, 20, [Coordinate(0,0), Coordinate(1,0), Coordinate(2,0), Coordinate(3,0)])
startingSnake = Snake(Coordinate(3,1), 20, 20, [])
# (self, width, height, snake = None, food = None):
b = Board(testSnakeStraightTop,f)
g = Painter(b)

while True:
  g.gameLoop()
"""

"""
  
pygame.init()

w = 500
h = 500

screen = pygame.display.set_mode((w*1.1, h*1.1))
pygame.display.set_caption("snake")

# Set up colors
DARK_BROWN = (135,112,80)
BROWN = (159,130,92)
GREEN = (101,188,79)
LILAC = (234, 215, 237)
WHITE = (249,234,251)

# Set colors
BORDER_COLOR = BROWN
BACKGROUND_COLOR = GREEN
SNAKE_COLOR = LILAC
FOOD_COLOR = DARK_BROWN
TEXT_COLOR = WHITE

# Set up fonts
font = pygame.font.Font(None, 36)

# Run until the user asks to quit
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                key_pressed = "UP"
            elif event.key == pygame.K_DOWN:
                key_pressed = "DOWN"
            elif event.key == pygame.K_LEFT:
                key_pressed = "LEFT"
            elif event.key == pygame.K_RIGHT:
                key_pressed = "RIGHT"
            else:
                key_pressed = "UNKNOWN"
                
            # Print which key is being pressed
            print("Key pressed:", key_pressed)

    # Fill the background with white
    screen.fill(WHITE)


    square_color = (255, 0, 0)
    # Draw square
    pygame.draw.rect(screen, (0,0,0), (248, 248, 26, 26))
    pygame.draw.rect(screen, square_color, (250, 250, 22, 22))

    # Draw a solid blue circle in the center
    # draw.circle(screen to draw to, color, (origin), radius)
    #pygame.draw.circle(screen, BLUE, (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

"""