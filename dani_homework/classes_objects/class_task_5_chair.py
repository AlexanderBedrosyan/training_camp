# Създай клас Chair, който има атрибут material.
# Добави метод describe(), който принтира "This chair is made of {material}."

class Chair:
    def __init__(self, material):
        self.material = material  #

    def describe(self):
        print(f"This chair is made of {self.material}.")

# Създаване на обекти
object_1 = Chair("wood")
object_2 = Chair("metal")

object_1.describe()  #
object_2.describe()  #