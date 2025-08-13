from astronaut import Astronaut
from spaceship import Spaceship
from mission import Mission

a1 = Astronaut("Neil", 1000)
a2 = Astronaut("Buzz", 800)
a3 = Astronaut("Sally", 500)

ship = Spaceship("Apollo", 2)

mission = Mission(ship)
mission.add_astronaut(a1)
mission.add_astronaut(a2)
mission.add_astronaut(a3)  # should trigger over capacity check

print("Total hours in space:", mission.total_hours_in_space())
print("Over capacity?", mission.is_over_capacity())
