class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):

        if player in self.players:
            return 'Player ' + player.name + ' is already in the guild.'

        if player.guild != 'Unaffiliated':
            return 'Player ' + player.name + ' is in another guild.'

        self.players.append(player)
        player.guild = self.name
        return 'Welcome player ' + player.name + ' to the guild ' + self.name

    def kick_player(self, player_name):
        player = [player for player in self.players if player_name == player.name]

        if not player:
            return 'Player {} is not in the guild.'.format(player_name)
        player = player[0]
        self.players.remove(player)
        player.guild = 'Unaffiliated'
        return 'Player {} has been removed from the guild.'.format(player_name)

    def guild_info(self):
        info = 'Guild: ' + self.name
        for player in self.players:
            info += '\n' + player.player_info()
        return info
