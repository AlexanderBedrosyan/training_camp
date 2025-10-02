# Candidate: name, private __votes; методи add_votes(), get_votes()

class Candidate:
    def __init__(self, name):
        self.name = name
        self.__votes = 0

    def add_votes(self, curr_votes=int) -> None:
        if curr_votes > 0:
            self.__votes += curr_votes
        else:
            print("Error")

    def get_votes(self) -> int:
        return self.__votes


