# Student: име, private __grades (dict: курс → оценка), методи add_grade(course, grade), average()

class Student:
    def __init__(self, name):
        self.name = name
        self.__grades = {}

    def add_grade(self, course, grade):
        self.__grades[course] = grade

    def average(self):
        aver_grade = 0
        for current_grade in self.__grades.values():
            aver_grade += current_grade
        return aver_grade / len(self.__grades)
