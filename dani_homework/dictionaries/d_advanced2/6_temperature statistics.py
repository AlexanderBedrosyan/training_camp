# Условие:
# Функция temp_stats(data) приема речник град -> [температури] и връща за всеки град средна, макс и мин температура (средната закръглена до 2).
#
# Примерен тест: ```python def temp_stats(data): res = {} for city, vals in data.items(): res[city] = {"avg": round(sum(vals)/len(vals), 2), "max": max(vals), "min": min(vals)} return res
#
# temps = {"Sofia":[20,22,25], "Varna":[18,19,17]}
# print(temp_stats(temps))
# # Очакван изход:
# # {'Sofia': {'avg': 22.33, 'max': 25, 'min': 20}, 'Varna': {'avg': 18.0, 'max': 19, 'min': 17}}

def temp_stats(data):
    res = {}
    for city, vals in data.items():
        res[city] = {
            "avg": round(sum(vals) / len(vals), 2),
            "max": max(vals),
            "min": min(vals)
        }
    return res


# --- Примерен тест ---
temps = {"Sofia": [20, 22, 25], "Varna": [18, 19, 17]}
print(temp_stats(temps))
# {'Sofia': {'avg': 22.33, 'max': 25, 'min': 20}, 'Varna': {'avg': 18.0, 'max': 19, 'min': 17}}
