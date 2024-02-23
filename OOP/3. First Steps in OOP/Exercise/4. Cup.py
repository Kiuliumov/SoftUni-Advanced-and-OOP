class Cup:
    def __init__(self,size,quantity):
        self.size = size
        self.quantity = quantity
        self.free_space = self.size - self.quantity

    def fill(self,quantity):
        if self.free_space >= quantity:
            self.quantity += quantity
            self.free_space -= quantity

    def status(self):
        return self.free_space
