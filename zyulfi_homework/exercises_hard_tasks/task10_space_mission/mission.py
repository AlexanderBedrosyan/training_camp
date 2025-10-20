# Mission: списък от астронавти и кораб,
# методи:
# total_hours_in_space()
# is_over_capacity()
from exercises_hard_tasks.task10_space_mission.astronaut import Astronaut
from exercises_hard_tasks.task10_space_mission.spaceship import Spaceship


class Mission:
    def __init__(self, ship=Spaceship):
        self.ship = ship
        self.list_of_astronaut: list[Astronaut] = []


    def add_astronaut(self, curr_astronaut):
        if self.is_over_capacity():
            print("Is full")
        else:
            self.list_of_astronaut.append(curr_astronaut)

    def total_hours_in_space(self):
        return sum([curr_astronaut.get_hours() for curr_astronaut in self.list_of_astronaut])


    def is_over_capacity(self):
        if not self.ship.can_carry(len(self.list_of_astronaut) + 1):
            return False
        return True
