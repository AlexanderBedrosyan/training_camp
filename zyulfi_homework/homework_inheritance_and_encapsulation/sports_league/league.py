# Атрибути: private __teams (списък от Team)
# Методи:
# add_team(team) → добавя отбор
# top_scorer() → връща играча с най-много голове в лигата
# total_goals() → връща сумата на всички голове в лигата
from team import Team

class League:
    def __init__(self):
        self.__teams: list[Team] = []

    def add_team(self, curr_team=object) -> None:
        self.__teams.append(curr_team)

    def top_scorer(self) -> object:
        best_player = None
        best_scores = 0
        for curr_team in self.__teams:
            if curr_team.best_scorer().get_goals() >= best_scores:
                best_scores = curr_team.best_scorer().get_goals()
                best_player =  curr_team.best_scorer()
        return best_player

    def total_goals(self) -> int:
        # return sum([curr_team.total_goals() for curr_team in self.__teams])
        all_goals = 0
        for curr_team in self.__teams:
            all_goals += curr_team.total_goals()
        return all_goals






