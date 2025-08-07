# Създай MoveMixin с метод move() връщащ "Moving...".
# Направи клас Vehicle с атрибут brand и
# клас Bike, който наследява от Vehicle и MoveMixin.
# Създай Bike и извикай move.

class MoveMixin:
    def move(self):
        return ("Moving...")

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Bike(Vehicle, MoveMixin):
    def __init__(self, brand):
        Vehicle.__init__(self, brand)

bike = Bike("BMV")
print(f"{bike.brand} {bike.move()}")
