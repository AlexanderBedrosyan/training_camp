# Student (наследява Person): private __grades; методи add_grade(), average()
from exercises_hard_tasks2.school_system.person import Person


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__grades = []

    def add_grade(self, curr_grade=float) -> None:
        if 2 <= curr_grade <= 6:
            self.__grades.append(curr_grade)
        else:
            print("Error")

    def average(self) -> float:
        return sum([curr_grade for curr_grade in self.__grades]) / len(self.__grades)