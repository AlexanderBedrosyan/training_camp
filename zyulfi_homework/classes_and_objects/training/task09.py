# Задача 9
# Създай клас Student, в който се пази списък от всички студенти като клас атрибут.
# При създаване на обект, студентът се добавя в този списък.
# Напиши метод, който връща броя на студентите.

class Student:
    list_student = []

    def __init__(self, student=str) -> None:
        self.student = student

    setattr(current_student,  )

    list_student.append(student)

    def num_student(self):
        return len(list_student)

current_student = Student("Zyulfi")

print(num_student())


# # Задача 4
# # Създай клас Settings с атрибут theme. Използвай getattr, setattr и hasattr,
# # за да достъпиш, промениш и провериш theme.
#
# class Settings:
#     def __init__(self, theme=str):
#         self.theme = theme
#
# current_settings = Settings("Black")
#
# print(getattr(current_settings, "theme"))
# setattr(current_settings, "theme", "white")
# print(current_settings.theme)
# print(hasattr(current_settings, "theme"))
# print(hasattr(current_settings, "name"))
