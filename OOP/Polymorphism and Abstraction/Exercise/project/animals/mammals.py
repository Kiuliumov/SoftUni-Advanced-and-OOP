from abc import ABC, abstractmethod
from project.animals.animal import Animal
class Mammal(ABC, Animal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    @abstractmethod
    def make_sound(self):
        pass


