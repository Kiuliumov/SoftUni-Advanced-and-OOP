class Person:

    def __init__(self, name: str, surname):
        self.name = name
        self.surname = surname
        self.index = 0

    def __repr__(self) -> str:
        return self.name + ' ' + self.surname

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:

    def __init__(self, name, people):
        self.index = 0
        self.name = name
        self.people = people

    def __repr__(self):
        return f'Group {self.name} with members {", ".join([person.__repr__() for person in self.people])}'

    def __add__(self, other):
        return Group(self.name + ' ' + other.name, self.people + other.people)

    def __len__(self):
        return len(self.people)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.people):
            person = self.people[self.index]
            stored = f"Person {self.index}: {person}"
            self.index += 1
            return stored
        else:
            self.index = 0
            raise StopIteration

    def __getitem__(self, item):
        return f"Person {self.index}: {self.people[item]}"
