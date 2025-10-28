# Customer
# Атрибути: name, private __tickets
# Методи: book_movie(movie)
from movie import Movie


class Customer:
    def __init__(self, name:str):
        self.name = name
        self.__tickets = 0

    def book_movie(self, movie) -> bool:
        if movie.book_seat():
            self.__tickets += 1
            return True
        return False

    def get_tickets(self) -> int:
        return self.__tickets

#test
m5=Movie("ttt", 4)
c=Customer("Muncho")
print(c.book_movie(m5))


