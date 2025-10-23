# Discount: базов клас с метод apply(price)

from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def apply(self, price):
        pass