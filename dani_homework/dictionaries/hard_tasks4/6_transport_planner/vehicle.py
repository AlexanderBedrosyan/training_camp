# Vehicle Атрибути: name, speed
# Метод: travel_time(route) → проверява скорост > 0

class Vehicle:
    def __init__(self, name:str, speed: float):
        self.name = name
        self.speed = speed

    def travel_time(self, curr_route):
        if self.speed <= 0:
            raise ValueError("Error")
        return round(curr_route.distance / self.speed, 2)


