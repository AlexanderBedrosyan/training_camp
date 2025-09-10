# Vehicle
# Атрибути: name, private __speed
# Метод: travel_time(route) → разстояние / скорост (t = s : v)
class Vehicle:
    def __init__(self, name:str, speed:int or float):
        self.name = name
        self.__speed = speed

    def travel_time(self, curr_distance: float or int):
        return curr_distance / self.__speed

    def __str__(self) -> str:
        return f"{self.name} ({self.__speed} km/h)"

#test
v1=Vehicle("carA", 150)
V2=Vehicle("carB", 200)

print(v1.travel_time(110))
