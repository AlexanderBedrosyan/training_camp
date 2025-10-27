# ЗАДАЧА 10: Статистика на видеоигра
# История:
# Играчите преминават нива и трупат точки. Трябва да намериш най-добрия по коефициент.
# data = {"Иван":[10,20,30],"Мария":[40,50,60],"Петър":[20,20]} print(best_ratio(data))
#
# Очакван изход: ('Мария', 50.0)

class VideoGameStatistics:
    def __init__(self, curr_data):
        self.curr_data = curr_data

    def player_coefficient(self):
        player_coefficient_dict = {}
        for name, points in self.curr_data.items():
            player_coefficient_dict[name] = sum(points) / len(points)
        return player_coefficient_dict

    def best_ratio(self):
        return list(sorted(self.player_coefficient().items(), key=lambda item: -item[1]))[0]

data = {"Иван":[10,20,30],"Мария":[40,50,60],"Петър":[20,20]}

video = VideoGameStatistics(data)
print(video.best_ratio())

# Очакван изход: ('Мария', 50.0)