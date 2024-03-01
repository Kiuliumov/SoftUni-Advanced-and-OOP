class Customer:
    ID = 1

    def __init__(self, name: str, address: str, email: str) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.customer_id = Customer.ID
        Customer.ID += 1

    @staticmethod
    def get_next_id() -> int:
        return Customer.ID

    def __repr__(self) -> str:
        return 'Customer <{}> {}; Address: {}; Email: {}'.format(self.customer_id,self.name,self.address,self.email)
