# Flight
# Атрибути: code, capacity, private __booked
# Методи: book_passenger(p), is_full()
class Flight:
    def __init__(self, code: str, capacity: int):
        self.code = code
        self.capacity = capacity
        self.__booked = []  # private списък от пътници

    def book_passenger(self, passenger) -> bool:
        # Добавя пътник, ако има свободни места. Връща True/False.
        if not self.is_full():
            self.__booked.append(passenger)
            return True
        return False

    def is_full(self) -> bool:
        # Проверява дали полетът е пълен.
        return len(self.__booked) >= self.capacity

    def num_passengers(self) -> int:
        # Брой резервирани пътници.
        return len(self.__booked)

    def __str__(self):
        return f"Flight({self.code}, {len(self.__booked)}/{self.capacity} booked)"





