class Candidate:

    def __init__(self, name):
        self.name = name
        self.__votes = 0

    def add_votes(self, current_votes):
        if current_votes < 0:
            return
        self.__votes += current_votes

    def get_votes(self):
        return self.__votes

