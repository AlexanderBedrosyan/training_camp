# Student: име, private __grades (dict: курс → оценка); методи add_grade(), average()

class Student:
    def __init__(self, name=str):
        self.name = name
        self.__grades = {}

    def add_grade(self, course=str, grade=float) -> None:
        self.__grades[course] = grade

    def average(self):
        return sum([curr_grade for curr_grade in self.__grades.values()]) / len(self.__grades)

    def get_value(self) -> dict:
        return self.__grades