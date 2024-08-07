from project.services.base_service import BaseService


class SecondaryService(BaseService):
    INITIAL_CAPACITY = 15

    def __init__(self, name):
        super().__init__(name, self.INITIAL_CAPACITY)

    def details(self):
        return f"{self.name} Secondary Service:\nRobots: {' '.join([robot.name for robot in self.robots]) if self.robots else 'none'}"
