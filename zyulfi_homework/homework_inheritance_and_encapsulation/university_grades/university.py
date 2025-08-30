# Атрибути: name, private __courses
# Методи:
# add_course(course) → добавя курс
# best_student() → най-добрият студент във всички курсове
# average_university() → средната оценка за университета
from course import Course

class University:
    def __init__(self, name=str):
        self.name = name
        self.__courses: list[Course] = []

    def add_course(self, curr_course=object) -> None:
        self.__courses.append(curr_course)

    def best_student(self) -> object:
        best_all_course_grade = 0
        best_student_all_course = None
        for curr_student in self.__courses:
            if best_all_course_grade <= curr_student.average_grade():
                best_all_course_grade = curr_student.average_grade()
                best_student_all_course = curr_student
        return best_student_all_course

    def average_university(self) -> float:
        aver_uni = 0
        for curr_course in self.__courses:
            aver_uni += curr_course.average_grade()
        return aver_uni / len(self.__courses)