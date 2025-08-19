# Party: списък от кандидати, метод total_votes()
from candidate import Candidate


class Party:
    def __init__(self, name_party):
        self.name = name_party
        self.list_candidate: list[Candidate] = []

    def add_candidate(self, curr_candidate=object) -> None:
        self.list_candidate.append(curr_candidate)

    def total_votes(self) -> int:
        total_votes = 0
        for curr_candidate in self.list_candidate:
            total_votes += curr_candidate.votes
        return total_votes