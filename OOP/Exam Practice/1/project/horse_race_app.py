from horse_specification.horse import Horse
from horse_specification.appaloosa import Appaloosa
from horse_specification.thoroughbred import Thoroughbred
from music.jockey import Jockey
from music.horse_race import HorseRace


class HorseRaceApp:
    def __init__(self):
        self.horses: list[Horse] = []
        self.jockeys: list[Jockey] = []
        self.horse_races: list[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        if horse_type not in ['Appaloosa', 'Thoroughbred']:
            return

        if horse_name in self._get_horse_names():
            raise Exception('Horse {} has been already added!'.format(horse_name))

        horse = self._create_horse_by_type(horse_type, horse_name, horse_speed)
        self.horses.append(horse)
        return '{} horse {} is added.'.format(horse_type, horse_name)

    def add_jockey(self, jockey_name: str, age: int):

        if jockey_name in self._get_jockey_names():
            raise Exception('Jockey {} has been already added!'.format(jockey_name))

        self.jockeys.append(Jockey(jockey_name, age))
        return 'Jockey {} is added.'.format(jockey_name)

    def create_horse_race(self, race_type):

        if race_type in self._get_race_types():
            raise Exception('Race {} has been already created!'.format(race_type))

        horse_race = HorseRace(race_type)
        self.horse_races.append(horse_race)
        return 'Race {} is created.'.format(race_type)

    def add_horse_to_jockey(self, jokey_name: str, horse_type: str):
        free_horses = self._get_horse_types(horse_type)
        jokey = self._get_jokey_by_name(jokey_name)

        if jokey_name not in self._get_jockey_names():
            raise Exception('Jockey {} could not be found!'.format(jokey_name))

        if jokey.horse:
            return 'Jockey {} already has a horse.'.format(jokey_name)

        if not free_horses:
            raise Exception('Horse breed {} could not be found!'.format(horse_type))

        horse = free_horses[-1]
        jokey.horse = horse
        horse.is_taken = True
        return 'Jockey {} will ride the horse {}.'.format(jokey_name, horse.name)

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        if race_type not in self._get_race_types():
            raise Exception('Race {} could not be found!'.format(race_type))
        race = self._get_race_by_type(race_type)

        if jockey_name not in self._get_jockey_names():
            raise Exception('Jockey {} could not be found!'.format(jockey_name))

        jokey = self._get_jokey_by_name(jockey_name)
        if jokey.horse is None:
            raise Exception('Jockey {} cannot enter race without a horse!'.format(jockey_name))

        if jokey in race.jockeys:
            return 'Jockey {} has been already added to the {} race.'.format(jockey_name, race_type)

        race.jockeys.append(jokey)
        return 'Jockey {} added to the {} race.'.format(jockey_name, race_type)

    def start_horse_race(self, race_type):
        if race_type not in self._get_race_types():
            raise Exception('Race {} could not be found!'.format(race_type))

        race = self._get_race_by_type(race_type)
        if len(race.jockeys) < 2:
            raise Exception('Horse race {} needs at least two participants!'.format(race_type))

        winner: Jokey = self._get_winner(race.jockeys)
        speed = winner.horse.speed
        horse_name = winner.horse.name
        return "The winner of the {} race, with a speed of {}km/h is {}! Winner's horse: {}.".format(race_type, speed, winner.name, horse_name)

    # helper methods

    @staticmethod
    def _create_horse_by_type(horse_type: str, horse_name: str, horse_speed: int) -> Horse:
        if horse_type == "Appaloosa":
            return Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            return Thoroughbred(horse_name, horse_speed)

    def _get_horse_names(self) -> list:
        return [horse.name for horse in self.horses]

    def _get_jockey_names(self) -> list:
        return [jockey.name for jockey in self.jockeys]

    def _get_jokey_by_name(self, jokey_name: str):
        return [jockey for jockey in self.jockeys if jockey.name == jokey_name][0]

    def _get_race_types(self) -> list:
        return [race.race_type for race in self.horse_races]

    def _get_horse_types(self, horse_type) -> list:
        if horse_type == 'Appaloosa':
            return [horse for horse in self.horses if isinstance(horse, Appaloosa) and not horse.is_taken]
        else:
            return [horse for horse in self.horses if isinstance(horse, Thoroughbred) and not horse.is_taken]

    def _get_race_by_type(self, race_type):
        return [race for race in self.horse_races if race.race_type == race_type][0]

    @staticmethod
    def _get_winner(jockeys):
        if len(jockeys) < 2:
            raise Exception("Horse race needs at least two participants!")
        winner = max(jockeys, key=lambda jockey: jockey.horse.speed)
        return winner




