from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    INITIAL_WEIGHT = 9
    WEIGHT_FACTOR = 3

    def __init__(self, name, kind, price):
        super().__init__(name, kind, price, self.INITIAL_WEIGHT)

    def eating(self):
        self.weight += self.WEIGHT_FACTOR
