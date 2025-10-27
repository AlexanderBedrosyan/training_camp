# Developer: базова заплата + бонус за проект
#
from  employee import Employee


class Developer(Employee):
    def __init__(self, base_salary, bonus_salary):
        self.base_salary = base_salary
        self.bonus_salary = bonus_salary

    def calculate_salary(self):
        return self.base_salary + self.bonus_salary