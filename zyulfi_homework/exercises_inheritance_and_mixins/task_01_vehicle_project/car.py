# В car.py създай клас Car, който наследява Vehicle
# private атрибут __brand
# метод info() да връща "Brand car with max speed X"

from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, max_speed, brand=str):
        super().__init__(max_speed)
        self.__brand = brand

    def info(self) -> str:
        return f"{self.__brand} car with max speed {self._max_speed}"

