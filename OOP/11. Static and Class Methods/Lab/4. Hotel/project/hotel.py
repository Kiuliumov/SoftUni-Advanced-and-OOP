class Hotel:
    def __init__(self, name: str, guests=0):
        self.name = name
        self.guests = guests
        self.rooms = []

    @classmethod
    def from_stars(cls, stars: int):
        return cls(f'{stars} stars Hotel')

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, number_of_people: int):
        room_numbers = [room.number for room in self.rooms]
        if room_number in room_numbers:
            var = self.rooms[room_numbers.index(room_number)].take_room(number_of_people)
            if var is None:
                self.guests += self.rooms[room_numbers.index(room_number)].guests


    def free_room(self, room_number):
        room_numbers = [room.number for room in self.rooms]
        self.guests -= self.rooms[room_numbers.index(room_number)].guests
        self.rooms[room_numbers.index(room_number)].free_room()
    def status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        return ('Hotel {} has {} total guests'.format(self.name, self.guests) +
                '\nFree rooms: {}').format(', '.join(free_rooms) +
                                           '\nTaken rooms: {}').format((', '.join(taken_rooms)))
