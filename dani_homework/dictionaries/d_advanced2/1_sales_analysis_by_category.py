# Задача 1: Анализ на продажби по категории
# Условие: Напиши функция analyze_sales(data), която приема
# речник с категории и списък от продажби за всяка категория.
# Трябва да върне речник с:
# -средна продажба за всяка категория (закръглена до 2 десетични),
# -категорията с най-висока обща продажба.
# Примерен тест:
# def analyze_sales(data):
# averages = {cat: round(sum(vals)/len(vals),
# for cat, vals in data.items()}
# top_category = max(data, key=lambda c: sum(data[c]))
# return {"average_sales": averages, "top_category": top_category}
from pprint import pprint


data = {
    "Електроника": [1200, 800, 950],
    "Дрехи": [300, 500, 250],
    "Храни": [150, 200, 180]
}
def analyze_sales(data):
    av_sales = {
        cat: round(sum(sales) / len(sales), 2)
        for cat, sales in data.items()
    }
    #print("av_sales:\n", av_sales)

    totals = {cat: sum(sales)
              for cat, sales in data.items()
    }
    #print("totals:\n", totals)

    top_cat = max(data, key=lambda cat: sum(data[cat]))
    #print("top_cat:\n", top_cat)

    return {"av_sales": av_sales,
            "totals": totals,
            "top_cat": top_cat
    }

pprint(analyze_sales(data))
#print(analyze_sales(data))

# Очакван изход:{'average_sales': {'Електроника': 983.33, 'Дрехи': 350.0, 'Храни': 176.67}, 'top_category': 'Електроника'}
