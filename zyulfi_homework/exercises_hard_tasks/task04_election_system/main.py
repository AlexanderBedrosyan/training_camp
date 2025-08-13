from candidate import Candidate
from party import Party
from election import Election

c1 = Candidate("Alice")
c2 = Candidate("Bob")
c3 = Candidate("Charlie")

c1.add_votes(1200)
c2.add_votes(1500)
c3.add_votes(900)

party1 = Party("Party A")
party1.add_candidate(c1)
party1.add_candidate(c2)

party2 = Party("Party B")
party2.add_candidate(c3)

election = Election()
election.add_party(party1)
election.add_party(party2)

print("Winning party:", election.winning_party().name)
print("Top candidate:", election.top_candidate().name)
