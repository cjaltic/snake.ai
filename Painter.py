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

  def pygameEventHandler(self):
    # buffer
    self.clock.tick(self.speed)
    key_pressed = "STRIAGHT"
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
    return key_pressed
        
  def resetSnake(self):
    self.board.resetSnake()

  def resetScore(self):
    self.board.resetScore()

  def paint(self):
    self.paintBackground()
    self.paintSnake()
    self.paintFood()
    self.paintScore()
    self.paintHighScore()
    pygame.display.flip()

  def paintScore(self):
    self.screen.blit(self.font.render("SCORE: " + str(self.board.score), False, self.TEXT_COLOR, self.BORDER_COLOR), (self.paddingSize/6, ((self.height - 1)*self.pixelSize + self.paddingSize) - self.pixelPadding))

  def paintBackground(self):
    # Paint background (border)
    self.screen.fill(self.BORDER_COLOR)
    # Paint playing field
    pygame.draw.rect(self.screen, self.BACKGROUND_COLOR, (self.paddingSize/2, self.paddingSize/2, self.width*self.pixelSize, self.height*self.pixelSize))

  def paintHighScore(self):
    self.screen.blit(self.font.render("HIGH SCORE: " + str(self.board.highScoreEngine.highScore), False, self.TEXT_COLOR, self.BORDER_COLOR), ((self.width*self.pixelSize + self.paddingSize) - ((self.width * self.pixelSize + self.paddingSize) / 3), ((self.height - 1)*self.pixelSize + self.paddingSize) - self.pixelPadding))

  def paintEndGame(self):
    self.screen.blit(self.bigFont.render("GAME OVER", False, self.TEXT_COLOR, self.BACKGROUND_COLOR), (50,50))
    self.screen.blit(self.bigFont.render("SCORE:  " + str(self.board.score), False, self.TEXT_COLOR, self.BACKGROUND_COLOR), (50,100))
    self.screen.blit(self.font.render("press q to quit or", False, self.TEXT_COLOR, self.BACKGROUND_COLOR), (50,200))
    self.screen.blit(self.font.render("press any other key to play again", False, self.TEXT_COLOR, self.BACKGROUND_COLOR), (50,250))
    self.paintHighScore()
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

