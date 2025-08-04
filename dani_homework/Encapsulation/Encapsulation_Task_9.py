# Създай клас Student, в който се пази списък от всички студенти като клас атрибут.
# При създаване на обект, студентът се добавя в този списък.
# Напиши метод, който връща броя на студент

# --------------------------------------------------------------------------

class Student:
    all_students: list['Student'] = []      # списък от обекти от тип Student

    def __init__(self, name: str) -> None:
        self.name: str = name
        Student.all_students.append(self)   # добавяне в списъка при създаване

    @classmethod
    def count_students(cls) -> int:
        return len(cls.all_students)        # връща броя на студентите


# инициализирам няколко обекта-студенти
s1 = Student("Muncho")
s2 = Student("Boncho")
s3 = Student("Toncho")
s4 = Student("Guncho")

# Извикваме метода, който връща броя на студентите
print("Брой студенти:", Student.count_students())                       # -> int (в случая: 2)

# Проверка на списъка
print("Имена на студентите:", [s.name for s in Student.all_students])   # -> list[str]
