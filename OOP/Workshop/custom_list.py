class CustomList:

    def __init__(self):
        self.array = []


    def append(self, value):
        self.array.append(value)

    def remove(self, ind_to_remove):
        for i in range(len(self.array)):
            if i == ind_to_remove:
                return self.array.pop(i)
        raise IndexError(f'Index {ind_to_remove} does not exist')

    def get(self, index):
        for i in range(len(self.array)):
            if i == index:
                return self.array[i]
        raise IndexError(f'Index {index} does not exist')

    def extend(self, iterable):
        for item in iterable:
            self.array.append(item)
        return self

    def insert(self, index, value):
        self.array.insert(index, value)

    def pop(self):
        return self.array.pop()

    def clear(self):
        self.array = []

    def index(self, value):
        for item in self.array:
            if item == value:
                return item
        raise ValueError(f'Value {value} does not exist')

    def count(self, value):
        counter = 0
        for item in self.array:
            if item == value:
                counter += 1
        return counter

    def reverse(self):
        return self.array[::-1]

    def copy(self):
        new_list = CustomList()
        new_list.array.extend(self.array)
        return new_list

    def size(self):
        return len(self.array)

    def add_first(self, value):
        self.array = [value] + self.array

    def dictionize(self):
        dictionary = {}

        for i, item in enumerate(self.array):
            if i % 2 == 0:
                dictionary[item] = self.array[i + 1]
        return dictionary

    def move(self, amount):

        if amount > len(self.array):
            raise IndexError(f'Amount is bigger than the length of the array')
        for i in range(amount):
            self.array.append(self.array.pop(0))
        return self.array

    def sum(self):
        sum = 0
        for item in self.array:
            if item.__class__.__name__ == 'int' or item.__class__.__name__ == 'float' or item.__class__.__name__ == 'float':
                sum += float(item)
            else:
                sum += len(item)
        return sum

    def overbound(self):
        biggest_value = self.array[0]
        for i in range(1, len(self.array)):

            current_value = self.array[i]
            for item in self.array:
                if item.__class__.__name__ == 'int' or item.__class__.__name__ == 'float' or item.__class__.__name__ == 'float':
                    current_value = float(item)
                else:
                    current_value = len(item)

            if current_value > biggest_value:
                biggest_value = current_value
        return biggest_value

    def underbound(self):
        smallest_value = self.array[0]

        for i in range(1, len(self.array)):

            current_value = self.array[i]
            for item in self.array:
                if item.__class__.__name__ == 'int' or item.__class__.__name__ == 'float' or item.__class__.__name__ == 'float':
                    current_value = float(item)
                else:
                    current_value = len(item)

            if current_value < smallest_value:
                smallest_value = current_value

        return smallest_value