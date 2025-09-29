# Movie
# Атрибути: title, private __ratings
# Методи: add_rating(), average_rating()

class Movie:
    def __init__(self, title=str):
        self.title = title
        self.__ratings = []

    def add_rating(self, curr_rating=float or int) -> None:
        self.__ratings.append(curr_rating)

    def average_rating(self) -> float:
        return sum([curr_rating for curr_rating in self.__ratings]) / len(self.__ratings)

