class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount):
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry, cannot go in debt!")
        else:
            self.add_transaction(transaction_amount)
            return f"New balance: {self.balance}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        else:
            self._transactions.append(amount)

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        return iter(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return reversed(self._transactions)

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __add__(self, other):
        new_owner = self.owner + '&' + other.owner
        new_amount = self.amount + other.amount
        new_account = Account(new_owner, new_amount)
        new_account._transactions = self._transactions + other._transactions
        return new_account

