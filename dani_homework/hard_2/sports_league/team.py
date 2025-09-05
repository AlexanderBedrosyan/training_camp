# Team
# Атрибути: name, private __players
# Методи: add_player(), total_goals(), best_scorer()
from player import Player


class Team:
    def __init__(self, name:str):
        self.name = name
        self.__players: list[Player] = []

    def add_player(self, current_player):
        self.__players.append(current_player)

    def total_goals(self):
        total_goals = 0
        for current_player in self.__players:
            total_goals += current_player.get_goals()
        return total_goals

    def best_scorer(self):
        if not self.__players:
            return None
        return max(self.__players, key=lambda player: player.get_goals())

    def __str__(self):
        return f"Team {self.name} with {len(self.__players)} players"

# player1 = Player("Messi", "Forward", 2)
# player2 = Player("Ronaldo", "Forward", 1)
#
# player1.score_goals()
# player1.score_goals()
# player2.score_goals()
#
# t = Team("Glarus")
# t.add_player(player1)
# t.add_player(player2)
#
# print(t.total_goals())          # 3
# print(t.best_scorer())