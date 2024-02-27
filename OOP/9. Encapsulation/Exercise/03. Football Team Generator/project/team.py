class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self,player):
        if player in self.__players:
            return f'Player {player.name} has already joined'
        self.__players.append(player)
        return f'Player {player.name} joined team {self.__name}'

    def remove_player(self,player_name):
        names = [player.name for player in self.__players]
        if player_name in names:
            return self.__players.pop(names.index(player_name))
        return f'Player {player_name} not found'

