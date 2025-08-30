# Атрибути: name, private __grades (dict: course → оценка)
# Методи:
# add_grade(course, grade) → добавя оценка (2–6)
# average() → връща средната оценка
# __str__() → "{name}, avg: {average}"

class Student:
    def __init__(self, name=str):
        self.name = name
        self.__grades = {}

    def add_grade(self, course=str, grade=float) -> None:
        self.__grades[course] = grade

    def average(self) -> float:
        aver_grade = 0
        for curr_values in self.__grades.values():
            aver_grade += curr_values
        return aver_grade / len(self.__grades)

    def __str__(self):
        return f"{self.name}, avg: {self.average}"

