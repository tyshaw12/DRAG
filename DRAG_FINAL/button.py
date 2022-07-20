import pygame

#button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
# Function to load each button
    def load_button(self, surface):
        action = False
        # get mouse position
        mouse_pos = pygame.mouse.get_pos()
        # get mouse locaion+ collision
        if self.rect.collidepoint(mouse_pos):
            # get_pressed left click is index 0 , right click is index 1 , middle click is index 2
            # Handles mouse action does on the button
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked == False
        # draw button
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action