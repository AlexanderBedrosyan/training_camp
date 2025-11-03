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
        self.dict_actors = {}

    def add_actor(self, name, role):
        if name not in self.dict_actors:
            self.dict_actors[name] = {"roles": [role], "income": 0}
        else:
            if role not in self.dict_actors[name]["roles"]:
                self.dict_actors[name]["roles"].append(role)

    def record_income(self, name, amount):
        if name not in self.dict_actors:
            print(f"The actor '{name}' is not exist.")
            return
        self.dict_actors[name]["income"] += amount


    def most_profitable_actor(self):
        if not self.dict_actors:
            return None
        return max(self.dict_actors, key=lambda n: self.dict_actors[n]["income"])

    def total_income(self):
        return sum(actor["income"] for actor in self.dict_actors.values())


# Тест:
t = TheaterCompany()
t.add_actor("Elena", "Juliet")
t.record_income("Elena", 1000)
t.add_actor("Ivan", "Romeo")
t.record_income("Ivan", 800)
print(t.most_profitable_actor()) # Elena
print(t.total_income()) # 1800