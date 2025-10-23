# Student
# Атрибути: name, private __grades
# Методи: add_grade(), average()

class Student():
    def __init__(self, name=str):
        self.name = name
        self.__grades = []

    def add_grade(self, curr_grade) -> None:
        if 2 <= curr_grade <= 6:
            self.__grades.append(curr_grade)
        else:
            print("Error")

    def average(self):
        return sum([curr_grade for curr_grade in self.__grades]) / len(self.__grades)

