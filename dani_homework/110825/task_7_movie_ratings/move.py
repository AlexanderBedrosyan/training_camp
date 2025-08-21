# Movie: име, private __ratings (list от числа),
# методи add_rating(), average_rating()

class Movie:
    def __init__(self, name):
        self.name = name
        self.__ratings = []

    def add_rating(self, rating):
        if 0<= rating <= 10:
            self.__ratings.append(rating)
        else:
            print("Rating must be between 0 and 10.")

    def average_ratting(self, current_rating):
        if not self.__ratings:
            return 0
        return sum(self.__ratings) / len(self.__ratings)
