from student import Student
from professor import Professor

s = Student("Eva", 20)
s.add_grade(5)
s.add_grade(6)
print(s.average())  # 5.5

p = Professor("Dr. John", 50)
p.add_course("Math")
print(p.list_courses())