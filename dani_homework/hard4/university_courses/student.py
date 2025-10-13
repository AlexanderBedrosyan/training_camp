# Student Атрибути: name, private __grades (dict: course → grade)
# Методи: add_grade(course, grade), average() (проверка дали има оценки)

class Student:
    def __init__(self, name:str):
        self.name = name
        self.__grades = {}
        # {"Math": 5.50}

    def add_grade(self, course:str, grade:float):
        self.__grades[course] = grade

    def average(self):
        if len(self.__grades) == 0:

            return 0
        return sum([current_grade for current_grade in self.__grades.values()]) / len(self.__grades)




