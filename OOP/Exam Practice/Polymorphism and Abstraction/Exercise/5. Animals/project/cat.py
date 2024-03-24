from project.animal import Animal



class Cat(Animal):
    CLASS_NAME = 'Cat'

    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)
        self.sound = 'Meow meow!'

    def __repr__(self):
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.CLASS_NAME}'

    def make_sound(self):
        return self.sound