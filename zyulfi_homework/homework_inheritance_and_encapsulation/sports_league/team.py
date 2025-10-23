# Атрибути: name, private __players (списък от Player)
# Методи:
# add_player(player) → добавя играч
# total_goals() → връща сумата на головете на всички играчи
# best_scorer() → връща играча с най-много голове
from player import Player

class Team:
    def __init__(self, name):
        self.name = name
        self.__players: list[Player] = []

    def add_player(self, curr_player=object):
        self.__players.append(curr_player)

    def total_goals(self) -> int:
        total_goals = 0
        for player in self.__players:
            total_goals += player.get_goals()
        return total_goals

    def best_scorer(self) -> object:
        best_player = None
        best_scores = 0
        for curr_player in self.__players:
            if curr_player.get_goals() >= best_scores:
                best_scores = curr_player.get_goals()
                best_player = curr_player
        return best_player

# p1 = Player("Ivan", "st")
# p2 = Player("Dragan", "rt")
# p1.score_goal()
# p1.score_goal()
# p2.score_goal()
# p2.score_goal()
# p2.score_goal()
# team1 = Team("Veselite mecheta")
# team1.add_player(p1)
# team1.add_player(p2)
# print(team1.name)
# print(team1.total_goals())
# print(team1.best_scorer())