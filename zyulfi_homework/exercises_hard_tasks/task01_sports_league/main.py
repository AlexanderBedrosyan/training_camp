from player import Player
from team import Team
from league import League

p1 = Player("Ivan", "Forward")
p1.score_goal()
p1.score_goal()
t = Team("Tigers")
t.add_player(p1)

league = League()
league.add_team(t)
print(league.top_scorer().name)  # Ivan
print(p1.goals)
