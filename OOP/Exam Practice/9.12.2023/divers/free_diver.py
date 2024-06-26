from exam_practice.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    def __init__(self, name):
        super().__init__(name, 120)

    def miss(self, time_to_catch: int):
        used_oxy = round(time_to_catch * 0.6)
        if self.oxygen_level < used_oxy:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= used_oxy

    def renew_oxy(self):
        self.oxygen_level = 120
