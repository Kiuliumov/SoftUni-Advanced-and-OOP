class Player:

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return 'Skill {} added to the collection of the player {}'.format(skill_name, self.name)
        return 'Skill already added'

    def player_info(self):
        info = 'Name: {}\n'.format(self.name)
        info += 'Guild: {}\n'.format(self.guild)
        info += 'HP: {}\n'.format(self.hp)
        info += 'MP: {}\n'.format(self.mp)
        for skill, mana_cost in self.skills.items():
            info += '==={} - {}\n'.format(skill, mana_cost)
        return info
