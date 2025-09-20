# Задача 1: Сравнение на студенти
# Създайте клас Student с атрибути:
#   name
#   grade
# Имплементирайте:
# __eq__ → сравнява по оценка
# __lt__ → сравнява по оценка

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade

#Пример:
s1 = Student("Ivan", 5.5)
s2 = Student("Maria", 6.0)

print(s1 < s2)   # True
print(s1 == s2)  # False