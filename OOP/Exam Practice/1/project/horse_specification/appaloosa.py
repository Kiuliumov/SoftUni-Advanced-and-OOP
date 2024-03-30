from music.horse_specification.horse import Horse

class Appaloosa(Horse):

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
        self.max_speed = 120

    def train(self):
        if self.speed + 2 > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += 2
