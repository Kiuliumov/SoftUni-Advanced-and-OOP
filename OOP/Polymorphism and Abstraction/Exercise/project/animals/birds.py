from abc import ABC, abstractmethod
from music.animals.animal import Animal
from music.food import Food, Meat


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        Animal.__init__(self, name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]'


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Hoot Hoot'

    def feed(self, food: Food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += 0.25 * food.quantity
            return
        return 'Owl does not eat {}!'.format(food.__class__.__name__)


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Cluck'

    def feed(self, food: Food):
        self.food_eaten += food.quantity
        self.weight += 0.35 * food.quantity
