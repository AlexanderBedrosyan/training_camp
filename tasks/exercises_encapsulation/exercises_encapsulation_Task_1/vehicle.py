from engine import Engine

class Vehicle:
    def __init__(self, vehicle_type):
        self._type = vehicle_type

    def start(self):
        print(f"Starting {self._type}")


class Car(Vehicle, Engine):

    def __init__(self, vehicle_type, power):
        Vehicle.__init__(self, vehicle_type)
        Engine.__init__(self, power)

    def start(self):
        super().start()





