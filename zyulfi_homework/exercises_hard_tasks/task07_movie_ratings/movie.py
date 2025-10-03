# Movie: име, private __ratings (list от числа), методи add_rating(), average_rating()

class Movie:
    def __init__(self, name_movie):
        self.name = name_movie
        self.__ratings = []

    def add_rating(self, rating=float) -> None:
        self.__ratings.append(rating)

    def average_rating(self) -> float:
        return sum(self.__ratings) / len(self.__ratings)
