# Party: name, списък от кандидати; метод total_votes()
from exercises_hard_tasks2.election_system.candidate import Candidate


class Party:
    def __init__(self, name):
        self.name = name
        self.list_of_candidates: list[Candidate] = []

    def add_candidate(self, curr_candidate=object) -> None:
        self.list_of_candidates.append(curr_candidate)

    def total_votes(self) -> int:
        return sum([curr_candidate.get_votes() for curr_candidate in self.list_of_candidates])

    def best_candidate(self):
        best_candidate = None
        best_vote = 0
        for curr_candidate in self.list_of_candidates:
            if curr_candidate.get_votes() >= best_vote:
                best_vote = curr_candidate.get_votes()
                best_candidate = curr_candidate
        return best_candidate