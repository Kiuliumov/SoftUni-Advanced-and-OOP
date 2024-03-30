from music.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):

    def __init__(self, name, kind, price):
        super().__init__(name, kind, price, 9)
        self.type = 'MaleRobot'

    def eating(self):
        self.weight += 3
    