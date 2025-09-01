from party import Party
from typing import List

class Election:

    def __init__(self):
        self.list_of_parties: List[Party] = []

    def add_party(self, current_party=object):
        self.list_of_parties.append(current_party)

    def winning_party(self):
        return list(sorted(self.list_of_parties, key=lambda current_party: current_party.total_votes()))[0]

    def top_candidate(self):
        # top_candidate = None
        # top_candidate_vote = 0
        # for current_party in self.list_of_parties:
        #     if current_party.top_candidate_in_party().get_votes() >= top_candidate_vote:
        #         top_candidate_vote = current_party.top_candidate_in_party().get_votes()
        #         top_candidate = current_party.top_candidate_in_party()
        # return top_candidate
        return list(sorted([current_candidate for current_party in self.list_of_parties for current_candidate in current_party.list_of_candidates], key=lambda curr_candidate: -curr_candidate.get_votes()))[0]