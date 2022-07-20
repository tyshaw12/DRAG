import constants
# Class to handle collisions for player and computer car even though computer doesn't collide with anything right now
class Collision:
    def handle_collision(player_car, computer_car):
        if player_car.collide(constants.TRACK_BORDER_MASK) != None:
            player_car.bounce()

        computer_finish_poi_collide = computer_car.collide(
        constants.FINISH_MASK, *constants.FINISH_POSITION)
        if computer_finish_poi_collide != None:
            player_car.reset()
            computer_car.reset()

        player_finish_poi_collide = player_car.collide(
            constants.FINISH_MASK, *constants.FINISH_POSITION)
        if player_finish_poi_collide != None:
            if player_finish_poi_collide[1] == 0:
                player_car.bounce()
            else:
                player_car.reset()
                computer_car.reset()