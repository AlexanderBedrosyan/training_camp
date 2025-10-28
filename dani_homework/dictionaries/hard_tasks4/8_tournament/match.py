# Match Атрибути: p1, p2, winner
# Метод: play() → добавя точки на победителя

class Match:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.winner = None

    def is_winner(self):
        if self.p1.get_score() > self.p2.get_score():
            self.winner = self.p1
        else:
            self.winner = self.p2
        self.play()

    def play(self):
        self.winner.add_points(3)


