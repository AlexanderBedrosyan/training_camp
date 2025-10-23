# Astronaut
# Атрибути: name, private __hours
# Методи: add_hours(), get_hours()

class Astronaut:
    def __init__(self, name=str):
        self.name = name
        self.__hours = 0

    def add_hours(self, hours=float or int) -> None:
        self.__hours += hours

    def get_hours(self) -> float:
        return self.__hours