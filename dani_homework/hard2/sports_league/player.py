# Player
# Атрибути: name, position, private __goals
# Методи: score_goal(), get_goals(), __str__()

class Player:
    def __init__(self, name:str, position:str, goals=0):
        self.name = name
        self.position = position
        self.__goals = goals        # отбелязани голове

    def score_goals(self):
        self.__goals += 1

    def get_goals(self):
        return self.__goals

    def __str__(self):
        return f'{self.name} {self.position} - {self.__goals} goals'
#
# plyer1 = Player("Momo", "center", 2 )
# print(plyer1)
#
# plyer1.score_goals()
# plyer1.score_goals()
# plyer1.score_goals()
#
# print(plyer1.__getstate__())
# print(plyer1)
