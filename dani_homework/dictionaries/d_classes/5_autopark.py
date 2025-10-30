# Задача 5: Автопарк
# Създай клас Garage, който следи коли и ремонти.
# Условия:
# Речник {рег.номер: {"model": име, "repairs": [разходи]}}
# Метод add_repair(reg, cost) – добавя ремонт.
# Метод total_spent(reg) – сума на всички ремонти за колата.
# Метод most_expensive_car() – връща регистрацията на колата с най-много похарчено.
class Garage:
    def __init__(self):
        self.reg_num_dict = {}

    def add_repair(self, reg, cost):
        model = reg[:2]
        reg_num = {"model": model, "repairs": [cost]}

        if reg not in self.reg_num_dict:
            self.reg_num_dict[reg] = {}
            self.reg_num_dict[reg]["model"] = model
            self.reg_num_dict[reg]["repairs"] = []

        self.reg_num_dict[reg]['repairs'].append(cost)

    def total_spent(self, reg):
        return sum(self.reg_num_dict[reg]['repairs'])

    def most_expensive_car(self):
        return sorted(self.reg_num_dict.items(), key=lambda x: sum(x[1]["repairs"]), reverse=True)[0][0]

# Тест:
g = Garage()
g.add_repair("CA1234", 400)
g.add_repair("CB5678", 800)
g.add_repair("CA1234", 300)
g.total_spent("CA1234")
print(g.most_expensive_car())  # CA1234
