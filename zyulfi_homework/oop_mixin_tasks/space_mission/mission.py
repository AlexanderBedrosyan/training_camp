# Mission (MissionMixin)
# Атрибути: private __astronauts, private __ship
# Методи: add_astronaut(), total_hours(), check_capacity()
from oop_mixin_tasks.space_mission.astronaut import Astronaut
from oop_mixin_tasks.space_mission.mission_mixin import MissionMixin
from oop_mixin_tasks.space_mission.spaceship import Spaceship


class Mission(MissionMixin):
    def __init__(self, ship=Spaceship):
        self.__astronauts: list[Astronaut] = []
        self.__ship = ship

    def add_astronaut(self, curr_astronaut=Astronaut) -> None:
        self.__astronauts.append(curr_astronaut)

    def total_hours(self):
        return sum([curr_astronaut.get_hours() for curr_astronaut in self.__astronauts])

    def get_ship(self):
        return self.__ship

    def check_capacity(self):
        return MissionMixin().is_over_capacity(self.get_ship, len(self.__astronauts))