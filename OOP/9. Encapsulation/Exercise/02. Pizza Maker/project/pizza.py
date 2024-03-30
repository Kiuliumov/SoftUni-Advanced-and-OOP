from music.dough import Dough
from music.topping import Topping


class Pizza:
    def __init__(self, name, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}
        if self.name == '':
            raise ValueError('The name cannot be an empty string')
        if self.dough is None:
            raise ValueError('You should add dough to the pizza')
        if max_number_of_toppings <= 0:
            raise ValueError('The maximum number of toppings cannot be less or equal to zero')

    def add_topping(self, topping: Topping):
        if len(self.toppings) < self.max_number_of_toppings:
            if topping.topping_type not in self.toppings:
                self.toppings[topping.topping_type] = topping.weight
            else:
                self.toppings[topping.topping_type] += topping.weight
        else:
            raise ValueError('Not enough space for another topping')

    def calculate_total_weight(self):
        return self.dough.weight + sum(self.toppings.values())
