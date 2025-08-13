# 🔹 Задача 6
# Създай Mixin DriveMixin с метод drive() връщащ "Driving...".
# Създай клас Truck с атрибут weight, наследяващ DriveMixin, и тествай drive().

from mixins import DriveMixin

class Truck(DriveMixin):

    def __init__(self, weight):
        self.weight = weight

    def drive_tester(self):
        return f"Truck with {self.weight} weight. {self.drive()}"

current_truck = Truck(2000)
print(current_truck.drive_tester())
print(current_truck.drive())