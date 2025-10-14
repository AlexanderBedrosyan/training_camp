# Задача 8: Най-добър ученик по предмет
# Условие:
# best_in_subject(students, subject) приема речник име -> {предмет: оценка} и връща името на ученика
# с най-добра оценка по subject.
# Ако няма оценки за предмета върни None.

def best_in_subject(students, subject):
    best_student = None
    best_grade = 0

    for name, dict_of_grades in students.items():
        try:
            curr_grade = dict_of_grades[subject]
            if curr_grade >= best_grade:
                best_grade = curr_grade
                best_student = name
        except KeyError:
            print("Error")
    return best_student if best_student else "No grades"


students = {"Иван":{"math":6,"bio":5},"Мария":{"math":5,"bio":6}}

print(best_in_subject(students, "bio"))

# Очакван изход:
# 'Мария'
