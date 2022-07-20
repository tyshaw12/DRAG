import pygame
pygame.init()
from utils import scale_image
from color import Color

# Video stuff
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 60

# Images
GREEN_CAR = pygame.image.load("images/green_car.png").convert_alpha()
FASTEST_CAR = pygame.image.load("images/fastest_car.png").convert_alpha()
GREEN_LORRIE =pygame.image.load("images/green_lorrie.png").convert_alpha()
PURPLE_CYCLE = pygame.image.load("images/purple_cycle.png").convert_alpha()
YELLOW_CYCLE = pygame.image.load("images/yellow_cycle.png").convert_alpha()
PATH = [(175, 119), (110, 70), (56, 133), (70, 481), (318, 731), (404, 680), (418, 521), (507, 475), (600, 551), (613, 715), (736, 713),
        (734, 399), (611, 357), (409, 343), (433, 257), (697, 258), (738, 123), (581, 71), (303, 78), (275, 377), (176, 388), (178, 260)]
GRASS = scale_image(pygame.image.load("images/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("images/track.png"), 0.9)
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

TRACK_BORDER = scale_image(pygame.image.load("images/track-border.png"), 0.9)
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)

FINISH = pygame.image.load("images/finish.png")
FINISH_MASK = pygame.mask.from_surface(FINISH)
FINISH_POSITION = (130, 250)

# Fonts
big_font = pygame.font.SysFont("arialblack", 40)
small_font = pygame.font.SysFont("arialblack", 11)
medium_font = pygame.font.SysFont("arialblack", 16)

# Colors
TEXT_COL = Color(255, 255, 255)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)

# WIN condition
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))