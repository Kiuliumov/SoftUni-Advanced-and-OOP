from abc import ABC, abstractmethod
from project.animals.animal import Animal


class Bird(ABC, Animal):
    def __init__(self, name, weight, wing_size):
        Animal.__init__(self, name, weight)
        self.wing_size = wing_size

    @abstractmethod
    def make_sound(self):
        pass





class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return 'Hoot Hoot'


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
