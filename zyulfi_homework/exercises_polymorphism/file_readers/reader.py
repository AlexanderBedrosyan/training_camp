# Reader: базов клас с метод read(file)

from abc import ABC, abstractmethod


class Reader(ABC):
    @abstractmethod
    def read(self, file):
        pass