# Student
# Атрибути: name, private __grades (dict)
# Методи: add_grade(course, grade) # average()
class Student:
    def __init__(self, name:str):
        self.name = name
        self.__grades = {}

    def add_grade(self, course, grade):
        self.__grades[course] = grade

    def average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades.values()) / len(self.__grades)

    def __str__(self) -> str:
        return f"{self.name} (avg: {self.average():.3f})"