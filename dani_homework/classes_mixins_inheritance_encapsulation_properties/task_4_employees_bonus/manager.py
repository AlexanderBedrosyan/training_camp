# Manager има екип и метод total_team_salary()

from employee import Employee

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.team_list = []

    def add_employee(self, team_member=object):
        self.team_list.append(team_member)

    def total_team_salary(self):
        current_salary = 0
        for member in self.team_list:
            current_salary += member._salary

        current_salary += self._salary
        return current_salary

