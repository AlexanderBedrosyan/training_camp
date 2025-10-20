# История:
# Университет съхранява информация за студенти и оценки.
# Трябва да се определи най-добрият студент по среден успех.
# Условие:
# Създай функция best_student(students), която връща името и средния успех.


class University:

    def best_student(self, curr_data):
        best_student = None
        best_grade = 0

        for name, information in curr_data.items():
            current_avg_grades = [
                sum(list_grades) / len(list_grades)
                for list_grades in list(information.values()) # loop in list of lists [[5, 6, 6], [6, 5]]
            ]
            total_avg_grades = sum(current_avg_grades) / len(current_avg_grades)
            if best_grade <= total_avg_grades:
                best_grade = total_avg_grades
                best_student = name
        return (best_student, best_grade)


data = { "Иван": {"math":[5,6,6],"it":[6,5]},
         "Мария": {"math":[6,6,6],"it":[5,6]},
         "Петър": {"math":[4,4],"it":[5,4]} }

student = University()

print(student.best_student(data))

# Очакван изход: ('Мария', 5.83)