from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver


class NauticalCatchChallengeApp:
    FISH_TYPES = {'PredatoryFish': PredatoryFish, 'DeepSeaFish': DeepSeaFish}
    DIVER_TYPES = {'FreeDiver': FreeDiver, 'ScubaDiver': ScubaDiver}

    def __init__(self):
        self.divers = []
        self.fish_list = []


    def dive_into_competition(self, diver_type: str, diver_name: str):

        if diver_type not in self.DIVER_TYPES:
            return f'{diver_type} is not allowed in our competition.'

        if self.__get_diver_by_name(diver_name):
            return f'{diver_name} is already a participant.'

        self.divers.append(self.DIVER_TYPES[diver_type](diver_name))
        return f'{diver_name} is successfully registered for the competition as a {diver_type}.'

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.FISH_TYPES:
            return f'{fish_type} is forbidden for chasing in our competition.'

        if self.__get_fish_by_name(fish_name):
            return f'{fish_name} is already permitted.'

        self.fish_list.append(self.FISH_TYPES[fish_type](fish_name, points))
        return f'{fish_name} is allowed for chasing as a {fish_type}.'

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self.__get_diver_by_name(diver_name)

        if not diver:
            return f'{diver_name} is not registered for the competition.'

        fish = self.__get_fish_by_name(fish_name)

        if not fish:
            return f'The {fish_name} is not allowed to be caught in this competition.'

        if diver.has_health_issue:
            return f'{diver_name} will not be allowed to dive, due to health issues.'

        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f'{diver_name} hits a {fish.points}pt. {fish_name}.'

        elif diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f'{diver_name} missed a good {fish_name}.'

        else:

            if is_lucky:
                diver.hit(fish)
                return f'{diver_name} hits a {fish.points}pt. {fish_name}.'

            diver.miss(fish.time_to_catch)
            return f'{diver_name} missed a good {fish_name}.'

    def health_recovery(self):
        counter = 0
        for diver in self.divers:
            if diver.has_health_issue:
                counter += 1
                diver.update_health_status()
                diver.renew_oxy()
        return f'Divers recovered: {counter}'

    def diver_catch_report(self, diver_name: str):
        diver = self.__get_diver_by_name(diver_name)
        report = f'**{diver.name} Catch Report**\n'
        for fish in diver.catch:
            report += fish.fish_details() + '\n'
        return report.rstrip()

    def competition_statistics(self):
        sorted_divers = sorted([diver for diver in self.divers if not diver.has_health_issue], key=lambda diver: (-len(diver.catch), diver.name))
        statistics = '**Nautical Catch Challenge Statistics**\n'
        for diver in sorted_divers:
            statistics += str(diver) + '\n'
        return statistics.rstrip()

    def __get_diver_by_name(self, diver_name):
        for diver in self.divers:
            if diver.name == diver_name:
                return diver

    def __get_fish_by_name(self, fish_name):
        for fish in self.fish_list:
            if fish.name == fish_name:
                return fish

