# Задача 7: Университетска система
# Създай клас University, който следи преподаватели и студенти.
# Условия:
# Речник {преподавател: {"students": [списък], "subject": предмет}}
# Метод add_teacher(name, subject)
# Метод add_student(teacher, student)
# Метод teacher_load(teacher) – брой студенти на преподавателя.
# Метод most_loaded_teacher() – връща най-натоварения преподавател.










# Тест:
# u = University()
# u.add_teacher("Dr. Ivanov", "Math")
# u.add_teacher("Dr. Petrov", "Physics")
# u.add_student("Dr. Ivanov", "Anna")
# u.add_student("Dr. Ivanov", "Boris")
# print(u.most_loaded_teacher())  # Dr. Ivanov