import constants
import pygame
from player_kart import PlayerCar
from computer_kart import ComputerCar
from cast import Cast
from handle_collisions import Collision
from handle_move import Move


class Run:
    def __init__(self, player_IMG, opponent_IMG):
        run = True
        clock = pygame.time.Clock()
        images = [(constants.GRASS, (0, 0)), (constants.TRACK, (0, 0)),
            (constants.FINISH, constants.FINISH_POSITION), (constants.TRACK_BORDER, (0, 0))]
        player_car = PlayerCar(4, 4, player_IMG)
        computer_car = ComputerCar(3, 3,opponent_IMG, constants.PATH)

        while run:
            clock.tick(constants.FPS)

            Cast.draw(constants.WIN, images, player_car, computer_car)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                    break

            Move.move_player(player_car)
            computer_car.move()

            Collision.handle_collision(player_car, computer_car)