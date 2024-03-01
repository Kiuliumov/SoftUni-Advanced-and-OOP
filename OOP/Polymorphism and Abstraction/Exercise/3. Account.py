class Account:
    def __init__(self, owner, amount=0):
        self.index = 0
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount):
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry, cannot go in debt!")
        self._transactions.append(transaction_amount)
        return f"New balance: {self.balance}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        if self.balance + amount < 0:
            raise ValueError("sorry, cannot go in debt!")
        self._transactions.append(amount)
        return f"New balance: {self.balance}"

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __repr__(self):
        return "Account({}, {})".format(self.owner, self.amount)

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self._transactions):
            item = self._transactions[self.index]
            self.index += 1
            return item
        else:
            self.index = 0
            raise StopIteration

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return reversed(self._transactions)

    def __len__(self):
        return len(self._transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __add__(self, other):
        new_instance = Account(self.owner + '&' + other.owner, self.amount + other.amount)
        new_instance._transactions = self._transactions + other._transactions
        return new_instance

def main():
    acc = Account('bob', 10)

    acc2 = Account('john')

    print(acc)

    print(repr(acc))

    acc.add_transaction(20)

    acc.add_transaction(-20)

    acc.add_transaction(30)

    print(acc.balance)

    print(len(acc))

    for transaction in acc:
        print(transaction)
    print(acc[1])
    print(list(reversed(acc)))
    acc2.add_transaction(10)
    acc2.add_transaction(60)
    print(acc > acc2)
    print(acc >= acc2)
    print(acc < acc2)
    print(acc <= acc2)
    print(acc == acc2)
    print(acc != acc2)
    acc3 = acc + acc2
    print(acc3)
    print(acc3._transactions)

if __name__ == "__main__":
    main()