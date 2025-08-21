# vehicle.py:
# Клас Vehicle със:
# protected атрибут _type
# метод start(), който отпечатва "Starting {type}"
# --------------------------------------

from engine import Engine

class Vehicle:
    def __init__(self, current_type=str):
        self._type = current_type

    def start(self) -> None:
        print(f"Starting {self._type}")

class Car(Vehicle, Engine):
    def __init__(self, vehicle_type, power):
        Vehicle.__init__(self, vehicle_type)
        Engine.__init__(self, power)

    def start(self):
        super().start()