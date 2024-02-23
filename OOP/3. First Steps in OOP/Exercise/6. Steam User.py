class SteamUser:
    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours = 0
        self.games_count = len(games)

    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return f'{self.username} is playing {game}'
        else:
            return f'{game} is not in library'

    def buy_game(self, game):
        if game not in self.games:
            self.games.append(game)
            self.games_count += 1
            return f'{self.username} bought {game}'
        else:
            return f'{game} is already in your library'

    def status(self):
        return f'{self.username} has {self.games_count} games. Total play time: {self.played_hours}'

