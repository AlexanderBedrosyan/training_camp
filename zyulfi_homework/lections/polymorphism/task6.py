# Създайте функция start_engine(vehicle), която може да стартира двигател на всяко
# превозно средство (Car, Motorcycle, Boat), без да се интересува от класа.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Dran, dran"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Dran, dran"

class Boat(Vehicle):
    def start_engine(self):
        return "Dran, dran"

c = Car()
m = Motorcycle()
b = Boat()

print(c.start_engine())
print(m.start_engine())
print(b.start_engine())