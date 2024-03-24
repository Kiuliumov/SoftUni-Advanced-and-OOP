from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name):
        super().__init__(name, 15)
        self.type = 'SecondaryService'

    def details(self):
        robots_as_string = ' '.join([robot.name for robot in self.robots])
        return f'{self.name} Secondary Service:\nRobots: {robots_as_string if self.robots else "none"}'
