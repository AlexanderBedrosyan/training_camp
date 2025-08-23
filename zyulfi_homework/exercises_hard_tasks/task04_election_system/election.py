# Election: списък от партии, методи:
# winning_party()
# top_candidate()
from exercises_hard_tasks.task04_election_system.candidate import Candidate
from party import Party


class Election:
    def __init__(self):
        self.list_party: list[Party] = []

    def add_party(self, curr_party=object) -> None:
        self.list_party.append(curr_party)

    def winning_party(self) -> object:
        best_party = None
        best_vote = 0
        for curr_party in self.list_party:
            if curr_party.total_votes() >= best_vote:
                best_vote = curr_party.total_votes()
                best_party = curr_party
        return best_party

    def top_candidate(self) -> str:
        best_candidate = None
        best_candidate_vote = 0

        for curr_party in self.list_party:
            for curr_candidate in curr_party.list_candidate:
                if curr_candidate.votes >= best_candidate_vote:
                    best_candidate_vote = curr_candidate.votes
                    best_candidate = curr_candidate
        return best_candidate
