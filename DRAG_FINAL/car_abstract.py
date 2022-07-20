import math
import utils
import pygame
# AbstractCar builds the basic car for player_car and computer_car
# They have the same max_vel = max velocity and rotation_vel = rotation velocity, yes you can mess with this and make it very funny looking
class AbstractCar:
    def __init__(self, max_vel, rotation_vel, IMG):
        self.img = IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1
    # Rotate function for the cars
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
    # Function to draw the car
    def draw(self, win):
        utils.blit_rotate_center(win, self.img, (self.x, self.y), self.angle)
    # Function to move the car forward
    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()
    # Function to move the car backward
    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()
    # Function to move the car based on radians and rotation velocity
    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal
    # Collisions(DOENSNT DO MUCH TO COMPUTER BECAUSE COLLISIONS ARE OFF WHILE PATH IS MESSED UP)
    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi
    # Reset cars after finish, currently breaks computer_car
    def reset(self):
        self.x, self.y = self.START_POS
        self.angle = 0
        self.vel = 0
