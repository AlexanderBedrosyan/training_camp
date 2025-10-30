# Vehicle: базов клас с метод travel_time(distance)
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def travel_time(self, distance):
        pass