from typing import List
from candidate import Candidate

class Party:

    def __init__(self, name):
        self.name = name
        self.list_of_candidates: List[Candidate] = []

    def add_candidate(self, curr_candidate:object):
        self.list_of_candidates.append(curr_candidate)

    def total_votes(self):
        # total_votes = 0
        # for current_candidate in self.list_of_candidates:
        #     total_votes += current_candidate.get_votes()
        # return total_votes
        return sum([current_candidate.get_votes() for current_candidate in self.list_of_candidates])

    def top_candidate_in_party(self):
        # current_best_candidate = None
        # current_best_votes = 0
        # for current_candidate in self.list_of_candidates:
        #     if current_candidate.get_votes() >= current_best_votes:
        #         current_best_votes = current_candidate.get_votes()
        #         current_best_candidate = current_candidate
        # return current_best_candidate
        return list(sorted(self.list_of_candidates, key=lambda current_candidate: -current_candidate.get_votes()))[0]
