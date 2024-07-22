from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    DEFAULT_OXYGEN_LEVEL = 120
    DECREASE_FACTOR = 0.6

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_OXYGEN_LEVEL)

    def miss(self, time_to_catch):
        value_to_decrease = int(self.DECREASE_FACTOR * time_to_catch)

        if self.oxygen_level > value_to_decrease:
            self.oxygen_level -= value_to_decrease
        else:
            self.oxygen_level = 0

        if self.oxygen_level == 0:
            self.has_health_issue = True

    def renew_oxy(self):
        self.oxygen_level = self.DEFAULT_OXYGEN_LEVEL
