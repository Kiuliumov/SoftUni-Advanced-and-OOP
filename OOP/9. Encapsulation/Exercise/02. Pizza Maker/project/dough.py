class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        self.__flour_type = flour_type
        self.__baking_technique = baking_technique
        self.__weight = weight
        if self.__flour_type == '':
            raise ValueError('The flour type cannot be an empty string')
        if self.__baking_technique == '':
            raise ValueError('The baking technique cannot be an empty string')
        if self.__weight <= 0:
            raise ValueError("The weight cannot be less or equal to zero")

    @property
    def flour_type(self):
        return self.__flour_type

    @flour_type.setter
    def flour_type(self, new_flour_type):
        if new_flour_type == '':
            raise ValueError('The flour type cannot be an empty string')
        self.__flour_type = new_flour_type

    @property
    def baking_technique(self):
        return self.__baking_technique

    @baking_technique.setter
    def baking_technique(self, new_baking_technique):
        if new_baking_technique == '':
            raise ValueError('The baking technique cannot be an empty string')
        self.__baking_technique = new_baking_technique

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        if new_weight <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight = new_weight
