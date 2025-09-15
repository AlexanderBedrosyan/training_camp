# Задача 4: Сравнение на спортни отбори
# Клас Team:
#   name
#   wins
# Имплементирайте:
# __ge__ → сравнява по победи
# __eq__ → равни, ако победите са равни

class Team:
    def __init__(self, name, wins):
        self.name = name
        self.wins = wins

    def __ge__(self, other):
        return self.wins >= other.wins

    def __eq__(self, other):
        return self.wins == other.wins

# Пример:

t1 = Team("Tigers", 10)
t2 = Team("Lions", 8)
print(t1 >= t2)  # True
print(t1 == t2)  # False