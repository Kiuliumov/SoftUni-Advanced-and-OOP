class PizzaDelivery:

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False


    def add_extra(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return 'Pizza {} already prepared, and we can\'t make any changes!'.format(self.name)

        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0

        self.ingredients[ingredient] += quantity
        self.price += price_per_quantity * quantity

    def remove_ingredient(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return 'Pizza {} already prepared, and we can\'t make any changes!'.format(self.name)

        if ingredient not in self.ingredients:
            return 'Wrong ingredient selected! We do not use {} in {}!'.format(ingredient, self.name)

        if quantity > self.ingredients[ingredient]:
            return 'Please check again the desired quantity of {}!'.format(ingredient)

        self.ingredients[ingredient] -= quantity
        self.price -= price_per_quantity * quantity

    def make_order(self):
        self.ordered = True
        ingredients = ', '.join( ['{}: {}'.format(ingredient, quantity) for ingredient, quantity in self.ingredients.items()])
        return 'You\'ve ordered pizza {} prepared with {} and the price will be {}lv.'.format(self.name, ingredients, self.price)

