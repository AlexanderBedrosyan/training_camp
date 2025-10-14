# Условие:
# Функция filter_students(data, min_grade) връща нов речник само с учениците,
# чиито средни оценки са >= min_grade.

def filter_students(curr_data, min_grade):
    new_dict = {}

    for key, value in curr_data.items():
        av_gr = sum(value) / len(value)
        if av_gr >= min_grade:
            new_dict[key] = value
    return new_dict

students = {"Иван": [4,5], "Мария": [6,6], "Петър": [3,4]}
print(filter_students(students, 6))

# Очакван изход:
# {'Мария': [6, 6]}
