from music.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    def __init__(self, name, kind, price):
        super().__init__(name,kind,price,7)
        self.type = 'FemaleRobot'

    def eating(self):
        self.weight += 1
