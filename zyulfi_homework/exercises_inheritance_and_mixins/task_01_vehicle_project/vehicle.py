# В vehicle.py създай клас Vehicle с:
# protected атрибут _max_speed
# метод info(), който връща "Vehicle with max speed X"

class Vehicle:
    def __init__(self, max_speed=int):
        self._max_speed = max_speed

    def info(self) -> str:
        return f"Vehicle with max speed {self._max_speed}"

    @property
    def max_speed(self):
        return self._max_speed

    @max_speed.setter
    def max_speed(self, value):
        if value <= 0:
            raise ValueError("Wrong amount")
        self._max_speed = value
