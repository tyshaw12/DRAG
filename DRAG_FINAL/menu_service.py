import pygame
import constants
from draw import Draw
from button import Button
from game import Run
pygame.init()
#create instances of button
green_car = Button(200, 300, constants.GREEN_CAR, 1)
green_lorrie = Button(390, 300, constants.GREEN_LORRIE, 1)
fastest_car = Button( 300, 300, constants.FASTEST_CAR , 1)
purple_motorcycle = Button(500, 300, constants.PURPLE_CYCLE, 1)
yellow_motorcycle = Button(580, 300, constants.YELLOW_CYCLE, 1)

clicked = True
yellow_cycle = False
screen = constants.screen
def main_menu():
    pygame.display.set_caption("Choose your car!")
# loop for the menu
    Menu = True
    while Menu:
        screen.fill((52,78,91))

        Draw.draw_text("Esc = Quit ", constants.small_font, (255,255,255), 40, 40)
        Draw.draw_text("Click on a car to choose it!", constants.big_font, (255,255,255), 120, 90)
        # This is what I'm most proud of. This menu took forever to build.
        if green_car.load_button(screen):
            Run(constants.GREEN_CAR, constants.FASTEST_CAR)
        if green_lorrie.load_button(screen):
            Run(constants.GREEN_LORRIE, constants.YELLOW_CYCLE)
        if fastest_car.load_button(screen):
            Run(constants.FASTEST_CAR, constants.GREEN_CAR)
        if purple_motorcycle.load_button(screen):
            Run(constants.PURPLE_CYCLE, constants.YELLOW_CYCLE)
        if yellow_motorcycle.load_button(screen):
            Run(constants.YELLOW_CYCLE, constants.PURPLE_CYCLE)
        
        pygame.display.update()  
# Event handling (Only handles quitting right now)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Menu = False
    if event.type == pygame.QUIT:
        Menu = False
        
main_menu()