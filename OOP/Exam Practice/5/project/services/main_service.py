from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name):
        super().__init__(name, 30)
        self.type = 'MainService'

    def details(self):
        robots_as_string = ' '.join([robot.name for robot in self.robots])
        return f'{self.name} Main Service:\nRobots: {robots_as_string if self.robots else "none"}'
