# Tournament
# Атрибути: private __players
# Методи: add_player(player)
# leaderboard()
from player import Player


class Tournament:
    def __init__(self):
        self.__players: list[Player] = []

    def add_player(self, cur_player):
        self.__players.append(cur_player)

    def leaderboard(self):
        return [(player.name, player.get_score()) for player in list(sorted(self.__players, key=lambda cur_player: -cur_player.get_score()))]
