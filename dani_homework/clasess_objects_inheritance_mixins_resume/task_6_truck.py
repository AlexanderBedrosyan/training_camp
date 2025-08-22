# Създай Mixin DriveMixin с метод drive() връщащ "Driving...".
# Създай клас Truck с атрибут weight, наследяващ DriveMixin, и тествай drive().
# --------------------------------------------------------------------------------

class DriveMixin:
    def drive(self)-> str:
        return "Driving..."

class Truck(DriveMixin):
    def __init__(self, weight: int)-> None:
        self.weight:int = weight


t = Truck(2000)
print(t.drive())
print(t.weight)