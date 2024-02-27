class Topping:
    def __init__(self, topping_type: str, weight: float):
        self.__topping_type = topping_type
        self.__weight = weight
        if self.topping_type == "":
            raise ValueError("The topping type cannot be an empty string")
        if self.weight <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, new_topping_type):
        if new_topping_type == "":
            raise ValueError("The topping type cannot be an empty string")
        self.__topping_type = new_topping_type

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        if new_weight <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight = new_weight
