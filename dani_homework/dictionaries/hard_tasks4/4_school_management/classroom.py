# Classroom
# Атрибути: списък от ученици, класен ръководител
# Методи: average_grade(), best_student()

class Classroom:
    def __init__(self, teacher:object):
        self.teacher = teacher
        self.list_of_students: list = []

    def add_student(self, current_student):
        self.list_of_students.append(current_student)

    def average_grade(self):
        return sum([curr_st.average_grade_of_st() for curr_st in self.list_of_students]) / len(self.list_of_students)

    def best_student(self):
        best_st = None
        best_av_grade = 0
        for curr_st in self.list_of_students:
            if best_av_grade <= curr_st.average_grade_of_st():
                best_av_grade = curr_st.average_grade_of_st()
                best_st = curr_st
        return best_st.name


