# Mission: списък от астронавти и кораб, методи:
# total_hours_in_space()
# is_over_capacity(

from astronaut import Astronaut
from spaceship import Spaceship

class Mission:
    def __init__(self, spaceship: Spaceship):
        self.spaceship = spaceship
        self.astronauts = []

    def add_astronaut(self, astronaut: Astronaut):
       # Добавя астронавт в мисията.
        self.astronauts.append(astronaut)
        if self.is_over_capacity():
            print(f"⚠️ Warning: Mission is over capacity! ({len(self.astronauts)}/{self.spaceship.capacity})")

    def total_hours_in_space(self) -> int:
        # Връща общия брой часове в космоса на всички астронавти.
        return sum(a.get_hours_in_space() for a in self.astronauts)

    def is_over_capacity(self) -> bool:
        # Проверява дали броят на астронавтите надвишава капацитета.
        return len(self.astronauts) > self.spaceship.capacity

    def __str__(self):
        return f"Mission({self.spaceship.name}, astronauts={[a.name for a in self.astronauts]})"
