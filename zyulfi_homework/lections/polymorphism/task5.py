# Задача 5
# Направете клас Printer, който има метод print_document().
# Създайте два различни типа принтери (LaserPrinter и InkjetPrinter),
# които отпечатват по различен начин.

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

class LaserPrinter(Printer):
    def print_document(self):
        return "The laser"

class InkjetPrinter(Printer):
    def print_document(self):
        return "The Inkjet"

l = LaserPrinter()
i = InkjetPrinter()
print(l.print_document())
print(i.print_document())