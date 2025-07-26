# 🔹 Задача 9
# Създай клас Course с атрибути name и students (списък). Добави метод add_student(student_name), който добавя студент,
# и метод get_students_count(), който връща броя на студентите.
# Създай клас ProgrammingCourse, наследяващ Course, и добави метод add_language(language), който добавя език за курса
# в нов атрибут languages (списък).
from typing import List


class Course:

    def __init__(self, name=str, students=List):
        self.name = name
        self.students = students

    def add_student(self, student_name=str) -> None:
        self.students.append(student_name)

    def get_students_count(self) -> int:
        return len(self.students)

class ProgrammingCourse(Course):

    def __init__(self, name=str, students=List, languages=List):
        super().__init__(name, students)
        self.languages = languages

    def add_language(self, language=str) -> None:
        self.languages.append(language)


current_students = ["Gosho", "Trosho", "Dragancho"]
current_languages = ["Python", "R", "JAVA"]

programming_course = ProgrammingCourse("Basic Course", [], [])

print(programming_course.name)
print(programming_course.students)
print(programming_course.languages)
print(programming_course.get_students_count())

for student in current_students:
    programming_course.add_student(student)

for current_language in current_languages:
    programming_course.add_language(current_language)

print(programming_course.students)
print(programming_course.languages)
print(programming_course.get_students_count())

