from exam_practice.car.car import Car
from exam_practice.car.muscle_car import MuscleCar
from exam_practice.car.sports_car import SportsCar
from exam_practice.driver import Driver
from exam_practice.race import Race


class Controller:
    CAR_TYPES = {'MuscleCar': MuscleCar, 'SportsCar': SportsCar}

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type, model, speed_limit):
        if car_type in self.CAR_TYPES:
            if self.get_car_by_model(model):
                raise Exception(f'Car {model} is already created!')

            car = self.CAR_TYPES[car_type](model, speed_limit)
            self.cars.append(car)
            return f'{car_type} {model} is created.'

    def create_driver(self, driver_name):
        if self.get_driver_by_name(driver_name):
            raise Exception(f'Driver {driver_name} is already created!')
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f'Driver {driver_name} is created.'

    def create_race(self, race_name):
        if self.get_race_by_name(race_name):
            raise Exception(f'Race {race_name} is already created!')

        race = Race(race_name)
        self.races.append(race)
        return f'Race {race_name} is created.'

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.get_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = self.get_last_car_by_type(car_type)
        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:
            old_model = driver.car.model
            driver.car.is_taken = False

            driver.car = car
            car.is_taken = True
            return f'Driver {driver_name} changed his car from {old_model} to {driver.car.model}.'

        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.get_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self.get_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        else:
            race.drivers.append(driver)
            return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.get_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winner, second, third = sorted(race.drivers, key=lambda x: x.car.speed_limit, reverse=True)[:3]
        winner.number_of_wins += 1
        second.number_of_wins += 1
        third.number_of_wins += 1

        string = ''
        for winner in [winner, second, third]:
            string += f'Driver {winner.name} wins the {race_name} race with a speed of {winner.car.speed_limit}.\n'
        return string.rstrip()

    # helper methods

    def get_car_by_model(self, model) -> Car:
        for car in self.cars:
            if car.model == model:
                return car
        return None

    def get_driver_by_name(self, name) -> Driver:
        for driver in self.drivers:
            if driver.name == name:
                return driver
        return None

    def get_race_by_name(self, race_name) -> Race:
        for race in self.races:
            if race.name == race_name:
                return race
        return None

    def get_last_car_by_type(self, car_type):
        for car in reversed(self.cars):
            if car.get_type() == car_type and not car.is_taken:
                return car
        return None
