# ✅ Задача 7 – Employees Създай клас Employee с атрибути name и salary. Създай клас Developer, който наследява Employee
# и има допълнителен атрибут programming_language. Добави метод code(), който принтира "{name} is coding
# in {programming_language}."

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):

    def __init__(self, name, salary, programming_language, experience_time):
        super().__init__(name, salary)
        self.programming_language = programming_language
        self.experience_time = experience_time # years

    def code(self):
        print(f"{self.name} is coding in {self.programming_language}. \n Current salary: {self.salary}. \n Experience: {self.experience_time}")

    def add_more_money(self, money):
        self.salary += money

    def add_year(self):
        self.experience_time += 1
        self.add_more_money(1000)

developer = Developer("Goshko", 3000, "Python", 1)
developer.code()
developer.add_year()
developer.add_more_money(200)

developer.code()

