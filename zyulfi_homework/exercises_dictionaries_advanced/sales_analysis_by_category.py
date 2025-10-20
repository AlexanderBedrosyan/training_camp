# Задача 1: Анализ на продажби по категории
# Условие:
# Напиши функция analyze_sales(data), която приема речник с категории и
# списък от продажби за всяка категория. Трябва да върне речник с:
# средна продажба за всяка категория (закръглена до 2 десетични),
# категорията с най-висока обща продажба.

# {'average_sales': {'Електроника': 983.33, 'Дрехи': 350.0, 'Храни': 176.67},
# 'top_category': 'Електроника'}

def analyze_sales(curr_data):
    new_dict = {}
    new_dict["average_sales"] = {}
    new_dict["top_category"] = ""

    for key, value in curr_data.items():
        average_value = round((sum(value) / len(value)),2)
        # {"average_dales": {}, "top_category": ""}
        new_dict["average_sales"][key] = average_value

    d = sorted(new_dict["average_sales"].items(), key=lambda item: - item[1])[0][0]

    new_dict["top_category"] = d

    return new_dict

data = {
  "Електроника": [1200, 800, 950],
  "Дрехи": [300, 500, 250],
  "Храни": [150, 200, 180]
}

print(analyze_sales(data))

# Очакван изход:
# {'average_sales': {'Електроника': 983.33, 'Дрехи': 350.0, 'Храни': 176.67},
# 'top_category': 'Електроника'}
