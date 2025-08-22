# Създай клас person с атрибути name и age.
# Добави метод birthday(), който увеличава възрастта с 1 и връща новата възраст.
# -------------------------------------------------------------------------------

class Person:
    def __init__(self, name: str, age: int)-> None:
        self.name: str = name
        self.age: int = age

    def birthday(self)-> int:
        self.age += 1
        return self.age


p = Person("Maya", 32)
print(p.birthday())
print(p.birthday())