from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService

class RobotsManagingApp:
    SERVICE_TYPES = {'MainService': MainService, 'SecondaryService': SecondaryService}
    ROBOT_TYPES = {'MaleRobot': MaleRobot, 'FemaleRobot': FemaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []


    def add_service(self, service_type, name):

        if service_type not in self.SERVICE_TYPES:
            raise Exception('Invalid service type!')

        self.services.append(self.SERVICE_TYPES[service_type](name))
        return f'{service_type} is successfully added.'

    def add_robot(self, robot_type, name, kind, price):
        if robot_type not in self.ROBOT_TYPES:
            raise Exception('Invalid robot type!')
        self.robots.append(self.ROBOT_TYPES[robot_type](name, kind, price))
        return f'{robot_type} is successfully added.'
    def add_robot_to_service(self, robot_name, service_name):
        robot = self.__get_robot_by_name(robot_name)
        service = self.__get_service_by_name(service_name)

        if robot.__class__.__name__ == 'MaleRobot' and service.__class__.__name__ == 'SecondaryService' or robot.__class__.__name__ == 'FemaleRobot' and service.__class__.__name__ == 'MainService':
            return 'Unsuitable service.'

        if len(service.robots) == service.capacity:
            raise Exception('Not enough capacity for this robot!')

        service.robots.append(robot)
        self.robots.remove(robot)
        return f'Successfully added {robot_name} to {service_name}.'


    def remove_robot_from_service(self, robot_name, service_name):
        service = self.__get_service_by_name(service_name)
        robot = self.__get_robot_from_service(service, robot_name)

        if not robot:
            raise Exception('No such robot in this service!')

        service.robots.remove(robot)
        self.robots.append(robot)
        return f'Successfully removed {robot_name} from {service_name}.'

    def feed_all_robots_from_service(self, service_name):
        service = self.__get_service_by_name(service_name)
        for robot in service.robots:
            robot.eating()
        return f'Robots fed: {len(service.robots)}.'

    def service_price(self, service_name):
        service = self.__get_service_by_name(service_name)
        price = 0

        for robot in service.robots:
            price += robot.price

        return f'The value of service {service_name} is {price:.2f}.'


    def __str__(self):
        string = ''
        for service in self.services:
            string += service.details() + '\n'
        return string.rstrip()

    def __get_robot_by_name(self, robot_name):
        for robot in self.robots:
            if robot.name == robot_name:
                return robot

    def __get_service_by_name(self, service_name):
        for service in self.services:
            if service.name == service_name:
                return service

    def __get_robot_from_service(self, service, robot_name):
        for robot in service.robots:
            if robot.name == robot_name:
                return robot