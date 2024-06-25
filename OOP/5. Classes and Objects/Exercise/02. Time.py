class Time:

    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return '{:02d}:{:02d}:{:02d}'.format(self.hours, self.minutes, self.seconds)

    def next_second(self):
        if self.seconds == 59:
            self.seconds = 0
            if self.minutes == 59:
                self.minutes =0
                if self.hours == 23:
                    self.hours = 0
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1
        return self.get_time()

