from music.horse_specification.horse import Horse

class Thoroughbred(Horse):

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
        self.max_speed = 140

    def train(self):
        if self.speed + 3 > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += 3
