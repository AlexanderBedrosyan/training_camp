# Party: списък от кандидати, метод total_votes()

class Party:
    def __init__(self, party_name):
        self.name = party_name
        self.candidates = []

    def add_candidate(self, candidate=object) -> None:
        self.candidates.append(candidate)

    def total_votes(self) -> int:
        total_votes = 0
        for candidate in self.candidates:
            total_votes += candidate._Candidate__votes
        return total_votes

