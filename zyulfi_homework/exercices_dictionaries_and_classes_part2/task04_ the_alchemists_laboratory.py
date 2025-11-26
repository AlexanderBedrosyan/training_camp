# Задача 4: Лабораторията на алхимиците
# Създай клас AlchemyLab, който съхранява рецепти и резултатите от експерименти.
# Изисквания:
# Речник {име: {"ingredients": [...], "success_rate": %}}
# add_recipe(name, ingredients, rate)
# update_rate(name, new_rate)
# best_recipe() — връща рецептата с най-висок успех.
# average_success() — среден процент успех на всички рецепти.


class AlchemyLab:
    def __init__(self):
        self.alchemy_lab_dict = {}

    def add_recipe(self, name, ingredients, rate):
        if name not in self.alchemy_lab_dict:
            self.alchemy_lab_dict[name] = {"ingredients": [], "success_rate": 0}
        self.alchemy_lab_dict[name]["ingredients"].append(ingredients)
        self.alchemy_lab_dict[name]["success_rate"] = rate

    def update_rate(self, name, new_rate):
        if name in self.alchemy_lab_dict:
            self.alchemy_lab_dict[name]["success_rate"] = new_rate

    def best_recipe(self):
        return sorted(self.alchemy_lab_dict.items(), key=lambda x: -x[1]["success_rate"])[0][0]

    def average_success(self):
        return sum([curr_rate["success_rate"] for curr_name, curr_rate in self.alchemy_lab_dict.items()]) / len(self.alchemy_lab_dict)



# Тест:
a = AlchemyLab()
a.add_recipe("Elixir of Life", ["gold", "dew", "root"], 90)
a.add_recipe("Potion of Power", ["iron", "blood"], 80)
a.update_rate("Potion of Power", 85)
print(a.best_recipe()) # Elixir of Life
print(a.average_success())