from abc import ABC, abstractmethod


class BaseService(ABC):
    def __init__(self, name, capacity):
        self.__name = name
        self.__capacity = capacity
        self.__robots = []
        self.type = None

    @property
    def name(self):
        if self.__name.strip() == '':
            raise ValueError('Service name cannot be empty!')
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Service name cannot be empty!')
        self.__name = value

    @property
    def capacity(self):
        if self.__capacity <= 0:
            raise ValueError('Service capacity cannot be less than or equal to zero!')
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError('Service capacity cannot be less than or equal to zero!')
        self.__capacity = value
    @property
    def robots(self):
        return self.__robots

    @robots.setter
    def robots(self, value):
        self.__robots = value

    @abstractmethod
    def details(self):
        pass
