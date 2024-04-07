from exam_practice.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAXIMUM_HORSE_SPEED = 140

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        if self.speed + 3 > self.MAXIMUM_HORSE_SPEED:
            self.speed = self.MAXIMUM_HORSE_SPEED
        else:
            self.speed += 3

