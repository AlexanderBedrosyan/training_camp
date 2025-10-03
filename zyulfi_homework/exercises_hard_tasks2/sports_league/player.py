# Атрибути: name, position, private __goals
# Методи: score_goal(), get_goals(), __str__()

class Player:
    def __init__(self, name=str, position=str):
        self.name = name
        self.position = position
        self.__goals = 0

    def score_goal(self):
        self.__goals += 1

    def get_goals(self):
        return self.__goals

    def __str__(self):
        return f"The player {self.name} in position {self.position} has {self.get_goals()} a goal"

