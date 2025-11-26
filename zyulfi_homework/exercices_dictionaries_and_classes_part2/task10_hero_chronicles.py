# Задача 10: Хроники на героите
# Създай клас HeroChronicles, който следи герои, техните битки и точки слава.
# Изисквания:
# Речник {герой: {"battles": [битки], "glory": общо_точки}}
# add_hero(name)
# record_battle(name, battle, points)
# hero_rankings() — сортира героите по слава.
# top_hero() — връща героя с най-много точки.

class HeroChronicles:
    def __init__(self):
        self.dict_heros = {}

    def add_hero(self, name):
        if name not in self.dict_heros:
            self.dict_heros[name] = {
                "battles": [],
                "glory": 0
            }

    def record_battle(self, name, battle, points):
        if name in self.dict_heros:
            self.dict_heros[name]["battles"].append(battle)
            self.dict_heros[name]["glory"] += points
        else:
            self.add_hero(name)
            self.record_battle(name, battle, points)

    def hero_rankings(self):
        return dict(sorted(self.dict_heros.items(), key=lambda x: x[1]["glory"]))

    def top_hero(self):
        # hero = []
        # for key, value in self.hero_rankings().items():
        #     hero.append(key)
        # return hero[-1]
        return [(list(self.hero_rankings())[-1], self.hero_rankings()[list(self.hero_rankings())[-1]]["glory"])]


# Тест:
h = HeroChronicles()
h.add_hero("Draven")
h.record_battle("Draven", "Battle of Storms", 100)
h.record_battle("Draven", "Valley Siege", 150)
h.record_battle("Dragan", "Str", 200)
print(h.top_hero()) # Draven
print(h.hero_rankings()) # [('Draven', 250)]