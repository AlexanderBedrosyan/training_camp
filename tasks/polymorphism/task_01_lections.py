# Задача 1
# Създайте клас Vehicle с метод move(). Създайте класове Car и Plane, които наследяват Vehicle и реализират собствени
# версии на move().

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):

    def move(self):
        return "Driving..."

class Plane(Vehicle):

    def move(self):
        return "Flying..."


c = Car()
p = Plane()

print(c.move())
print(p.move())