# Задача 4: Сливане на продажби (сумиране)
# Условие:
# Функция merge_sales(q1, q2) обединява два речника продукт -> продажби.
# Ако продуктът е в двата речника, стойностите се сумират.

def merge_sales(sales_q1, sales_q2):
    for key, value in sales_q2.items():
        if key not in sales_q1:
            sales_q1[key] = 0
        sales_q1[key] += value
        # if key in sales_q1:
        #     sales_q1[key] += value
        # else:
        #     sales_q1[key] = value

    print(sales_q1)




sales_q1 = {"A": 100, "B": 200}
sales_q2 = {"A": 150, "C": 300}
print(merge_sales(sales_q1, sales_q2))

# Очакван изход:
# {'A': 250, 'B': 200, 'C': 300}
