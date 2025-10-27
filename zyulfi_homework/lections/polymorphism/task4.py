# Направете клас Employee с метод calculate_salary().
# Наследете го в Manager и Developer, като всеки има различна формула за изчисление на заплатата.

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        return 5000
    
class Developer(Employee):
    def calculate_salary(self):
        return 3000

m = Manager()
d = Developer()
print(m.calculate_salary())
print(d.calculate_salary())