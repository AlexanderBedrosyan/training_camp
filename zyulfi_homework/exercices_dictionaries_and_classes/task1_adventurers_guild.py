# Задача 1: Гилдия на приключенците
# Създай клас Guild, който управлява списък от приключенци и техните точки опит.
#
# Условия:
# Приключенците се пазят в речник {име: точки}.
# Метод add_adventurer(name, points) добавя приключенец или увеличава точките му.
# Метод top_adventurer() връща името на приключенеца с най-много точки.
# Метод average_points() връща средния опит на всички.

class Guild:
    def __init__(self):
        self.list_of_adventurers = []

    def add_adventurer(self, name, points):
        for element in self.list_of_adventurers:
            if name in element:
                element[name] += points
                return
        dict_curr_adventurer = {}
        dict_curr_adventurer[name] = points
        self.list_of_adventurers.append(dict_curr_adventurer)

    def top_adventurer(self):
        return list(sorted(self.list_of_adventurers, key=lambda x: -list(x.values())[0])[0])[0]

    def average_points(self):
        aver_point = 0
        for element in self.list_of_adventurers:
            aver_point += list(element.values())[0]
        return aver_point / len(self.list_of_adventurers)


# Тест:
g = Guild()
g.add_adventurer("Ivan", 120)
g.add_adventurer("Petar", 80)
g.add_adventurer("Ivan", 30)

print(g.list_of_adventurers)

print(g.top_adventurer())  # Ivan
print(round(g.average_points(), 2))  # 115.0
