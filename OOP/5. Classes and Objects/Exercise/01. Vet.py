class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, anima_name):
        if Vet.space > 0:
            Vet.space -= 1
            self.animals.append(anima_name)
            Vet.animals.append(anima_name)
            return '{} registered in the clinic'.format(anima_name)
        return 'Not enough space'


    def unregister_animal(self, animal_name):
        if animal_name in self.animals:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            Vet.space += 1
            return '{} unregistered successfully'.format(animal_name)
        return '{} not in the clinic'.format(animal_name)

    def info(self):
        return '{} has {} animals. {} space left in clinic'.format(self.name, len(self.animals), Vet.space)


