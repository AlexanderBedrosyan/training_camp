# Team: списък от Player обекти, методи add_player(), total_goals()

from player import Player

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, current_player=object) -> None:
        self.players.append(current_player)


    def total_goals(self) -> int:
        goals = 0
        for current_player in self.players:
            goals += current_player._Player__goals

        return goals

