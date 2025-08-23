# Student: име, private __grades (dict: курс → оценка), методи add_grade(course, grade),
# average()

class Student:
    def __init__(self, name=str):
        self.name = name
        self.__grades = {}

    def add_grade(self, course=str, grade=float):
        self.__grades[course] = grade

    def average(self) -> float:
        average_grades = 0
        for curr_course in self.__grades.values():
            average_grades += curr_course
        return average_grades / len(self.__grades)