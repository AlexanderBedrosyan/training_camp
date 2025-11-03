# Задача 4: Лабораторията на алхимиците
# Създай клас AlchemyLab, който съхранява рецепти и резултатите от експерименти.
# Изисквания: Речник {име: {"ingredients": [...], "success_rate": %}}
# add_recipe(name, ingredients, rate)
# update_rate(name, new_rate)
# best_recipe() — връща рецептата с най-висок успех.
# average_success() — среден процент успех на всички рецепти.
class AlchemyLab:
    def __init__(self):
        self.dict_recipe = {}

    def add_recipe(self, name, ingredients, rate):
        if name not in self.dict_recipe:
            self.dict_recipe[name] = {"ingredients": ingredients, "success_rate": rate}
        else:
            print(f"The recipe '{name}' is already exist!")

    def update_rate(self, name, new_rate):
        if name not in self.dict_recipe:
            print(f"The recipe '{name}' is not exist!")
            return
        self.dict_recipe[name]["success_rate"] = new_rate

    def best_recipe(self):
        if not self.dict_recipe:
            return None
        return max(self.dict_recipe, key=lambda n: self.dict_recipe[n]["success_rate"])

    def average_success(self):
        if not self.dict_recipe:
            return 0
        total = sum(r["success_rate"] for r in self.dict_recipe.values())
        return total / len(self.dict_recipe)



# Тест:
a = AlchemyLab()
a.add_recipe("Elixir of Life", ["gold", "dew", "root"], 90)
a.add_recipe("Potion of Power", ["iron", "blood"], 80)
a.update_rate("Potion of Power", 85)
print(a.best_recipe()) # Elixir of Life
#
