import pygame

class Cast():
    def draw(win, images, player_car, computer_car):
        for img, pos in images:
            win.blit(img, pos)

        player_car.draw(win)
        computer_car.draw(win)
        pygame.display.update()