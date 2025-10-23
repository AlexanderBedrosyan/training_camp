# Course: име, списък от студенти; метод average_grade()
from exercises_hard_tasks2.university_grades.student import Student


class Course:
    def __init__(self, name=str):
        self.name = name
        self.list_of_students: list[Student] = []

    def add_student(self, curr_student=object) -> None:
        self.list_of_students.append(curr_student)

    def average_grade(self) -> float:
        aver_value = 0
        for curr_student in self.list_of_students:
           aver_value += curr_student.average()
        return aver_value / len(self.list_of_students)


        return sum([curr_student.get_value().values() for curr_student in self.list_of_students]) / len(self.list_of_students)

    def best_student_of_course(self) -> object:
        bs_st_course = None
        bs_grade_course = 0

        for curr_student in self.list_of_students:
            if curr_student.average() >= bs_grade_course:
                bs_grade_course = curr_student.average()
                bs_st_course = curr_student
        return bs_st_course

