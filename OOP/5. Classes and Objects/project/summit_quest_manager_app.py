from exam_practice.climbers.arctic_climber import ArcticClimber
from exam_practice.climbers.summit_climber import SummitClimber
from exam_practice.peaks.arctic_peak import ArcticPeak
from exam_practice.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    ALL_CLIMBER_NAMES = []

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):

        if climber_type not in ['ArcticClimber', 'SummitClimber']:
            return f"{climber_type} doesn't exist in our register."

        if climber_name in self.ALL_CLIMBER_NAMES:
            return f"{climber_name} has been already registered."

        if climber_type == 'ArcticClimber':
            climber = ArcticClimber(climber_name)
        else:
            climber = SummitClimber(climber_name)

        self.climbers.append(climber)
        self.ALL_CLIMBER_NAMES.append(climber_name)

        return f'{climber_name} is successfully registered as a {climber_type}.'

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):

        if peak_type not in ["ArcticPeak", "SummitPeak"]:
            return f"{peak_type} is an unknown type of peak."

        if peak_type == 'ArcticPeak':
            peak = ArcticPeak(peak_name, peak_elevation)
        else:
            peak = SummitPeak(peak_name, peak_elevation)

        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear):
        climber = self._get_climber_by_name(climber_name)
        peak = self._get_peak_by_name(peak_name)

        required_gear = peak.get_recommended_gear()
        missing_gear = set(required_gear) - set(gear)
        if missing_gear:
            climber.is_prepared = False
            sorted_missing_gear = sorted(missing_gear)
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted_missing_gear)}."
        else:
            return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name, peak_name):
        climber = self._get_climber_by_name(climber_name)
        peak = self._get_peak_by_name(peak_name)

        if climber is None:
            return f"Climber {climber_name} is not registered yet."

        if peak is None:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        else:
            climber.rest()
            return f'{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest.'

    def get_statistics(self):
        sorted_climbers = sorted([climber for climber in self.climbers if climber.conquered_peaks],
                                 key=lambda climber: (-len(climber.conquered_peaks), climber.name))

        result = [
            f"Total climbed peaks: {len(self.peaks)}",
            "**Climber's statistics:**"
        ]

        climber_statistics = "\n".join(str(c) for c in sorted_climbers)
        result.append(climber_statistics)

        return '\n'.join(result)

    # helper methods
    def _get_climber_by_name(self, climber_name: str):
        for climber in self.climbers:
            if climber.name == climber_name:
                return climber

    def _get_peak_by_name(self, peak_name: str):
        for peak in self.peaks:
            if peak.name == peak_name:
                return peak
