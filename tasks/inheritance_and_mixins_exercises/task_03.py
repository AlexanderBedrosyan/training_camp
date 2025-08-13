# 🔹 Задача 3
# Създай клас Employee с атрибут name и метод work(), връщащ "{name} is working".
# Създай клас Manager, наследяващ Employee, и добави метод manage() връщащ "{name} is managing".

class Employee:

    def __init__(self, name):
        self.name = name # Gosho

    def work(self):
        return f"{self.name} is working."


class Manager(Employee):

    def manage(self):
        return f"{self.name} is managing."


current_employee = Employee("Gosho") # object with name Gosho
print(current_employee.work())

manager = Manager(current_employee.name) # received a name from the object which was issued earlier on row 20
print(manager.manage())