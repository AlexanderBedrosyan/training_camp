# Задача 1: Гилдията на драконоловците
# Създай клас DragonGuild, който управлява членове и победите им над дракони.
# Всеки член има име, ниво и списък с победи (като речник {дракон: награда}).
# Изисквания:
# add_hunter(name, level) — добавя ловец, ако го няма.
# record_victory(name, dragon, reward) — добавя победа и награда.
# total_rewards(name) — връща общата награда на ловец.
# top_hunter() — връща името на ловеца с най-много общи награди.

class DragonGuild:
    def __init__(self):
        self.hunter_dict = {}

    def add_hunter(self, name, level):
        self.hunter_dict[name] = {}
        self.hunter_dict[name]["level"] = level

    def record_victory(self, name, dragon, reward):
        if name not in self.hunter_dict:
            self.add_hunter(name, 1)
            self.record_victory(self, name, dragon, reward)
        else:
            self.hunter_dict[name][dragon] = reward


    def total_rewards(self, name):
        total_sum = 0
        # if name in self.hunter_dict:
        #     for curr_name, curr_value in self.hunter_dict[name].items():
        #         if curr_name == "level":
        #             continue
        #         else:
        #             total_sum += curr_value
        #     return total_sum
        # return f"The {name} is not in dict"
        if name not in self.hunter_dict:
            return f"The {name} is not in dict"
        return sum([curr_value for curr_name, curr_value in self.hunter_dict[name].items() if curr_name != "level"])

    def hunter_point(self):
        hunter_point_dict = {}
        for curr_name, curr_value in self.hunter_dict.items():
            hunter_point_dict[curr_name] = self.total_rewards(curr_name)
        return hunter_point_dict

    def top_hunter(self):
        # return sorted(self.hunter_point().items(), key=lambda x: -x[1])[0][0]
        return sorted(self.hunter_dict.items(), key=lambda x: -self.total_rewards(x[0]))[0][0]

    # max(self.hunters, key=lambda name: self.total_rewards(name))




# Тест:
g = DragonGuild()
g.add_hunter("Ivan", 10)
g.add_hunter("Maria", 12)
g.record_victory("Ivan", "FireDrake", 500)
g.record_victory("Ivan", "SkySerpent", 300)
g.record_victory("Maria", "ShadowWing", 900)
print(g.hunter_dict)
print(g.total_rewards("Ivan"))
print(g.total_rewards("Dragan"))
print(g.total_rewards("Maria"))
print(g.hunter_point())
print(g.top_hunter()) # Maria
#
