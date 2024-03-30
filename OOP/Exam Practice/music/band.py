class Band:

    def __init__(self, name: str):
        self.__name = name
        self.members = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(self.__name) == 0:
            raise ValueError('Band name should contain at least one character!')
        self.__name = value

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."
