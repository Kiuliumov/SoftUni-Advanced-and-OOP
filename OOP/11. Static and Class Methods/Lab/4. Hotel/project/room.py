class Room:
    def __init__(self, number: int, capacity: int,guests = 0):
        self.number = number
        self.capacity = capacity
        self.guests = guests
        self.is_taken = False

    def take_room(self, people: int):
        if not self.is_taken and people <= self.capacity:
            self.is_taken = True
            self.guests += people
            return
        return 'Room number ' + str(self.number) + ' cannot be taken'

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.guests = 0
            return
        return 'Room number ' + str(self.number) + ' is not taken'
