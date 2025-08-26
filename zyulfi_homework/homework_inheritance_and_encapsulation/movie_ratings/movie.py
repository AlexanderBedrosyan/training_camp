# Атрибу ти: title, private __ratings (list от числа)
# Методи:
# add_rating(rating) → добавя оценка (1–10)
# average_rating() → връща средната оценка
# __str__() → "{title}, avg rating: {average}"

class Movie:
    def __init__(self, title=str):
        self.title = title
        self.__ratings = []

    def add_rating(self, rating=int) -> None:
        if 1 <= rating <= 10:
            self.__ratings.append(rating)
        else:
            print("Error")

    def average_rating(self) -> float:
        return sum(self.__ratings) / len(self.__ratings)

    def __str__(self) -> str:
        return f"{self.title}, avg rating: {self.average_rating()}"
