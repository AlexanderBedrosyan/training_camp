from player import Player
from team import Team
from league import League

p1 = Player("Ivan", "Forward")
p1.score_goal()
p2 = Player("Georgi", "Midfielder")
p2.score_goal()

t = Team("Tigers")
t.add_player(p1)
t.add_player(p2)

league = League()
league.add_team(t)

print(league.top_scorer().name)  # Ivan
print(league.total_goals())      # 3