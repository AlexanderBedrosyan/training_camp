# Election: списък от партии, методи:
# winning_party()
# top_candidate()

class Election:
    def __init__(self):
        self.list_of_party = []

    def add_party(self, current_party=str)-> None:
        self.list_of_party.append(current_party)

    def winning_party(self)->object:
        winner = None
        win_vote_result = 0
        for current_party in self.list_of_party:
            if current_party.total_votes() >= win_vote_result:
                winner = current_party
                win_vote_result = current_party.total_votes()
        return winner

    def top_candidate(self):
        candidate = None
        winner_vote = 0
        for party in self.list_of_party:
            for current_candidate in party.candidates:
                if current_candidate._Candidate__votes >= winner_vote:
                    candidate = current_candidate
                    winner_vote = current_candidate._Candidate__votes
        return candidate




