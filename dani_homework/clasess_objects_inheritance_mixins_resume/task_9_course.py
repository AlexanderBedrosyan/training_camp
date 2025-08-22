# Създай клас Course с атрибути name и students (списък).
# Добави метод add_student(student_name), който добавя студент,
# и метод get_students_count(), който връща броя на студентите.
# Създай клас ProgrammingCourse, наследяващ Course,
# и добави метод add_language(language),
# който добавя език за курса в нов атрибут languages (списък).
# ------------------------------------------------------------

class Course:
    def __init__(self, name: str, students: list)-> None:
        self.name: str = name
        self.students: list = (students)

    def add_student(self, student_name: str)-> None:
        self.students.append(student_name)


    def get_students_count(self)-> int:
        return len(self.students)

class ProgrammingCourse(Course):
    def __init__(self, name: str, students: list, languages: list)-> None:
        super().__init__(name, students)
        self.languages: list = (languages)

    def add_language(self, language: str)-> None:
        self.languages.append(language)

c = Course("C++", ["Mime", "Mome", "Pepi"])
print(c.get_students_count())

c.add_student("Marcheto")
print(c.get_students_count())

pc = ProgrammingCourse("Python Basics", ["Ivan", "Elena"], ["Python"])
pc.add_student("Gosho")
pc.add_language("C#")
print(pc.get_students_count())  # 3
print(pc.languages)


