from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService




class RobotsManagingApp:
    ROBOTS = {'MaleRobot': MaleRobot, 'FemaleRobot': FemaleRobot}
    SERVICES = {'MainService': MainService, 'SecondaryService': SecondaryService}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type, service_name):

        if service_type not in self.SERVICES:
            raise Exception('Invalid service type!')

        self.services.append(self.SERVICES[service_type](service_name))
        return f'{service_type} is successfully added.'

    def add_robot(self, robot_type, name, kind, price):

        if robot_type not in self.ROBOTS:
            raise Exception('Invalid robot type!')

        self.robots.append(self.ROBOTS[robot_type](name, kind, price))
        return f'{robot_type} is successfully added.'

    def add_robot_to_service(self, robot_name, service_name):
        robot = self.__get_robot_by_name(robot_name)
        service = self.__get_service_by_name(service_name)
        mismatch = [isinstance(robot, MaleRobot) and isinstance(service, SecondaryService), isinstance(robot, FemaleRobot) and isinstance(service, MainService)]

        if any(mismatch):
            return 'Unsuitable service.'

        if len(service.robots) == service.capacity:
            raise Exception('Not enough capacity for this robot!')

        service.robots.append(robot)
        self.robots.remove(robot)
        return f'Successfully added {robot_name} to {service_name}.'

    def remove_robot_from_service(self, robot_name, service_name):
        service = self.__get_service_by_name(service_name)
        robot = self.__get_robot_from_service(service, robot_name)


        if robot_name not in [robot.name for robot in service.robots]:
            raise Exception('No such robot in this service!')

        service.robots.remove(robot)
        self.robots.append(robot)
        return f'Successfully removed {robot_name} from {service_name}.'

    def feed_all_robots_from_service(self, service_name):
        service = self.__get_service_by_name(service_name)

        counter = 0

        for robot in service.robots:
            robot.eating()
            counter += 1
        return f'Robots fed: {counter}.'

    def service_price(self, service_name):
        service = self.__get_service_by_name(service_name)

        total_price = sum([robot.price for robot in service.robots])
        return f'The value of service {service_name} is {total_price:.2f}.'

    def __str__(self):
        string = ''

        for service in self.services:
            string += service.details() + '\n'

        return string.rstrip()

    def __get_robot_by_name(self, robot_name):
        for robot in self.robots:
            if robot.name == robot_name:
                return robot
        return None

    def __get_service_by_name(self, service_name):
        for service in self.services:
            if service.name == service_name:
                return service
        return None

    @staticmethod
    def __get_robot_from_service(service, robot_name):

        for robot in service.robots:
            if robot.name == robot_name:
                return robot
        return None

    def __get_service_by_robot(self, service, robot_name):
        pass