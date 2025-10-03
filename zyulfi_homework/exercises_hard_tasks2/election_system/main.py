from candidate import Candidate
from party import Party
from election import Election

c1 = Candidate("Alice");
c1.add_votes(100)

c2 = Candidate("Bob")
c2.add_votes(150)

c3 = Candidate("Gugov")
c3.add_votes(250)

c4 = Candidate("Dragancho")
print(c4.add_votes(-25))

p = Party("Green")
p.add_candidate(c1)
p.add_candidate(c2)

p2 = Party("Free")
p2.add_candidate(c1)
p2.add_candidate(c2)
p2.add_candidate(c3)

e = Election()
e.add_party(p)
e.add_party(p2)

print(e.winning_party().name)    # Green
print(e.top_candidate().name)    # Bob