# Създай клас Employee с атрибут name
# и метод work(), връщащ "{name} is working".
# Създай клас Manager, наследяващ Employee,
# и добави метод manage() връщащ "{name} is managing".
# -------------------------------------------------------------------------

class Employee:
    def __init__(self, name: str)-> None:
        self.name: str = name

    def work(self):
        return f"{self.name} is working"

class Manager(Employee):
    def __init__(self, name: str)-> None:
        super().__init__(name)

    def manage(self):
        return f"{self.name} is managing"

e = Employee("A")
print(e.work())      #A is working

m = Manager("B")
print(m.work())      # B is working
print(m.manage())    # B is managing
