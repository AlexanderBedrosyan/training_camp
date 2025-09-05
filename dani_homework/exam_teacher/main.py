from student import Student
from teacher import Teacher

s = Student("Ivan", 5.5)
t = Teacher("Petrov", "Math")

s.show_info()
t.show_info()
print(Student.school_name)

s.grade = 6
print(s.grade)

try:
    s.grade = 7
except ValueError as e:
    print("Error:", e)

        




