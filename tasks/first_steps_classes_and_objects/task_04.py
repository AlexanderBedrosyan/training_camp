# Напиши клас Student, който приема име и списък от оценки. Добави метод, който връща средната оценка.
from typing import List

class Student:

    def __init__(self, name=str, list_of_results=List):
        self.name = name
        self.list_of_results = list_of_results

    def avg_result(self):
        total_result = sum(self.list_of_results)
        numbers_of_results = len(self.list_of_results)

        return round(total_result / numbers_of_results, 2)

    def student_name_and_avg_result(self):
        return f"Student: {self.name} with average result: {self.avg_result()}"

current_results = [4, 5, 6, 2, 3.40, 4.77, 6, 6, 6, 6]
# Obj
student = Student("Dragancho", current_results)
# Print avg result
print(student.avg_result())
# Print method with details for average result
print(student.student_name_and_avg_result())