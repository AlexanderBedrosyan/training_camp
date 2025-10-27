# Vehicle: private __speed, метод travel_time(route)
# from route import Route
class Vehicle:
    def __init__(self, speed=float):
        self.__speed = speed

    def travel_time(self, route=object) -> float:
        return route.distance / self.__speed

    @property
    def speed(self):
        return self.__speed



# r = Route("A", "B", 1000)
# v = Vehicle(100)
# print(v.travel_time(r))