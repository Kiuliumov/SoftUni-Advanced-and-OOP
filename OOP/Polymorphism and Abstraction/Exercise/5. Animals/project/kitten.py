from music.cat import Cat


class Kitten(Cat):
    CLASS_NAME = 'Kitten'

    def __init__(self, name, age):
        super().__init__(name, age, 'Female')
        self.sound = 'Meow'
