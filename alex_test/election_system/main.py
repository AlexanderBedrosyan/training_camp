from candidate import Candidate
from party import Party
from election import Election

c1 = Candidate("Alice"); c1.add_votes(100)
c2 = Candidate("Bob"); c2.add_votes(150)

p = Party("Green"); p.add_candidate(c1); p.add_candidate(c2)

e = Election(); e.add_party(p)

print(e.winning_party().name)    # Green
print(e.top_candidate().name)    # Bob