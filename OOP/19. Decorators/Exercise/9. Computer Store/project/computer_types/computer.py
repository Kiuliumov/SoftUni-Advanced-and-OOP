from abc import ABC, abstractmethod


class Computer(ABC):
    VALID_TYPES = ['Laptop', 'Desktop Computer']

    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError('Manufacturer name cannot be empty.')
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError('Model name cannot be empty.')
        self.__model = value

    @abstractmethod
    def configure_computer(self, processor, ram):
        pass

    def __repr__(self):
        return '{} {} with {} and {}GB RAM'.format(self.manufacturer, self.model, self.processor, self.ram)
