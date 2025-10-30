# Match
# Атрибути: player1, player2
# Метод: play(winner) → добавя точки на победителя
from player import Player


class Match:
    def __init__(self, player1:Player, player2:Player):
        self.player1 = player1
        self.player2 = player2

    def play(self, winner:Player):
        winner.add_score(3)




