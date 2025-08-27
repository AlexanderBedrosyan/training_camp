# Атрибути: name, private __students (списък от Student)
# Методи:
# add_student(student) → добавя студент
# average_grade() → средна оценка на всички
# best_student() → студентът с най-висока средна оценка

from student import Student

class Course:
    def __init__(self, name=str):
        self.name = name
        self.__students: list[Student] = []

    def add_student(self, curr_student=object) -> None:
        self.__students.append(curr_student)

    def average_grade(self) -> float:
        average_grade_all_student = 0
        for curr_student in self.__students:
            average_grade_all_student += curr_student.average()
        return average_grade_all_student / len(self.__students)

    def best_student(self) -> object:
        best_average_grade = 0
        best_student = None
        for curr_student in self.__students:
            if best_average_grade <= curr_student.average():
                best_average_grade = curr_student.average()
                best_student = curr_student
        return best_student