# League: списък от Team обекти, метод top_scorer() (връща играча с най-много голове в лигата)
from team import Team

class League:
    def __init__(self):
        self.list_teams: list[Team] = []

    def add_team(self, current_team=object) -> None:
        self.list_teams.append(current_team)

    def top_scorer(self) -> object:
        best_player = None
        best_score = 0
        for curr_team in self.list_teams:
            for curr_player in curr_team.list_player:
                if curr_player.goals >= best_score:
                    best_score = curr_player.goals
                    best_player = curr_player
        return best_player



