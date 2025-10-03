# League
# Атрибути: private __teams
# Методи: add_team(), top_scorer(), total_goals()
from exercises_hard_tasks2.sports_league.player import Player
from team import Team

class League:
    def __init__(self):
        self.__teams: list[Team] = []

    def add_team(self, curr_team=object) -> None:
        self.__teams.append(curr_team)

    def total_goals(self) -> int:
        return sum([curr_team.total_goals() for curr_team in self.__teams])

    def top_scorer(self):
        best_player = None
        most_goals = 0

        for curr_team in self.__teams:
            if curr_team.best_scorer().get_goals() >= most_goals:
                most_goals = curr_team.best_scorer().get_goals()
                best_player = curr_team.best_scorer()
        return best_player