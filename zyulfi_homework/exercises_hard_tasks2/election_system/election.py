# Election: списък от партии; методи winning_party(), top_candidate()
from exercises_hard_tasks2.election_system.party import Party


class Election:
    def __init__(self):
        self.list_of_party: list[Party] = []

    def add_party(self, curr_party) -> None:
        self.list_of_party.append(curr_party)

    def winning_party(self) -> object:
        winning_party = None
        best_result = 0

        for curr_party in self.list_of_party:
            if curr_party.total_votes() >= best_result:
                best_result = curr_party.total_votes()
                winning_party = curr_party
        return winning_party

    def top_candidate(self) -> object:
        best_candidate = None
        best_result = 0

        for curr_party in self.list_of_party:
            if curr_party.best_candidate().get_votes() >= best_result:
                best_result = curr_party.best_candidate().get_votes()
                best_candidate = curr_party.best_candidate()
        return best_candidate