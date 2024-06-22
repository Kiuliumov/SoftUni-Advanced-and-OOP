class User:
    def __init__(self, first_name: str, last_name: str, driving_license_number: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.driving_license_number = driving_license_number
        self.rating = 0
        self.is_blocked = False

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        if value.strip() == '':
            raise ValueError('First name cannot be empty!')
        self.__first_name = value

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        if value.strip() == '':
            raise ValueError('Last name cannot be empty!')
        self.__last_name = value

    @property
    def driving_license_number(self) -> str:
        return self.__driving_license_number

    @driving_license_number.setter
    def driving_license_number(self, value: str) -> None:
        if value.strip() == '':
            raise ValueError('Driving license number is required!')
        self.__driving_license_number = value

    @property
    def rating(self) -> float:
        return self.__rating

    @rating.setter
    def rating(self, value: float) -> None:
        if value < 0:
            raise ValueError('Users rating cannot be negative!')
        self.__rating = value

    def increase_rating(self) -> None:
        self.rating = self.rating + 0.5
        if self.rating > 10:
            self.rating = 10

    def decrease_rating(self) -> None:
        if self.rating - 2 < 0:
            self.rating = 0
            self.is_blocked = True
            return None
        self.rating = self.rating - 2

    def __str__(self) -> str:
        return ('{} {} Driving license: {} Rating: {}'.format
                (self.first_name, self.last_name, self.driving_license_number, self.rating))
