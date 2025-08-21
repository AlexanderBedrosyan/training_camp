# Car има private атрибут __brand и метод info()
from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand=str, max_speed=int):
        super().__init__(max_speed)
        self.__brand = brand

    def info(self):
        return f"{self.__brand} car with max speed {self._max_speed}"