# Intern: фиксирана малка заплата
from employee import Employee


class Intern(Employee):
    def __init__(self, fix_salary):
        self.fix_salary = fix_salary

    def calculate_salary(self):
        return self.fix_salary