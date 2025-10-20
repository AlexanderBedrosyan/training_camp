from player import Player
from match import Match
from tournament import Tournament

p1 = Player("Alice")
p2 = Player("Bob")

m = Match(p1, p2)
m.play(p1)

t = Tournament()
t.add_player(p1)
t.add_player(p2)

print(t.leaderboard())  # [('Alice', 3), ('Bob', 0)]