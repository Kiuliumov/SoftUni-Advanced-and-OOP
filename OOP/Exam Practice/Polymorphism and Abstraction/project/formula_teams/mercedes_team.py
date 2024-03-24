from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = -200000
        if race_pos in [7, 6]:
            revenue += 50000
        if race_pos in [5, 4]:
            revenue += 100000
        if race_pos in [3, 2]:
            revenue += 500000
            revenue += 100000
        if race_pos in [1]:
            revenue += 1000000
            revenue += 100000
        self.budget += revenue

        return f'The revenue after the race is {revenue}$. Current budget {self.budget}$'

