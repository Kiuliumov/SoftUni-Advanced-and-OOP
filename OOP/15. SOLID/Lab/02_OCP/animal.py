class Animal:
    def __init__(self, species):
        self.species = species
        self.sound = None

    def get_species(self):
        return self.species

    def make_sound(self):
        return self.sound

    def add_sound(self, sound):
        self.sound = sound


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
