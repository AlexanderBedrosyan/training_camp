# Truck добавя атрибут load_capacity и метод can_transport(weight)
from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, max_speed=int, load_capacity=bool):
        super().__init__(max_speed)
        self.load_capacity = load_capacity

    def can_transport(self, weight):
        return weight <= self.load_capacity


