# League: списък от Team обекти,
# метод top_scorer() (връща играча с най-много голове в лигата)

class League:
    def __init__(self):
        self.teams = []

    def add_team(self, current_team=object) -> None:
        self.teams.append(current_team)

    def top_scorer(self):
        best_p = None
        best_score = 0

        for current_team in self.teams:
            for current_pleayer in current_team.players:
                if current_pleayer._Player__goals >= best_score:
                    best_p = current_pleayer
                    best_score = current_pleayer._Player__goals

        return best_p


