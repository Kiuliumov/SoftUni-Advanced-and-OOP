from music.band import Band
from music.band_members.musician import Musician
from music.band_members.singer import Singer
from music.band_members.drummer import Drummer
from music.band_members.guitarist import Guitarist
from music.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = ['Guitarist', 'Drummer', 'Singer']

    def __init__(self):
        self.bands: list[Band] = []
        self.musicians: list[Musician] = []
        self.concerts: list[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError('Invalid musician type!')

        if name in self._get_musician_names():
            raise Exception(f'{name} is already a musician!')

        if musician_type == 'Guitarist':
            self.musicians.append(Guitarist(name=name, age=age))
        elif musician_type == 'Drummer':
            self.musicians.append(Drummer(name=name, age=age))
        elif musician_type == 'Singer':
            self.musicians.append(Singer(name=name, age=age))

        return f'{name} is now a {musician_type}.'

    def create_band(self, name: str):
        if name in self._get_band_names():
            raise Exception(f'{name} band is already created!')

        self.bands.append(Band(name=name))

        return f'{name} was created.'

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")
        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        if musician_name not in self._get_musician_names():
            raise Exception(f"{musician_name} isn't a musician!")

        if band_name not in self._get_band_names():
            raise Exception(f"{band_name} isn't a band!")

        band = self._get_band_by_name(band_name)
        musician = self._get_musician_by_name(musician_name)

        band.members.append(musician)
        return f'{musician_name} was added to {band_name}.'

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        if band_name not in self._get_band_names():
            raise Exception(f"{band_name} isn't a band!")

        band = self._get_band_by_name(band_name)

        if musician_name not in band.members:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        musician = self._get_musician_from_band_by_name(musician_name, band)
        band.members.remove(musician)
        return f'{musician_name} was removed from {band_name}.'

    def start_concert(self, concert_place, band_name):
        band = self._get_band_by_name(band_name)
        concert = self._get_concert_by_place(concert_place)
        for musician_type in ["Drummer", "Singer", "Guitarist"]:
            if not any(
                    filter(
                        lambda x: x.__class__.__name__ == musician_type,
                        band.members
                    )
                ):
                    raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == 'Rock':
            for band_member in band.members:
                    if band_member.__class__.__name__ == 'Drummer' and \
                            "play the drums with drumsticks" not in band_member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                    if band_member.__class__.__name__ == 'Singer' and "sing high pitch notes" not in band_member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                    if band_member.__class__.__name__ == 'Guitarist' and "play rock" not in band_member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Metal':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' and "play the drums with drumsticks" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and "sing low pitch notes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play metal" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Jazz':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' \
                        and "play the drums with drum brushes" not in band_member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' \
                        and ("sing low pitch notes" not in band_member.skills
                                or "sing high pitch notes" not in band_member.skills):
                            raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play jazz" not in band_member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."


    # helper methods
    def _get_musician_names(self):
        return [musician.name for musician in self.musicians]

    def _get_band_names(self):
        return [band.name for band in self.bands]

    def _get_band_by_name(self, name):
        band_index = self._get_band_names().index(name)
        return self.bands[band_index]

    def _get_concert_places(self):
        return [concert.place for concert in self.concerts]

    def _get_concert_by_place(self, concert_place):
        return self.concerts[self._get_concert_places().index(concert_place)]

    def _get_musician_by_name(self, name):
        return self.musicians[self._get_musician_names().index(name)]

    @staticmethod
    def _get_musician_from_band_by_name(name, band):
        return band.members[band.members.index(name)]
