from car_abstract import AbstractCar
#PlayerCar class
#Uses AbstractCar as a parent class
class PlayerCar(AbstractCar):
    def __init__(self, max_vel, rotation_vel, IMG):
        super().__init__(max_vel, rotation_vel, IMG)
        self.IMG = IMG
        self.current_point = 0
        self.vel = max_vel
    START_POS = (180, 200)

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
        self.vel = -self.vel/2
        self.move()
