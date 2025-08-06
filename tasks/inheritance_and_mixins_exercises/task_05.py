# 🔹 Задача 5
# Създай клас Vehicle с атрибут speed и метод move() връщащ "Moving at {speed} km/h".
# Създай клас Plane, наследяващ Vehicle, и добави метод fly() връщащ "Flying".

class Vehicle:

    def __init__(self, speed):
        self.speed = speed

    def move(self):
        return f"Moving at {self.speed} km/h"

class Plane(Vehicle):

    def fly(self):
        return f"Flying"

current_plane = Plane(250)
print(current_plane.move())
print(current_plane.fly())