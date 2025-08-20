# Candidate: name, private __votes, метод add_votes(n)

class Candidate:
    def __init__(self, name=str):
        self.name = name
        self.votes = 0

    def add_votes(self, current_votes=int) -> None:
        self.votes += current_votes