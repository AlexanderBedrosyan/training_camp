#Атрибути: name, position, private __goals
# Методи:
# score_goal() → увеличава __goals с 1
# get_goals() → връща броя на головете
# __str__() → връща "Player {name}, position: {position}, goals: {goals}"

class Player:
    def __init__(self, name=str, position=str):
        self.name = name
        self.position = position
        self.__goals = 0

    def score_goal(self) -> int:
        self.__goals += 1

    def get_goals(self) -> int:
        return self.__goals

    def __str__(self):
        return f"Player {self.name}, position: {self.position}, goals: {self.__goals}"

# p = Player("Zyulfi", "forward" )
# p.score_goal()
# print(p._Player__goals)
# print(p.get_goals())
# print(p.__str__())
# print(str(p))