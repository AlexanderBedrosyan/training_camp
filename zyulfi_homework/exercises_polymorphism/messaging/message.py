# Message: базов клас с метод send(msg)

from abc import ABC, abstractmethod


class Message(ABC):
    @abstractmethod
    def send(self, msg):
        pass