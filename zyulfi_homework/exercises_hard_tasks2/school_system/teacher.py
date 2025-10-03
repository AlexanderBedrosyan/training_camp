# Teacher (наследява Person): subject, private __students; методи add_student(), class_average()
from exercises_hard_tasks2.school_system.person import Person
from exercises_hard_tasks2.school_system.student import Student


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        self.__students: list[Student] = []

    def add_student(self, curr_student=object) -> None:
        self.__students.append(curr_student)

    def class_average(self) -> float:
        return sum([curr_student.average() for curr_student in self.__students]) / len(self.__students)
    


