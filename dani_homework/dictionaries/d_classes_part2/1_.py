# Задача 1: Гилдията на драконоловаците
# Създай клас DragonGuild, който управлява членове и победите им над дракони.
# Всеки член има име, ниво и списък с победи (като речник {дракон: награда}).
# Изисквания:
# add_hunter(name, level) — добавя ловец, ако го няма.
# record_victory(name, dragon, reward) — добавя победа и награда.
# total_rewards(name) — връща общата награда на ловец.
# top_hunter() — връща името на ловеца с най-много общи награди.


class DragonGuild:                              # управлява членове и победите им над дракони
    def __init__(self):
        self.hunters = {}
# {"Ivan": {"level": 5, "victories": {"Smaug": 300, Nidhogg": 150}}}

    def add_hunter(self, name, level):              # добавя ловец, ако го няма
        if name not in self.hunters:
            self.hunters[name] = {"level": level, "victories": {}}

    def record_victory(self, name, dragon, reward): # добавя победа и награда
        if name not in self.hunters:
            print(f"Ловецът '{name}' не съществува в гилдията!")
            return
        self.hunters[name]["victories"][dragon] = reward

    def total_rewards(self, name):                        # връща общата награда на ловец
        if name not in self.hunters:
            print(f"Ловецът '{name}' не съществува!")
            return 0
        return sum(self.hunters[name]["victories"].values())

    def top_hunter(self):                           # връща името на ловеца с най-много общи награди
        if not self.hunters:
            return None
        return max(self.hunters, key=lambda name: self.total_rewards(name))

    def __repr__(self):
        return f"DragonGuild ({len(self.hunters)} ловци)"

# Тест:
g = DragonGuild()
g.add_hunter("Ivan", 10)
g.add_hunter("Maria", 12)
g.record_victory("Ivan", "FireDrake", 500)
g.record_victory("Ivan", "SkySerpent", 300)
g.record_victory("Maria", "ShadowWing", 900)
print(g.top_hunter()) # Maria