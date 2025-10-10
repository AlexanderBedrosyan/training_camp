#Person: name, age; метод __str__()

class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} old"

#test
p=Person("Ivan", 50)
print(p.__str__())