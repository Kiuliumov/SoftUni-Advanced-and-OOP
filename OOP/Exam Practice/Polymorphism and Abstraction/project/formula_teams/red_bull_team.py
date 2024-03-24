from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = -250000
        if race_pos in [10, 9]:
            revenue += 10000
        if race_pos in [8, 7, 6, 5, 4, 3]:
            revenue += 20000
        if race_pos in [2]:
            revenue += 800000
            revenue += 20000
        if race_pos in [1]:
            revenue += 1500000
            revenue += 20000
        self.budget += revenue
        return f'The revenue after the race is {revenue}$. Current budget {self.budget}$'
