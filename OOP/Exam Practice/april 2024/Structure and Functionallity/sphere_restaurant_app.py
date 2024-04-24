from project.clients.vip_client import VIPClient
from project.clients.regular_client import RegularClient
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    CLIENTS = {'RegularClient': RegularClient, 'VIPClient': VIPClient}
    WAITERS = {'FullTimeWaiter': FullTimeWaiter, 'HalfTimeWaiter': HalfTimeWaiter}

    def __init__(self):
        self.waiters = []
        self.clients = []

    def hire_waiter(self, waiter_type, waiter_name, hours_worked):

        if waiter_type not in self.WAITERS:
            return f'{waiter_type} is not a recognized waiter type.'

        if self.__get_waiter_by_name(waiter_name):
            return f'{waiter_name} is already on the staff.'

        self.waiters.append(self.WAITERS[waiter_type](waiter_name, hours_worked))
        return f'{waiter_name} is successfully hired as a {waiter_type}.'

    def admit_client(self, client_type, client_name):

        if client_type not in self.CLIENTS:
            return f'{client_type} is not a recognized client type.'

        if self.__get_client_by_name(client_name):
            return f'{client_name} is already a client.'

        self.clients.append(self.CLIENTS[client_type](client_name))
        return f'{client_name} is successfully admitted as a {client_type}.'

    def process_shifts(self, waiter_name):
        waiter = self.__get_waiter_by_name(waiter_name)

        if not waiter:
            return f'No waiter found with the name {waiter_name}.'

        return waiter.report_shift()

    def process_client_order(self, client_name, order_amount):
        client = self.__get_client_by_name(client_name)

        if not client:
            return f'{client_name} is not a registered client.'

        return f'{client_name} earned {client.earning_points(order_amount)} points from the order.'

    def apply_discount_to_client(self, client_name):
        client = self.__get_client_by_name(client_name)

        if not client:
            return f'{client_name} cannot get a discount because this client is not admitted!'

        percentage, points = client.apply_discount()
        return f'{client_name} received a {percentage}% discount. Remaining points {points}'

    def generate_report(self):
        sorted_waiters = sorted(self.waiters, key=lambda w: w.calculate_earnings(), reverse=True)

        waiter_info = "** Waiter Details **\n"
        for waiter in sorted_waiters:
            waiter_info += str(waiter) + "\n"

        total_earnings = sum(waiter.calculate_earnings() for waiter in self.waiters)
        total_client_points = sum(client.points for client in self.clients)
        total_clients = len(self.clients)

        report = f"$$ Monthly Report $$\n"
        report += f"Total Earnings: ${total_earnings:.2f}\n"
        report += f"Total Clients Unused Points: {total_client_points}\n"
        report += f"Total Clients Count: {total_clients}\n"
        report += waiter_info

        return report.strip()

    # helper methods
    def __get_waiter_by_name(self, waiter_name):
        for waiter in self.waiters:
            if waiter.name == waiter_name:
                return waiter
        return None

    def __get_client_by_name(self, client_name):
        for client in self.clients:
            if client.name == client_name:
                return client
        return None
