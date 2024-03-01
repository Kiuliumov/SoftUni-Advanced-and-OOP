class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < 10:
            self.customers.append(customer)
        return

    def add_dvd(self, dvd):
        if len(self.dvds) < 15:
            self.dvds.append(dvd)
        return

    def rent_dvd(self, customer_id, dvd_id):
        customer_ids = [customer.id for customer in self.customers]
        dvd_ids = [dvd.id for dvd in self.dvds]
        customer = self.customers[customer_ids.index(customer_id)]
        dvd = self.dvds[dvd_ids.index(dvd_id)]
        if dvd in customer.rented_dvds:
            return f'{customer.name} has already rented {dvd.name}'
        if dvd.is_rented:
            return 'DVD is already rented'
        if customer.age < dvd.age_restriction:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id, dvd_id):
        customer_ids = [customer.id for customer in self.customers]
        dvd_ids = [dvd.id for dvd in self.dvds]
        customer = self.customers[customer_ids.index(customer_id)]
        dvd = self.dvds[dvd_ids.index(dvd_id)]
        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f'{customer.name} has successfully returned {dvd.name}'
        return f'{customer.name} does not have that DVD'

    def __repr__(self):
        string = ''
        for customer in self.customers:
            string += customer.__repr__() + '\n'
        for dvd in self.dvds:
            string += dvd.__repr__() + '\n'
        return string
