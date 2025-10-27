# GradeMixin
# Метод: best_student(students)
from oop_mixin_tasks.university.student import Student


class GradeMixin:
    def best_student(self, student=Student) -> float:
        return student.average()

