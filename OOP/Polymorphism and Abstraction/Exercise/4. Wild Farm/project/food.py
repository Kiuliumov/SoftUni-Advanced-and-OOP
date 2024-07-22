from abc import ABC


class Food(ABC):
    def __init__(self, quantity: int):
        self.quantity = quantity


class Vegetable(Food):
    ...


class Seed(Food):
   ...


class Meat(Food):
    ...


class Fruit(Food):
   ...
