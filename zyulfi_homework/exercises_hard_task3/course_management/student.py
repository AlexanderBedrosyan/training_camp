# Атрибути: name, private __grades (dict)
# Методи:
# add_grade(course, grade)
# average()

class Student:
    def __init__(self, name):
        self.name = name
        self.__grades = {}

    def grades(self):
        return self.__grades

    def add_grade(self, course, grade):
        if course not in self.__grades:
            self.__grades[course] = []

        self.__grades[course].append(grade)

    def average(self):
        total = 0
        counter = 0
        for grades in self.__grades.values():
            for grade in grades:
                total += grade
                counter += 1
        return total / counter

