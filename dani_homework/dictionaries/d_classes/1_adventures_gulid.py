# Задача 1: Гилдия на приключенците
# Създай клас Guild, който управлява списък от приключенци и техните точки опит.
# Условия:
# Приключенците се пазят в речник {име: точки}.
# Метод add_adventurer(name, points) добавя приключенец или увеличава точките му.
# Метод top_adventurer() връща името на приключенеца с най-много точки.
# Метод average_points() връща средния опит на всички.
class Guild:
    def __init__(self):
# речник във вида {име: точки_опит}
        self.adventurers = {}

    def add_adventurer(self, name: str, points: float):
# Добавя приключенец или увеличава неговите точки, ако вече съществува.

        if points < 0:
            raise ValueError("Точките не могат да бъдат отрицателни.")

        if name in self.adventurers:
            self.adventurers[name] += points
        else:
            self.adventurers[name] = points

    def top_adventurer(self) -> str:
# Връща името на приключенеца с най-много точки.
# Ако няма приключенци, връща None.

        if not self.adventurers:
            return None
        return max(self.adventurers, key=self.adventurers.get)

    def average_points(self) -> float:
# Изчислява средния брой точки на всички приключенци.

        if not self.adventurers:
            return 0.0
        total = sum(self.adventurers.values())
        return total / len(self.adventurers)

    def __str__(self):
        return f"Guild({len(self.adventurers)} adventurers)"

from guild import Guild

# Тестови данни
g = Guild()
g.add_adventurer("Ivan", 120)
g.add_adventurer("Petar", 80)
g.add_adventurer("Ivan", 30)

print(g.top_adventurer())           # Ivan
print(round(g.average_points(), 2)) # 115.0



# Данните се пазят в речник {име: точки}.
# Ако даден приключенец вече съществува, методът add_adventurer просто добавя допълнителните точки.
# top_adventurer() намира този с най-висок опит чрез max(..., key=dict.get).
# average_points() изчислява средното от всички стойности в речника.













# Тест:
# g = Guild()
# g.add_adventurer("Ivan", 120)
# g.add_adventurer("Petar", 80)
# g.add_adventurer("Ivan", 30)
# print(g.top_adventurer())  # Ivan
# print(round(g.average_points(), 2))  # 115.0