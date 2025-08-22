# Employee с name, _salary, методи get_salary()

class Employee:
    def __init__(self, name=str, salary=int):
        self.name = name
        self._salary = salary

    def get_salary(self):
        self._salary += 100