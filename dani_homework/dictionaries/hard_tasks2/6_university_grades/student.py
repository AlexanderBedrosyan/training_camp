# Student: име, private __grades (dict: курс → оценка); методи add_grade(), average()
class Student:
    def __init__(self, name):
        self.name = name
        self.__grades = {}

    def add_grade(self, curr_course, curr_grade):
        if curr_course not in self.__grades:
            self.__grades[curr_course] = []
        self.__grades[curr_course].append(curr_grade)

    def get_grades(self):
        return self.__grades

    def average(self):
        av_grade = 0
        count_grades = 0
        for curr_list_grades in self.__grades.values():
            for curr_grade in curr_list_grades:
                av_grade += curr_grade
                count_grades +=1
        return av_grade / count_grades



