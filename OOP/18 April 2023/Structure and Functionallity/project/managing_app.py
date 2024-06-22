from project.user import User
from project.route import Route
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.passenger_car import PassengerCar
from project.vehicles.cargo_van import CargoVan
from typing import List


class ManagingApp:
    CAR_TYPES = {'PassengerCar': PassengerCar, 'CargoVan': CargoVan}

    def __init__(self) -> None:
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str) -> str:

        if self.__get_user_by_driving_license_number(driving_license_number):
            return '{} has already been registered to our platform.'.format(driving_license_number)

        user: User = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return '{} {} was successfully registered under DLN-{}'.format(first_name, last_name, driving_license_number)

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str) -> str:

        if vehicle_type not in self.CAR_TYPES:
            return 'Vehicle type {} is inaccessible.'.format(vehicle_type)

        if self.__get_vehicle_by_license_plate_number(license_plate_number):
            return '{} belongs to another vehicle.'.format(license_plate_number)

        vehicle: BaseVehicle = self.CAR_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return '{} {} was successfully uploaded with LPN-{}.'.format(brand, model, license_plate_number)

    def allow_route(self, start_point: str, end_point: str, length: float) -> str:
        route_id = len(self.routes) + 1

        if self.__check_if_route_is_equal(start_point, end_point, length):
            return '{}/{} - {} km had already been added to our platform.'.format(start_point, end_point, length)

        if self.__check_if_shorter_route_exists(start_point, end_point, length):
            return '{}/{} shorter route had already been added to our platform.'.format(start_point, end_point)

        route: Route = Route(start_point, end_point, length, route_id)
        self.routes.append(route)

        self.__lock_if_longer_route_exists(start_point, end_point, length)
        return '{}/{} - {} km is unlocked and available to use.'.format(start_point, end_point, length)

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int, is_accident_happened: bool) -> str:
        user: User = self.__get_user_by_driving_license_number(driving_license_number)
        vehicle: BaseVehicle = self.__get_vehicle_by_license_plate_number(license_plate_number)
        route: Route = self.__get_route_by_id(route_id)

        if user.is_blocked:
            return 'User {} is blocked in the platform! This trip is not allowed.'.format(driving_license_number)

        if vehicle.is_damaged:
            return 'Vehicle {} is damaged! This trip is not allowed.'.format(license_plate_number)

        if route.is_locked:
            return 'Route {} is locked! This trip is not allowed.'.format(route_id)

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return vehicle.__str__()

    def repair_vehicles(self, count: int) -> str:
        sorted_vehicles = sorted([vehicle for vehicle in self.vehicles if vehicle.is_damaged], key=lambda vehicle: (vehicle.brand, vehicle.model))

        repaired = 0

        for i in range(count):
            if i < len(sorted_vehicles):
                sorted_vehicles[i].change_status()
                sorted_vehicles[i].recharge()
                repaired += 1



        return '{} vehicles were successfully repaired!'.format(repaired)


    def users_report(self) -> str:
        sorted_users = sorted(self.users, key=lambda user: -user.rating)

        string = '*** E-Drive-Rent ***'

        for user in sorted_users:
            string += '\n{}'.format(user.__str__())

        return string



    def __get_user_by_driving_license_number(self, driving_license_number: str) -> User:
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return user

    def __get_vehicle_by_license_plate_number(self, license_plate_number: str) -> BaseVehicle:
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return vehicle

    def __check_if_route_is_equal(self, start_point: str, end_point: str, length: float) -> bool:
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return True

    def __check_if_shorter_route_exists(self, start_point, end_point, length):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length < length:
                return True

    def __lock_if_longer_route_exists(self, start_point, end_point, length):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True

    def __get_route_by_id(self, route_id: int) -> Route:
        for route in self.routes:
            if route.route_id == route_id:
                return route
