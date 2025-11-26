# Задача 3: Театрална компания
# Създай клас TheaterCompany, който управлява актьори, техните роли и приходи от представления.
# Изисквания:
# Речник {актьор: {"roles": [роля], "income": сума}}
# add_actor(name, role) — добавя актьор и роля.
# record_income(name, amount) — увеличава приходите.
# most_profitable_actor() — връща актьора с най-високи приходи.
# total_income() — общ доход на компанията.

class TheaterCompany:
    def __init__(self):
        self.theater_company_dict = {}

    def add_actor(self, name, role):
        if name not in self.theater_company_dict:
            self.theater_company_dict[name] = {}
            self.theater_company_dict[name]["roles"] = [role]
            self.theater_company_dict[name]["income"] = 0

    def record_income(self, name, amount):
        if name in self.theater_company_dict:
            self.theater_company_dict[name]["income"] += amount
        else:
            print("Error")

    def most_profitable_actor(self):
        return sorted(self.theater_company_dict.items(), key=lambda x: -x[1]["income"])[0][0]

    def total_income(self):
        return sum([curr_income["income"] for curr_name, curr_income in self.theater_company_dict.items()])





# Тест:
t = TheaterCompany()
t.add_actor("Elena", "Juliet")
t.record_income("Elena", 1000)
t.add_actor("Ivan", "Romeo")
t.record_income("Ivan", 800)
print(t.most_profitable_actor()) # Elena
print(t.total_income()) # 1800