# Създай клас University, който следи преподаватели и студенти.
# Условия: Речник {преподавател: {"students": [списък], "subject": предмет}}
# Метод add_teacher(name, subject)
# Метод add_student(teacher, student)
# Метод teacher_load(teacher) – брой студенти на преподавателя.
# Метод most_loaded_teacher() – връща най-натоварения преподавател.
class University:
    def __init__(self):
# Структура: {преподавател: {"students": [списък], "subject": предмет}}
        self.teachers = {}

    def add_teacher(self, name: str, subject: str):
# Добавя преподавател, ако го няма.
        if name not in self.teachers:
            self.teachers[name] = {"students": [], "subject": subject}

    def add_student(self, teacher: str, student: str):
# Добавя студент към преподавателя (ако го няма, не прави нищо).
        if teacher not in self.teachers:
            print(f"❌ Преподавател {teacher} не съществува!")
            return
        self.teachers[teacher]["students"].append(student)

    def teacher_load(self, teacher: str) -> int:
# Връща броя на студентите на даден преподавател.
        if teacher not in self.teachers:
            return 0
        return len(self.teachers[teacher]["students"])

    def most_loaded_teacher(self) -> str:
# Връща името на най-натоварения преподавател (с най-много студенти).
        if not self.teachers:
            return None
        return max(self.teachers, key=lambda t: len(self.teachers[t]["students"]))

    def __str__(self):
        return f"University({len(self.teachers)} teachers)"
# Тест:
u = University()
u.add_teacher("Dr. Ivanov", "Math")
u.add_teacher("Dr. Petrov", "Physics")
u.add_student("Dr. Ivanov", "Anna")
u.add_student("Dr. Ivanov", "Boris")
print(u.most_loaded_teacher())  # Dr. Ivanov