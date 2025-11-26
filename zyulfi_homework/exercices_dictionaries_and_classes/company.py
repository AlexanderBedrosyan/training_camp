# Задача 8: Фирмена йерархия
# Създай клас Company, който управлява отдели и служители.
# Условия:
# Речник {отдел: {"employees": [имена], "budget": сума}}
# Метод add_employee(dept, name)
# Метод increase_budget(dept, amount)
# Метод total_budget() – връща общия бюджет на фирмата.

class Company:
    def __init__(self):
        self.company_dict = {}

    def add_employee(self, dept, name):
        if dept not in self.company_dict:
            self.company_dict[dept] = {
                "employees": [name],
                "budget": 0
            }

    def increase_budget(self, dept, amount):
        if dept in self.company_dict and amount > 0:
            self.company_dict[dept]["budget"] += amount
        elif dept in self.company_dict and amount <= 0:
            print(f"The amount cannot be negative.")
        elif dept not in self.company_dict and amount > 0:
            print(f"{dept} does not exist.")
        else:
            print(f"Does not exist {dept} and The amount cannot be negative.")

    def total_budget(self):
        return sum(list(budget["budget"] for dept, budget in self.company_dict.items()))

# Тест:
c = Company()
c.add_employee("IT", "Ivan")
c.add_employee("HR", "Maria")
c.increase_budget("IT", 5000)
c.increase_budget("HR", 3000)
print(c.company_dict)
print(c.total_budget())  # 8000