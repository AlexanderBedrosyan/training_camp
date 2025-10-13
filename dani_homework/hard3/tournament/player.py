# Player # Атрибути: name, private __score
# Методи: add_score(points) # get_score()

class Player:
    def __init__(self, name:str):
        self.name = name
        self.__score = 0

    def add_score(self, points:int):
        self.__score += points

    def get_score(self):
        return self.__score

