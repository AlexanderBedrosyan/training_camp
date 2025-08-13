# Developer добавя level, метод code()
from employee import Employee


class Developer(Employee):
    def __init__(self, name=str, salary=int, level=str):
        super().__init__(name, salary)
        self.level = level

    def code(self) -> str:
        return f"{self.name} is programing"