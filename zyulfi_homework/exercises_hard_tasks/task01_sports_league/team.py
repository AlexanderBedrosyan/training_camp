# Team: списък от Player обекти, методи add_player(), total_goals()
from player import Player

class Team:
    def __init__(self, team_name=object):
        self.team_name = team_name
        self.list_player: list[Player] = []

    def add_player(self, curr_player=object) -> None:
        self.list_player.append(curr_player)

    def total_goals(self) -> int:
        all_goals = 0
        for curr_player in self.list_player:
            all_goals += curr_player.goals
        return all_goals


