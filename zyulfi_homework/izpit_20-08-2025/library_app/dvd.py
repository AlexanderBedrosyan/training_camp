# клас DVD, наследява Item
#`DVD`: добави private атрибут `__duration`.

#•	Добави property duration за DVD, което приема само положителни числа:
# o	Ако числото на duration не е продължително да връща грешка:
# „Duration cannot be less than or equal to zero”
# o	Ако не е отрицателно или 0, то да закача атрибута.


from item import Item
from mixins import PrintableMixin

class DVD(Item):
    def __init__(self, title, year, duration):
        super().__init__(title, year)
        self.__duration = duration

    def print_info(self):
        print(f"DVD: {self.get_info()}, duration: {self.__duration}")

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if value <= 0:
            raise ValueError("Duration cannot be less than or equal to zero")
        else:
            self.__duration = value