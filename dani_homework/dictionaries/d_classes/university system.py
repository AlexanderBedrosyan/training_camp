# Създай клас University, който следи преподаватели и студенти.
# Условия: Речник {преподавател: {"students": [списък], "subject": предмет}}
# Метод add_teacher(name, subject)
# Метод add_student(teacher, student)
# Метод teacher_load(teacher) – брой студенти на преподавателя.
# Метод most_loaded_teacher() – връща най-натоварения преподавател.
from  pprint import pprint

class University:
    def __init__(self):
        self.teachers = {}

    def add_teacher(self, name, subject):
        self.teachers[name] = {}
        self.teachers[name]["subject"] = subject
        self.teachers[name]["students"] = []

    def add_student(self, teacher, student):
        if teacher not in self.teachers:
            self.add_teacher(teacher, "no subject")

        self.teachers[teacher]["students"].append(student)

    def teacher_load(self, teacher):
        print(self.teachers[teacher])
        return len(self.teachers[teacher]["students"])

    def most_loaded_teacher(self):
        pprint(self.teachers)
        return sorted(self.teachers.items(), key=lambda x: -len(x[1]["students"]))[0][0]

# Тест:
u = University()
u.add_teacher("Dr. Ivanov", "Math")
u.add_teacher("Dr. Petrov", "Physics")
u.add_student("Dr. Ivanov", "Anna")
u.add_student("Dr. Ivanov", "Boris")
u.add_student("Dr. Petkov", "Boris")
print(u.teacher_load("Dr. Ivanov"))
print(u.most_loaded_teacher())  # Dr. Ivanov