# Клас Employee с:
# protected атрибут _hours
# метод work(hours)

class Employee:
    def __init__(self, name):
        self.name = name
        self._hours = 0

    def work(self, hours):
        self._hours += hours

