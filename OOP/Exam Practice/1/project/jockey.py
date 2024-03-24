class Jockey:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
        self.horse = None

    @property
    def name(self):
        if self.__name == '' or self.__name.isspace():
            raise ValueError('Name should contain at least one character!')
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value.isspace():
            raise ValueError('Name should contain at least one character!')
        self.__name = value

    @property
    def age(self):
        if self.__age < 18:
            raise ValueError('Jockeys must be at least 18 to participate in the race!')
        return self.__age

    @age.setter
    def age(self, value):
        if value < 18:
            raise ValueError('Jockeys must be at least 18 to participate in the race!')
        self.__age = value


