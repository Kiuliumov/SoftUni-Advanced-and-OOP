class HorseRace:
    def __init__(self, race_type):
        self.__race_type = race_type
        self.jockeys = []

    @property
    def race_type(self):
        if self.__race_type not in ['Spring', 'Summer', 'Autumn', 'Winter']:
            raise ValueError('Race type does not exist!')
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        if value not in ['Spring', 'Summer', 'Autumn', 'Winter']:
            raise ValueError('Race type does not exist!')
        self.__race_type = value
