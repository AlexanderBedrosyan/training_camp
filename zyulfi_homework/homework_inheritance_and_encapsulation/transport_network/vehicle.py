# Атрибути: name, private __speed
# Методи:
# travel_time(route) → време за пътуване = distance / speed
# get_speed() → връща скоростта
from route import Route

class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.__speed = speed

    def travel_time(self, curr_route=object) -> float:
        return curr_route.distance / self.__speed

    def get_speed(self) -> int:
        return self.__speed