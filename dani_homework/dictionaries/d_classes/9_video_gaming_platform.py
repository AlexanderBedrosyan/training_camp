# Създай клас GamePlatform, който следи игри и оценки.
# Условия: Речник {игра: {"ratings": [числа], "genre": жанр}}
# Метод add_rating(game, rating)
# Метод best_game() – връща играта с най-висока средна оценка.
# Метод average_genre(genre) – средна оценка за жанра.
class GamePlatform:
    def __init__(self):
        # Структура: {игра: {"ratings": [числа], "genre": жанр}}
        self.games = {}

    def add_game(self, name: str, genre: str):
# Добавя нова игра, ако я няма вече в системата.
        if name not in self.games:
            self.games[name] = {"ratings": [], "genre": genre}

    def add_rating(self, game: str, rating: float, genre: str = "Unknown"):
# Добавя оценка за игра; ако играта липсва, я създава с жанр.
        if rating < 0 or rating > 10:
            raise ValueError("Оценката трябва да е между 0 и 10.")
        if game not in self.games:
            self.add_game(game, genre)
        self.games[game]["ratings"].append(rating)

    def average_rating(self, game: str) -> float:
# Средна оценка за конкретна игра.
        data = self.games.get(game)
        if not data or not data["ratings"]:
            return 0.0
        return sum(data["ratings"]) / len(data["ratings"])

    def best_game(self) -> str:
# Връща името на играта с най-висока средна оценка.
        if not self.games:
            return None
        return max(self.games, key=lambda g: self.average_rating(g))

    def average_genre(self, genre: str) -> float:
# Изчислява средната оценка за всички игри от даден жанр.
        genre_ratings = [
            rating
            for g, data in self.games.items()
            if data["genre"] == genre
            for rating in data["ratings"]
        ]
        if not genre_ratings:
            return 0.0
        return sum(genre_ratings) / len(genre_ratings)

    def __str__(self):
        return f"GamePlatform({len(self.games)} games)"

# Тест:
gp = GamePlatform()
gp.add_rating("Zelda", 10)
gp.add_rating("Zelda", 9)
gp.add_rating("Mario", 8)
print(gp.best_game())  # Zelda
