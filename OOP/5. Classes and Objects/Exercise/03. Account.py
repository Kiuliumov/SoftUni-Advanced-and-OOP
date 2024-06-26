class Account:
    def __init__(self, id, name, balance = 0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount > self.balance:
            return 'Amount exceeded balance'
        self.balance -= amount
        return self.balance

    def info(self):
        return 'User {} with account {} has {} balance'.format(self.name, self.id, self.balance)

