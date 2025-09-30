# Team
# Атрибути: name, private __players
# Методи: add_player(), total_goals(), best_scorer()
from exercises_hard_tasks2.sports_league.player import Player


class Team:
    def __init__(self, name):
        self.name = name
        self.__players: list[Player] = []

    def add_player(self, curr_player=object) -> None:
        self.__players.append(curr_player)

    def total_goals(self) -> int:
        return sum([curr_player.get_goals() for curr_player in self.__players])

    def best_scorer(self):
        best_player = None
        most_goals = 0
        for curr_player in self.__players:
            if curr_player.get_goals() >= most_goals:
                most_goals = curr_player.get_goals()
                best_player = curr_player
        return best_player


