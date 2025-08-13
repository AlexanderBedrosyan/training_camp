# Player: name, position, private __goals, методи score_goal(), get_goals()

class Player:
    def __init__(self, name=str, position=str):
        self.name = name
        self.position = position
        self.__goals = 0
        self.__receive_goals = 0

    def score_goal(self) -> None:
        self.__goals += 1


    def get_goals(self) -> None:
        self.__receive_goals += 1
