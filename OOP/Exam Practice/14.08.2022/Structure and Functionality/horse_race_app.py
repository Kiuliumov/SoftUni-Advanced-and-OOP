from project.jockey import Jockey
from project.horse_race import HorseRace
from project.horse_specification.horse import Horse
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from typing import List



class HorseRaceApp:
    VALID_HORSE_TYPES = {'Appaloosa': Appaloosa, 'Thoroughbred': Thoroughbred}
    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type, horse_name, horse_speed):

        if self.get_horse_by_name(horse_name):
            raise Exception(f'Horse {horse_name} has been already added!')

        if horse_type in self.VALID_HORSE_TYPES:
            self.horses.append(self.VALID_HORSE_TYPES[horse_type](name=horse_name, speed=horse_speed))
            return f'{horse_type} horse {horse_name} is added.'

    def add_jockey(self, jockey_name, age):

        if self.get_jockey_by_name(jockey_name):
            raise Exception(f'Jockey {jockey_name} has been already added!')

        self.jockeys.append(Jockey(name=jockey_name, age=age))
        return f'Jockey {jockey_name} is added.'

    def create_horse_race(self, race_type):

        if self.get_race_by_type(race_type):
            raise Exception(f'Race {race_type} has been already created!')

        self.horse_races.append(HorseRace(race_type=race_type))
        return f'Race {race_type} is created.'

    def add_horse_to_jockey(self, jockey_name, horse_type):
        jockey = self.get_jockey_by_name(name=jockey_name)
        horse = self.get_horse_by_type(horse_type)


        if not jockey:
            raise Exception(f'Jockey {jockey_name} could not be found!')

        if not horse:
            raise Exception(f'Horse breed {horse_type} could not be found!')

        if jockey.horse:
            return f'Jockey {jockey_name} already has a horse.'

        horse.is_taken = True
        jockey.horse = horse
        return f'Jockey {jockey_name} will ride the horse {horse.name}.'

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        horse_race = self.get_race_by_type(race_type)
        jockey = self.get_jockey_by_name(jockey_name)

        if not horse_race:
            raise Exception(f'Race {race_type} could not be found!')

        if not jockey:
            raise Exception(f'Jockey {jockey_name} could not be found!')

        if not jockey.horse:
            raise Exception(f'Jockey {jockey_name} cannot race without a horse!')

        if jockey in horse_race.jockeys:
            return f'Jockey {jockey_name} has been already added to the {race_type} race.'

        horse_race.jockeys.append(jockey)
        return f'Jockey {jockey_name} added to the {race_type} race.'


    def start_horse_race(self, race_type):
        horse_race = self.get_race_by_type(race_type)

        if not horse_race:
            raise Exception(f'Race {race_type} could not be found!')

        if len(horse_race.jockeys) < 2:
            raise Exception(f'Horse race {race_type} needs at least two participants!')

        winner_speed = float('-inf')

        for jockey in horse_race.jockeys:
            if jockey.horse.speed > winner_speed:
                winner_speed = jockey.horse.speed
                winner = jockey

        return f"The winner of the {race_type} race, with a speed of {winner_speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."


    # helper methods

    def get_jockey_by_name(self, name) -> Jockey:
        for jockey in self.jockeys:
            if jockey.name == name:
                return jockey
        return None

    def get_horse_by_name(self, name) -> Horse:
        for horse in self.horses:
            if horse.name == name:
                return horse
        return None

    def get_race_by_type(self, race_type) -> HorseRace:
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        return None

    def get_horse_by_type(self, horse_type) -> Horse:
        for horse in reversed(self.horses):
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                return horse
        return None

