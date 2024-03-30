from music import animal, caretaker, cheetah, keeper, lion, tiger, vet, worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: animal.Animal, price: int):
        if self.__budget - price >= 0 and len(self.animals) + 1 <= self.__animal_capacity:
            self.__budget -= price
            self.animals.append(animal)
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        if not len(self.animals) + 1 <= self.__animal_capacity:
            return 'Not enough space for animal'
        return 'Not enough budget'

    def hire_worker(self, worker: worker.Worker):
        if len(self.workers) + 1 <= self.__workers_capacity:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        return 'Not enough space for worker'

    def fire_worker(self, worker_name: str):
        names_of_workers = [worker.name for worker in self.workers]
        if worker_name in names_of_workers:
            self.workers.remove(self.workers[names_of_workers.index(worker_name)])
            return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        needed_money = sum([worker.salary for worker in self.workers])
        if self.__budget >= needed_money:
            self.__budget -= needed_money
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        money_needed = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= money_needed:
            self.__budget -= money_needed
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        string = f'You have {len(self.animals)} animals\n'
        lions = [a for a in self.animals if isinstance(a, lion.Lion)]
        tigers = [a for a in self.animals if isinstance(a, tiger.Tiger)]
        cheetahs = [a for a in self.animals if isinstance(a, cheetah.Cheetah)]
        string += f'----- {len(lions)} Lions:'
        for l in lions:
            string += f'\n{l.__repr__()}'
        string += f'\n----- {len(tigers)} Tigers:'
        for t in tigers:
            string += f'\n{t.__repr__()}'
        string += f'\n----- {len(cheetahs)} Cheetahs:'
        for c in cheetahs:
            string += f'\n{c.__repr__()}'
        return string

    def workers_status(self):
        string = f'You have {len(self.workers)} workers\n'
        caretakers = [w for w in self.workers if isinstance(w, caretaker.Caretaker)]
        keepers = [w for w in self.workers if isinstance(w, keeper.Keeper)]
        vets = [w for w in self.workers if isinstance(w, vet.Vet)]
        string += f'----- {len(keepers)} Keepers:'
        for k in keepers:
            string += f'\n{k.__repr__()}'
        string += f'\n----- {len(caretakers)} Caretakers:'
        for c in caretakers:
            string += f'\n{c.__repr__()}'
        string += f'\n----- {len(vets)} Vets:'
        for v in vets:
            string += f'\n{v.__repr__()}'
        return string
