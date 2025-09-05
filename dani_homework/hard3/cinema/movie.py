# Movie
# Атрибути: title, private __seats
# Методи: book_seat() (намалява броя на местата с 1, ако има)

class Movie:
    def __init__(self, title:str, seats:int):
        self.title = title
        self.__seats = seats

    def book_seat(self) -> bool:
        if self.__seats > 0:
            self.__seats -= 1
            return True
        return False

    def get_seats(self):
        return self.__seats

#test
m1=Movie("Mines", 4)
m1.book_seat()
print(f'For a movie {m1.title} are booked {m1.get_seats()} seats')