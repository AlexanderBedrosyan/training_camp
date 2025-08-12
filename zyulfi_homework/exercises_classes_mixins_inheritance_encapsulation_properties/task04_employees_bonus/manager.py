# Manager има екип и метод total_team_salary()
from employee import Employee


class Manager(Employee):
    def __init__(self, name=str, salary=int):
        super().__init__(name, salary)
        self.team_member = []

    def add_employee(self, curr_employee=object):
        self.team_member.append(curr_employee)

    def total_team_salary(self) -> float:
        sum_salary = 0
        for member in self.team_member:
            sum_salary += member._salary
        sum_salary += self._salary
        return sum_salary
