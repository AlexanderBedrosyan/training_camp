# Person
# Атрибути: name, age
# Метод: __str__()

class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} old."


