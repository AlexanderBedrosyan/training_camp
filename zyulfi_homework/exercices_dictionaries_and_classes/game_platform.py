# Задача 9: Видео игрова платформа
# Създай клас GamePlatform, който следи игри и оценки.
# Условия:
# Речник {игра: {"ratings": [числа], "genre": жанр}}
# Метод add_rating(game, rating)
# Метод best_game() – връща играта с най-висока средна оценка.
# Метод average_genre(genre) – средна оценка за жанра.


class GamePlatform:
    def __init__(self):
        self.games_dict = {}

    def add_game(self, name, genre):
        if name not in self.games_dict:
            self.games_dict[name] = {
                "ratings": [],
                "genre": genre
            }

    def add_rating(self, name, rating):
        if name in self.games_dict:
            self.games_dict[name]["ratings"].append(rating)
        else:
            self.add_game(name, "random")
            self.add_rating(name, rating)

    def best_game(self):
        return sorted(self.games_dict.items(), key=lambda x: - sum(x[1]["ratings"])/len(x[1]["ratings"]))[0][0]

    def average_genre(self, genre):
        curr_counter = 0
        for curr_name_game, curr_data in self.games_dict.items():
            if genre == curr_data["genre"]:
                curr_counter += 1
        return round(curr_counter / len(self.games_dict), 2)

# Тест:
gp = GamePlatform()
gp.add_game("Zelda", "action")
gp.add_game("Mario", "drama")
gp.add_rating("Zelda", 10)
gp.add_rating("Zelda", 9)
gp.add_rating("Mario", 10)
gp.add_rating("Car", 8)
gp.add_game("ff", "action")
gp.add_rating("ff", 15)

print(gp.average_genre("action"))
print(gp.best_game())  # Zelda
print(gp.games_dict)