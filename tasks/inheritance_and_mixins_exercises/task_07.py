# 🔹 Задача 7
# Създай клас Person с атрибути name и age. Добави метод birthday(), който увеличава възрастта с 1 и
# връща новата възраст.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1
        return self.age


current_person = Person("Alexander", 33)
print(current_person.age)
print(current_person.birthday())
print(current_person.age)