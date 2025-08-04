# Задача 3
# Създай клас Employee с атрибут name и метод work(), връщащ "{name} is working".
# Създай клас Manager, наследяващ Employee, и добави метод manage() връщащ "{name} is managing".

class Employee:
    def __init__(self, name=str):
        self.name = name

    def work(self) -> str:
        return f"{self.name} is working"

class Manager(Employee):
    def manage(self) -> str:
        return f"{self.name} is managing"

current_employee = Employee("Gugov")
current_manager = Manager("Petkan")
print(current_employee.work())
print(current_manager.manage())