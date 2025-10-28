# Manager: базова заплата + бонус за екипManager
from employee import Employee


class Manager(Employee):
    def __init__(self, base_salary, bonus_team):
        self.base_salary = base_salary
        self.bonus_team = bonus_team

    def calculate_salary(self):
        return self.base_salary + self.bonus_team