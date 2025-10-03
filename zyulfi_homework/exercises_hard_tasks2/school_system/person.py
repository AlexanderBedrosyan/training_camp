# Person: name, age; метод __str__()

class Person:
    def __init__(self, name=str, age=float or int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The {self.name} is {self.age} ages."

