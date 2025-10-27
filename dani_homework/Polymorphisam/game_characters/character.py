# Character: базов клас с метод attack()
from abc import ABC, abstractmethod


class Character(ABC):
    @abstractmethod
    def attack(self):
        pass