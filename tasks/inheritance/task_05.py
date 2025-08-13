# ✅ Задача 5 – super() използване Създай клас Person с атрибут name. Създай клас Student, който наследява Person и има
# допълнителен атрибут student_id. Използвай super() за инициализация. Добави метод, който принтира "{name}'s
# ID is {student_id}".

class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def student_details(self):
        print(f"{self.name}'s ID is {self.student_id}")

student = Student("Gosho", 13715)
student.student_details()