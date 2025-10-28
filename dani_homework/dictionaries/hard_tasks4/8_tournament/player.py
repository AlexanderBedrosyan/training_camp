# Player
# Атрибути: name, private __score
# Методи: add_points(n), get_score()
class Player:
    def __init__(self, name:str):
        self.name = name
        self.__score = 0

    def add_points(self, curr_ponts):
        self.__score += curr_ponts

    def get_score(self):
        return self.__score
