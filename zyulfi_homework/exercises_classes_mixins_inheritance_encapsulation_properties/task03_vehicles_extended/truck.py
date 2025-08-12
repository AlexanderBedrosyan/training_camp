# Truck добавя атрибут load_capacity и метод can_transport(weight)

from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, max_speed=int, load_capacity=int):
        super().__init__(max_speed)
        self.load_capacity = load_capacity

    def can_transport(self, weight=int) -> bool:
        if weight <= self.load_capacity:
            return True
        else:
            return False

