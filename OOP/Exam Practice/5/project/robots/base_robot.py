from abc import ABC, abstractmethod


class BaseRobot(ABC):
    def __init__(self, name: str, kind: str, price: int, weight: int):
        self.__name = name
        self.__kind = kind
        self.__price = price
        self.__weight = weight
        self.type = None

    @property
    def name(self):
        if self.__name.strip() == '':
            raise ValueError('Robot name cannot be empty!')
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Robot name cannot be empty!')
        self.__name = value

    @property
    def kind(self):
        if self.__kind.strip() == '':
            raise ValueError('Robot kind cannot be empty!')

    @kind.setter
    def kind(self, value):
        if value.strip() == '':
            raise ValueError('Robot name cannot be empty!')
        self.__kind = value

    @property
    def price(self):
        if self.__price <= 0.0:
            raise ValueError('Robot price cannot be less than or equal to 0.0!')
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0.0:
            raise ValueError('Robot price cannot be less than or equal to 0.0!')
        self.__price = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value

    @abstractmethod
    def eating(self):
        pass

