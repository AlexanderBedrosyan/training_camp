# Course Атрибути: title, списък студенти
# Методи: add_student(student), course_average()
from student import Student


class Course:
    def __init__(self, title:str):
        self.title = title
        self.students: list[Student] = []

    def add_student(self, current_student):
        self.students.append(current_student)

    def course_average(self):
        c_av = 0
        st_n = 0
        for curr_student in self.students:
            if curr_student.average() == 0:
                continue
            st_n += 1
            c_av += curr_student.average()

        if st_n == 0 or c_av == 0:
            return 0

        return c_av / st_n

    def best_student_course(self):
        best_st = None
        best_gr = 0
        for curr_st in self.students:
            if best_gr <= curr_st.average():
                best_gr = curr_st.average()
                best_st = curr_st
        return best_st
