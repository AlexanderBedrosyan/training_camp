# Задача 6
# Създай Mixin DriveMixin с метод drive() връщащ "Driving...".
# Създай клас Truck с атрибут weight, наследяващ DriveMixin, и тествай drive().

from mixins.task_06_DriveMixin import DriveMixin

class Truck(DriveMixin):
    def __init__(self, wеight=int): # the weight in tons
        self.wеight = wеight
        if self.wеight > 20:
            print("Тhe truck is overloaded")
        else:
            print(DriveMixin.drive(self))

current_truck = Truck(10)
current_truck2 = Truck(30)





