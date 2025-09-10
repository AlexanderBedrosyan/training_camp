# Vehicle: private __speed, метод travel_time(route)
from route import Route

from route import Route

class Vehicle:
    def __init__(self, name: str, speed: float):
        if speed <= 0:
            raise ValueError("Скоростта трябва да е положително число.")
        self.name = name
        self.__speed = float(speed)   # private

    def get_speed(self) -> float:   #скоростта на превозното средство

        return self.__speed

    def travel_time(self, route: Route) -> float:   #Времето = разстояние / скорост (в часове)

        return route.distance / self.__speed

    def __str__(self) -> str:
        return f"{self.name} ({self.__speed:g} km/h)"

