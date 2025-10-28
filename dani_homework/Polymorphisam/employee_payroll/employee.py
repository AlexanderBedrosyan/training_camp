# Employee: базов клас с метод calculate_salary()
from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass