from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth


class ChristmasPastryShopApp:
    VALID_DELICACIES = {'Gingerbread': Gingerbread, 'Stolen': Stolen}
    VALID_BOOTHS = {'Open Booth': OpenBooth, 'Private Booth': PrivateBooth}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, delicacy_type, name, price):

        if name in self.get_all_delicacy_names():
            raise Exception(f'{name} already exists!')

        if delicacy_type not in self.VALID_DELICACIES:
            raise Exception(f'{delicacy_type} is not on our delicacy menu!')

        self.delicacies.append(self.VALID_DELICACIES[delicacy_type](name, price))
        return f'Added delicacy {name} - {delicacy_type} to the pastry shop.'

    def add_booth(self, booth_type, booth_number, capacity):

        if booth_number in self.get_all_booth_numbers():
            raise Exception(f'Booth number {booth_number} already exists!')

        if booth_type not in self.VALID_BOOTHS:
            raise Exception(f'{booth_type} is not a valid booth!')

        self.booths.append(self.VALID_BOOTHS[booth_type](booth_number, capacity))
        return f'Added booth number {booth_number} in the pastry shop.'

    def reserve_booth(self, number_of_people):
        booth = self.get_booth_by_number_of_people(number_of_people)

        if not booth:
            raise Exception(f'No available booth for {number_of_people} people!')

        booth.reserve(number_of_people)
        return f'Booth {booth.booth_number} has been reserved for {number_of_people} people.'

    def order_delicacy(self, booth_number, delicacy_name):
        booth = self.find_booth_by_number(booth_number)
        delicacy = self.find_delicacy_by_name(delicacy_name)

        if not booth:
            raise Exception(f'Could not find booth {booth_number}!')

        if not delicacy:
            raise Exception(f'No {delicacy_name} in the pastry shop!')

        booth.order(delicacy)
        return f'Booth {booth_number} ordered {delicacy_name}.'

    def leave_booth(self, booth_number):
        booth = self.find_booth_by_number(booth_number)
        bill = booth.calculate_bill()
        self.income += bill
        booth.free()

        return (f'Booth {booth_number}:\n'
                f'Bill: {bill:.2f}lv.')

    def get_income(self):
        return f'Income: {self.income:.2f}lv.'

    # helper_methods
    def get_all_delicacy_names(self):
        return [delicacy.name for delicacy in self.delicacies]

    def get_all_booth_numbers(self):
        return [booth.booth_number for booth in self.booths]

    def get_booth_by_number_of_people(self, number_of_people):
        booths = [booth for booth in self.booths if booth.capacity >= number_of_people and not booth.is_reserved]
        return booths[0] if booths else None

    def find_booth_by_number(self, booth_number):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                return booth
        return None

    def find_delicacy_by_name(self, delicacy_name):
        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                return delicacy
        return None
