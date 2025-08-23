# super() използване
# Създай клас person с атрибут name.
# Създай клас Student, който наследява person и има допълнителен атрибут student_id.
# Използвай super() за инициализация.
# Добави метод, който принтира "{name}'s ID is {student_id}".

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def print_info(self):
        print(f"{self.name}'s ID is {self.student_id}")


student = Student("Name", "7777777")
student.print_info()


