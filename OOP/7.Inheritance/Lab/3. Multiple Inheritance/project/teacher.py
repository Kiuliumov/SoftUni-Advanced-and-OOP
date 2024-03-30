from music.person import Person
from music.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'
