from student import Student
from course import Course
from university import University

s1 = Student("Anna")
s2 = Student("Mark")
s3 = Student("Lily")

c1 = Course("Math")
c1.add_student(s1)
c1.add_student(s2)

c2 = Course("Physics")
c2.add_student(s2)
c2.add_student(s3)

s1.add_grade("Math", 5.5)
s2.add_grade("Math", 6)
s2.add_grade("Physics", 5)
s3.add_grade("Physics", 5.8)

uni = University()
uni.add_course(c1)
uni.add_course(c2)

print("Best student:", uni.best_student().name)
