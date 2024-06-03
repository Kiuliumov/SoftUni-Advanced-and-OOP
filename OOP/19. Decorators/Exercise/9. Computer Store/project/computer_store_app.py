from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer, manufacturer, model, processor, ram):

        if type_computer not in ['Desktop Computer', 'Laptop']:
            raise ValueError('{} is not a valid type computer!'.format(type_computer))

        if type_computer == 'Desktop Computer':
            computer = DesktopComputer(manufacturer, model)
        else:
            computer = Laptop(manufacturer, model)

        configuration = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return configuration

    def sell_computer(self, client_budget, wanted_processor, wanted_ram):

        computer_to_sell = None

        for computer in self.warehouse:
            if computer.price <= client_budget and computer.processor == wanted_processor and computer.ram >= wanted_ram:
                computer_to_sell = computer

        if computer_to_sell is None:
            raise Exception('Sorry, we don\'t have a computer for you.')

        profit = client_budget - computer_to_sell.price
        self.profits += profit
        self.warehouse.remove(computer_to_sell)
        return '{} sold for {}$.'.format(computer_to_sell.__repr__(), client_budget)