# League
# Атрибути: private __teams
# Методи: add_team(), top_scorer(), total_goals()
from team import Team


class League:
    def __init__(self):
        self.__teams: list[Team] = []

    def add_team(self, current_team):
        self.__teams.append(current_team)

    def top_scorer(self):
        top_scorer = 0
        for current_team in self.__teams:
            top_scorer = current_team.best_scorer()

        return top_scorer

    def total_goals(self):
        total_goals = 0
        for current_team in self.__teams:
            total_goals = current_team.best_scorer()

        return total_goals
