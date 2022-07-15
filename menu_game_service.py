import pygame
pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Choose your car!")

#Create reusable locales
max_y = 600
max_x = 800

#Load images
GREEN_CAR = pygame.image.load("images/green_car.png")
FASTEST_CAR = pygame.image.load("images/fastest_car.png")
GREEN_LORRIE =pygame.image.load("images/green_lorrie.png")
PURPLE_CYCLE = pygame.image.load("images/purple_cycle.png")
YELLOW_CYCLE = pygame.image.load("images/yellow_cycle.png")

#define fonts
font = pygame.font.SysFont("arialblack", 40)
small_font = pygame.font.SysFont("arialblack", 11)
medium_font = pygame.font.SysFont("arialblack", 16)
#define colors
TEXT_COL = (255,255,255)

# draw text and display images
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
def draw_pic(file, x, y):
    img = file
    screen.blit(img, (x,y))

# define game variables
green_car = False
fastest_car = False
green_lorrie = False
purple_cycle = False
yellow_cycle = False

# loop for the game
run = True
while run:
    screen.fill((52,78,91))
    draw_text("Choose your car!", font, TEXT_COL, 230, 80)
    draw_pic(GREEN_CAR, 200, 300)
    draw_text("Press 1", small_font, TEXT_COL, 200, 280)
    draw_pic(FASTEST_CAR, 300, 300)
    draw_text("Press 2", small_font, TEXT_COL, 300, 280)
    draw_pic(GREEN_LORRIE, 390, 300)
    draw_text("Press 3", small_font, TEXT_COL, 400, 280)
    draw_pic(PURPLE_CYCLE, 500, 300)
    draw_text("Press 4", small_font, TEXT_COL, 490, 280)
    draw_pic(YELLOW_CYCLE, 580, 300)
    draw_text("Press 5", small_font, TEXT_COL, 570, 280)



    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                green_car = True
                draw_text("You wanted the green car? Y/N", medium_font, TEXT_COL, 260, 500)
            if event.key == pygame.K_2:
                fastest_car = True
                draw_text("You wanted the fastest car? Y/N", medium_font, TEXT_COL, 260, 500)
            if event.key == pygame.K_3:
                green_lorrie = True
                draw_text("You wanted the green lorrie? Y/N", medium_font, TEXT_COL, 250, 500)
            if event.key == pygame.K_4:
                purple_cycle = True
                draw_text("You wanted the purple motorcycle? Y/N", medium_font, TEXT_COL, 220, 500)
            if event.key == pygame.K_5:
                yellow_cycle = True
                draw_text("You wanted the yellow motorcycle? Y/N", medium_font, TEXT_COL, 220, 500)
            if event.key == pygame.K_ESCAPE:
                run = False
        pygame.display.update()      
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

