from abc import ABC, abstractmethod


class Horse(ABC):

    def __init__(self, name: str, speed: int):
        self.__name = name
        self.__speed = speed
        self.is_taken = False
        self.max_speed = 0

    @property
    def name(self):
        if len(self.__name) < 4:
            raise ValueError('Horse name {} is less than 4 symbols!'.format(self.__name))
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError('Horse name {} is less than 4 symbols!'.format(self.__name))
        self.__name = value

    @property
    def speed(self):
        if self.__speed > self.max_speed:
            raise ValueError('Horse speed is too high!')
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.max_speed:
            raise ValueError('Horse speed is too high!')
        self.__speed = value

    @abstractmethod
    def train(self):
        pass
