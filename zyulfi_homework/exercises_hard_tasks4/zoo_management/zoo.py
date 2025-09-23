# Zoo
# Атрибути: списък клетки
# Методи: total_animals(), largest_cage()
from exercises_hard_tasks4.zoo_management.cage import Cage


class Zoo:
    def __init__(self):
        self.list_of_cage: list[Cage] = []

    def add_cage(self, curr_cage:object) -> None:
        self.list_of_cage.append(curr_cage)

    def total_animals(self) -> int:
        return sum([curr_cage.count_animals() for curr_cage in self.list_of_cage])

    def largest_cage(self):
        return list(sorted(self.list_of_cage, key=lambda curr_cage: -curr_cage.count_animals()))[0]