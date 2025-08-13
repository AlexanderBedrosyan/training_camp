# Shape: базов клас с абстрактен метод area()
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


