from music.animal import Animal


class Dog(Animal):
    CLASS_NAME = 'Dog'
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)

    def __repr__(self):
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.CLASS_NAME}'

    def make_sound(self):
        return 'Woof!'
