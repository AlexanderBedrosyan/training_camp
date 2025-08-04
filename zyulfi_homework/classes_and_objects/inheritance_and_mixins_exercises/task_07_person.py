# Задача 7
# Създай клас Person с атрибути name и age.
# Добави метод birthday(), който увеличава възрастта с 1 и връща новата възраст.

class Person:
    def __init__(self, name=str, age=int):
        self.name = name
        self.age = int(age)

    def birthday(self) -> int:
        self.age += 1
        return self.age


current_person = Person("Ivan", 25)
print(current_person.name)
print(current_person.age)
current_person.birthday()
print(current_person.name)
print(current_person.age)
current_person.birthday()
print(current_person.name)
print(current_person.age)