class Shop:
    def __init__(self, name, shop_type, capacity):
        self.name = name
        self.type = shop_type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, shop_type):
        return cls(name, shop_type, 10)

    def add_item(self, item):
        if len(self.items) < self.capacity:
            if item not in self.items:
                self.items[item] = 0
            self.items[item] += 1
            return item + ' added to the shop'
        return 'Not enough capacity in the shop'

    def remove_item(self, item, amount):
        if item in self.items:
            self.items[item] -= amount
            if self.items[item] <= 0:
                del self.items[item]
            return str(amount) + ' ' + item + ' removed from the shop'
        return 'Cannot remove ' + str(amount) + ' ' + item

    def __repr__(self):
        return self.name + ' of type ' + self.type + ' with capacity ' + str(self.capacity)
