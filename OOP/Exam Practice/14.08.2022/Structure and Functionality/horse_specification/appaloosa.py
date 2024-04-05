from project.horse_specification.horse import Horse



class Appaloosa(Horse):
    MAXIMUM_HORSE_SPEED = 120

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        if self.speed + 2 > self.MAXIMUM_HORSE_SPEED:
            self.speed = self.MAXIMUM_HORSE_SPEED
        else:
            self.speed += 2


