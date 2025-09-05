# Атрибути: private __teams (списък от Team)
# Методи:
# add_team(team) → добавя отбор
# top_scorer() → връща играча с най-много голове в лигата
# total_goals() → връща сумата на всички голове в лигата
from team import Team


class League:
    def __init__(self)->None:
        self.__teams: list[Team] = []

    def add_team(self, current_team):
        self.__teams.append(current_team)

    def total_goals(self):
        total_league_goals = 0
        for current_team in self.__teams:
            total_league_goals += current_team.total_goals()
        return total_league_goals

    def top_scorer(self):
        best_player = None

        for current_team in self.__teams:
            best_team_pl = current_team.best_scorer()
            if best_team_pl is None:
                continue

            else:
                if best_team_pl.get_goals() > best_player.get_goals():
                    best_player = best_team_pl
        return best_player