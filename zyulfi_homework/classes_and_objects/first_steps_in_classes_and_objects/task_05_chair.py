# Задача 5
# Създай клас Chair, който има атрибут material.
# Добави метод describe(), който принтира "This chair is made of {material}."

class Chair:
    def __init__(self, material):
        self.material = material

    def describe (self):
        print(f"This chair is made of {self.material}.")

current_chair = Chair(input("Enter the material the chair is made of: "))
Chair.describe(current_chair)