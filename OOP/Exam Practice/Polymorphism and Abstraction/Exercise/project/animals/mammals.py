from abc import ABC

from project.animals.animal import Animal
from project.food import Food, Fruit, Meat, Vegetable


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Squeak'

    def feed(self, food: Food):
        if isinstance(food, Vegetable) or isinstance(food, Fruit):
            self.food_eaten += food.quantity
            self.weight += 0.1 * food.quantity
            return
        return 'Mouse does not eat {}!'.format(food.__class__.__name__)


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Woof!'

    def feed(self, food: Food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += 0.4 * food.quantity
            return
        return 'Dog does not eat {}!'.format(food.__class__.__name__)


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Meow'

    def feed(self, food: Food):
        if isinstance(food, Vegetable) or isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += 0.3 * food.quantity
            return
        return 'Cat does not eat {}!'.format(food.__class__.__name__)


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'ROAR!!!'

    def feed(self, food: Food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += 1 * food.quantity
            return
        return 'Tiger does not eat {}!'.format(food.__class__.__name__)
