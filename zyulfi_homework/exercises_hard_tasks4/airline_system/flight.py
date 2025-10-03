# Flight
# Атрибути: code, capacity, private __booked
# Методи: book_passenger(p), is_full()

class Flight:
    def __init__(self, code=str, capacity=int):
        self.code = code
        self.capacity = capacity
        self.__booked = []

    def book_passenger(self, curr_passenger):
        if not self.is_full():
           self.__booked.append(curr_passenger)

    def is_full(self) -> bool:
        if len(self.__booked) == self.capacity:
            return True
        return False

    def get_book(self) -> list:
        return self.__booked

    def amount_passenger(self) -> int:
        return len(self.__booked)


