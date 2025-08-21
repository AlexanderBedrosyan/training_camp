# Създай клас с:
# обикновен атрибут name
# private атрибут __salary
# метод increase_salary(amount)
# @property за salary (само за четене)
# Примерен вход:
# e = Employee("Anna", 3000)
# e.increase_salary(500)
# print(e.salary)  # 3500
#-------------------------------------------

class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.__salary = salary              # частен атрибут

    def increase_salary(self, amount: float) -> None:
        self.__salary += amount             # метод за увеличаване на заплата

    @property
    def salary(self) -> float:
        return self.__salary                # само за четене
# Употреба
e = Employee("Anna", 3000)
e.increase_salary(500)
print(e.salary)                             # -> 3500.0
