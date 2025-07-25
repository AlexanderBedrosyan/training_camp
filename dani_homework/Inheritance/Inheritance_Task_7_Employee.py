# Employees
# Създай клас Employee с атрибути name и salary.
# Създай клас Developer, който наследява Employee и
# има допълнителен атрибут programming_language.
# Добави метод code(), който принтира "{name} is coding in {programming_language}."

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def code(self):
        print(f"{self.name} is coding in {self.programming_language}.")

# Тест
dev = Developer("Alice", 5000, "Python")
dev.code()
