from abc import ABC, abstractmethod


class BaseVehicle(ABC):
    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float) -> None:
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage
        self.battery_level = 100
        self.is_damaged = False

    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, value: str) -> None:
        if value.strip() == '':
            raise ValueError('Brand cannot be empty!')
        self.__brand = value

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, value: str) -> None:
        if value.strip() == '':
            raise ValueError('Model cannot be empty!')
        self.__model = value

    @property
    def license_plate_number(self) -> str:
        return self.__license_plate_number

    @license_plate_number.setter
    def license_plate_number(self, value: str) -> None:
        if value.strip() == '':
            raise ValueError('License plate number is required!')
        self.__license_plate_number = value

    @abstractmethod
    def drive(self, mileage_float) -> None:
        pass

    def recharge(self) -> None:
        self.battery_level = 100

    def change_status(self) -> None:
        self.is_damaged = not self.is_damaged

    def __str__(self) -> str:
        return ('{} {} License plate: {} Battery: {}% Status: {}'.format
                (self.brand, self.model, self.license_plate_number, self.battery_level, 'Damaged' if self.is_damaged else 'OK'))
