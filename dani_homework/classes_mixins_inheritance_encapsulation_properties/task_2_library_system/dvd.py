# DVD има duration и метод is_long() (>120 минути)
from item import LibraryItem

class DVD(LibraryItem):
    TIME_LIMIT = 120
    def __init__(self, title=str, duration=int):
        super().__init__(title)
        self.duration = duration

    def is_long(self):
        return self.duration >= DVD.TIME_LIMIT

