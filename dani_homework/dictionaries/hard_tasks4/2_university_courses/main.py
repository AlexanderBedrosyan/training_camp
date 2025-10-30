from course import Course
from grade_book import GradeBook
from student import Student

s1 = Student("Ivan")
s2 = Student("Ivan")
s3 = Student("Ivan")

s1.add_grade("Math", 3.5)
s1.add_grade("Art", 5.5)
s1.add_grade("BEL", 4.5)

print(s1.average())
print(s2.average())

c1 = Course("First year")
c2 = Course("Second year")
c1.add_student(s1)
print(c1.course_average())

gb = GradeBook()
gb.add_courses(c1)
gb.add_courses(c2)

print(gb.best_student())
print(gb.top_course())