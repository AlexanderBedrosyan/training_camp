# Задача 5
# Създай клас Vehicle с атрибут speed и метод move() връщащ "Moving at {speed} km/h".
# Създай клас Plane, наследяващ Vehicle, и добави метод fly() връщащ "Flying".

class Vehicle:
    def __init__(self, speed=int):
        self.speed = speed

    def move(self) -> str:
        return f"Moving at {self.speed} km/h"

class Plane(Vehicle):
    def fly(self):
        return "Flying"

current_vehicle = Vehicle(55)
current_fly = Plane()
print(current_vehicle.move())
print(current_fly.fly())