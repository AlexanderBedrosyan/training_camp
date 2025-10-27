# Trip
# Атрибути: destination, price, private __booked=False
# Методи: book(), cancel(), is_booked()

class Trip:
    def __init__(self, destination=str, price=float):
        self.destination = destination
        self.price = price
        self.__booked = False

    def book(self) -> None:
        if not self.__booked:
            self.__booked = True

    def cancel(self) -> None:
        if self.__booked:
            self.__booked = False

    def is_booked(self) -> bool:
        return self.__booked