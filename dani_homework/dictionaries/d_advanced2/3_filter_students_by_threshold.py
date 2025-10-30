# Условие:
# Функция filter_students(data, min_grade) връща нов речник само с учениците,
# чиито средни оценки са >= min_grade.
# Примерен тест: def filter_students(data, min_grade):
# return {n: s for n, s in data.items() if sum(s)/len(s) >= min_grade}
from pprint import  pprint

def filter_students(data, min_grade):
    dict_result = {n: s for n, s in data.items() if sum(s) / len(s) >= min_grade}
    return dict_result

students = {"Иван": [4,5], "Мария": [6,6], "Петър": [3,4]}

pprint(filter_students(students, 4))
# Очакван изход: {'Мария': [6, 6]}