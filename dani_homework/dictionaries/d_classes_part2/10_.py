# Задача 10: Хроники на героите
# Създай клас HeroChronicles, който следи герои, техните битки и точки слава.
# Изисквания: Речник {герой: {"battles": [битки], "glory": общо_точки}}
# add_hero(name)
# record_battle(name, battle, points)
# hero_rankings() — сортира героите по слава.
# top_hero() — връща героя с най-много точки.
class HeroChronicles:
    def __init__(self):
        self.dict_heros = {}
# {герой: {"battles": [битки], "glory": общо_точки}}

    def add_hero(self, name):
        if name not in self.dict_heros:
            self.dict_heros[name] = {"battles": [], "glory": 0}

    def record_battle(self, name, battle, points):
        if name not in self.dict_heros:
            print(f"The H '{name}' does not exist!")
            return
        hero = self.dict_heros[name]

        if battle not in hero["battles"]:
            hero["battles"].append(battle)
            # Добавяме точки
        hero["glory"] += points

    def hero_rankings(self):
        rankings = [(name, data["glory"]) for name, data in self.dict_heros.items()]
        rankings.sort(key=lambda x: x[1], reverse=True)
        return rankings

    def top_hero(self):
        if not self.dict_heros:
            return None
        return max(self.dict_heros, key=lambda n: self.dict_heros[n]["glory"])

# Тест:
h = HeroChronicles()
h.add_hero("Draven")
h.record_battle("Draven", "Battle of Storms", 100)
h.record_battle("Draven", "Valley Siege", 150)
print(h.top_hero()) # Draven
print(h.hero_rankings()) # [('Draven', 250)]