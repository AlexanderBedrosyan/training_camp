# Shape: базов клас с абстрактен метод area()

from abc import ABC, abstractmethod

# Абстрактен базов клас
class Shape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def area(self):
        pass