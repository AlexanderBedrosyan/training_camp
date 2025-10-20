# MissionMixin
# Метод: is_over_capacity(ship, astronauts)
from oop_mixin_tasks.space_mission.astronaut import Astronaut
from oop_mixin_tasks.space_mission.spaceship import Spaceship


class MissionMixin:
    def is_over_capacity(self, ship=Spaceship, astronauts=int) -> bool:
        if ship().capacity <= astronauts:
            return True
        else:
            return False

