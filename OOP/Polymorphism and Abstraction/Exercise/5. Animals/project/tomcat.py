from project.cat import Cat


class Tomcat(Cat):
    CLASS_NAME = 'Tomcat'

    def __init__(self, name, age):
        super().__init__(name, age, 'Male')
        self.sound = 'Hiss'
