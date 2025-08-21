# Candidate: name, private __votes, метод add_votes(n)

class Candidate:
    def __init__(self, name=str):
        self.name = name
        self.__votes = 0

    def add_votes(self, vote=int) -> None:
        self.__votes += vote

