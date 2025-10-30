# Създай клас Company, който управлява отдели и служители.
# Условия: Речник {отдел: {"employees": [имена], "budget": сума}}
# Метод add_employee(dept, name)
# Метод increase_budget(dept, amount)
# Метод total_budget() – връща общия бюджет на фирмата.

class Company:
    def __init__(self):
# структура: {отдел: {"employees": [имена], "budget": сума}}
        self.departments = {}

    def add_employee(self, dept: str, name: str):
# Добавя служител в даден отдел (създава отдела, ако го няма).
        if dept not in self.departments:
            self.departments[dept] = {"employees": [], "budget": 0.0}
        self.departments[dept]["employees"].append(name)

    def increase_budget(self, dept: str, amount: float):
# Увеличава бюджета на отдела (създава отдела, ако го няма).
        if amount < 0:
            raise ValueError("Сумата не може да бъде отрицателна.")
        if dept not in self.departments:
            self.departments[dept] = {"employees": [], "budget": 0.0}
        self.departments[dept]["budget"] += amount

    def total_budget(self) -> float:
# Връща общия бюджет на всички отдели.
        return sum(data["budget"] for data in self.departments.values())

    def __str__(self):
        return f"Company({len(self.departments)} departments)"

# Тест:
c = Company()
c.add_employee("IT", "Ivan")
c.add_employee("HR", "Maria")
c.increase_budget("IT", 5000)
c.increase_budget("HR", 3000)
print(c.total_budget())  # 8000
