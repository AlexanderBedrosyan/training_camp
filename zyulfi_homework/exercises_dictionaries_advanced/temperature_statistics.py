# Задача 6: Температурни статистики
# Условие:
# Функция temp_stats(data) приема речник град -> [температури] и връща за всеки град средна,
# макс и мин температура (средната закръглена до 2).

def temp_stats(curr_temps):
    new_dict = {}
    for key, value in curr_temps.items():
        average_temp = round(sum(value) / len(value), 2)
        min_temp = min(value)
        max_temp = max(value)
        new_dict[key] = {"avg":average_temp, 'max': max_temp, 'min': min_temp}
        curr_temps[key] = {"avg":average_temp, 'max': max_temp, 'min': min_temp}

    return new_dict

temps = {"Sofia":[20,22,25], "Varna":[18,19,17]}

print(temp_stats(temps))

# Очакван изход:
# {'Sofia': {'avg': 22.33, 'max': 25, 'min': 20}, 'Varna': {'avg': 18.0, 'max': 19, 'min': 17}}
