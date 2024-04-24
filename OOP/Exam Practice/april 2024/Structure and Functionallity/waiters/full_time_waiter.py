from project.waiters.base_waiter import BaseWaiter


class FullTimeWaiter(BaseWaiter):
    HOURLY_WAGE = 15

    def __init__(self, name, hours_worked):
        super().__init__(name, hours_worked)

    def calculate_earnings(self):
        return self.hours_worked * self.HOURLY_WAGE

    def report_shift(self):
        return f'{self.name} worked a full-time shift of {self.hours_worked} hours.'