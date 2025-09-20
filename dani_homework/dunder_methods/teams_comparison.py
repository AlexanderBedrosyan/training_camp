class Team:
    def __init__(self, name, wins):
        self.name = name
        self.wins = wins

    def __ge__(self, other):
        if isinstance(other, Team):
            return self.wins >= other.wins
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Team):
            return self.wins == other.wins
        return NotImplemented


# Примерно използване:
t1 = Team("Tigers", 10)
t2 = Team("Lions", 8)

print(t1 >= t2)  # True
print(t1 == t2)  # False
