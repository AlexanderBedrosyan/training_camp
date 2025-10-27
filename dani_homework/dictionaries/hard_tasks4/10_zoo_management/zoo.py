# Zoo
# Атрибути: списък клетки
# Методи: total_animals(), largest_cage()a
from cage import Cage


class Zoo:
    def __init__(self):
        self.cages = []

    def add_cage(self, current_cage):
        self.cages.append(current_cage)

    def total_animals(self):
        return sum(cage.count_animals() for cage in self.cages)

    def largest_cage(self) -> Cage:
        if not self.cages:
            return None
        return max(self.cages, key=lambda c: c.capacity)
