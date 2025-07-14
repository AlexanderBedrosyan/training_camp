# Създай функция, която приема матрица и връща сумата на всички елементи, които се намират на главния диагонал.
#
# Пример:
#
# matrix = [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]

# Резултат: 15  # 1+5+9

def calculation_of_main_diagonal(current_matrix):
    sum_element = 0

    for i in range(len(current_matrix)):
        sum_element += current_matrix[i][i]

    return sum_element
    # return sum([current_matrix[i][i] for i in range(len(current_matrix))])


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(calculation_of_main_diagonal(matrix))

