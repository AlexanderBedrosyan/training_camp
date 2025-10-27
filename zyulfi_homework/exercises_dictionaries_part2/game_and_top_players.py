# 🕹️ ЗАДАЧА 5: Игра и топ играчи
# ---------------------------------------------------------------
# История:
# Играчите събират точки. Трябва да покажеш топ 3 по общ резултат.
#data = {"Иван":[10,20,30],"Мария":[50,40],"Петър":[15,10,15],"Гошо":[60]} print(top_players(data))

class BestPlayer:
    def __init__(self, curr_data):
        self.curr_data = curr_data

    def sum_points(self):
        points_dict = {}
        for name, points in self.curr_data.items():
            points_dict[name] = sum(points)
        return points_dict

    def sorted_players(self):
        return dict(sorted(self.sum_points().items(), key=lambda item: -item[1]))

    def top_players(self):
        # new_list = []
        # for element in self.sorted_players().items():
        #     if len(new_list) <= 2:
        #         new_list.append(element)
        # return new_list
        return [element for element in self.sorted_players().items()][0:3]

data = {"Иван":[10,20,30],"Мария":[50,40],"Петър":[15,10,15],"Гошо":[60]}

pl = BestPlayer(data)
print(pl.top_players())

# Очакван изход: [('Мария',90),('Гошо',60),('Иван',60)]