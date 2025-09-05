# Атрибути: name, private __players (списък от Player)
# Методи:
# add_player(player) → добавя играч
# total_goals() → връща сумата на головете на всички играчи
# best_scorer() → връща играча с най-много голове
from homework.task_1_sports_league.player import Player


class Team:
    def __init__(self, name: str)->None:
        self.name: str = name
        self.__players: list[Player] = []

    def add_player(self, player):
        self.__players.append(player)

    def total_goals(self):
        #total_goals = 0
        return sum(player.get_goals() for player in self.__players)

    def best_scorer(self):
        if not self.__players:
            return None

        best_scorer_player = self.__players[0]
        for player in self.__players[1:]:
            if player.get_goals() > best_scorer_player.get_goals():
                best_scorer_player = player
        return best_scorer_player