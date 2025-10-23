# Payment: базов клас с метод process(amount)
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process(self, amount):
        pass

