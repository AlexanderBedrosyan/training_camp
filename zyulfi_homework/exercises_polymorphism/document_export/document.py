# DocumentExporter: базов клас с метод export(content)
from abc import ABC, abstractmethod

class DocumentExporter(ABC):
    @abstractmethod
    def export(self, content):
        pass
