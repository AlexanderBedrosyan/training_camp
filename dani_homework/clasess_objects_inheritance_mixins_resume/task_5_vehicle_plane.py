# Създай клас Vehicle с атрибут speed и метод move() връщащ "Moving at {speed} km/h".
# Създай клас Plane, наследяващ Vehicle, и добави метод fly() връщащ "Flying".
# -------------------------------------------------------------------------------

class Vehicle:
    def __init__(self, speed: int)-> None:
        self.speed: int = speed

    def move(self)-> str:
        return (f"Moving at {self.speed} km/h")

class Plane(Vehicle):
    def __init__(self, speed: int)-> None:
        super().__init__(speed)

    def fly(self)-> str:
        return "Flying"

p = Plane(50)
print(p.move())
print(p.fly())