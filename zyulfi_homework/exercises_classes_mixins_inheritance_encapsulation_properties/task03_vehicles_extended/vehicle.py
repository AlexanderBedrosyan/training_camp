# Vehicle: базов клас с protected _max_speed и метод describe()

class Vehicle:
    def __init__(self, max_speed=int):
        self._max_speed = max_speed

    def describe(self) -> str:
        return f"The vehicle max speed is {self._max_speed}"