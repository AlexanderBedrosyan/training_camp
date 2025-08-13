# storage.py:
# Клас Storage със:
# private атрибут __items (списък)
# метод add_item(item)
# @property items (само за четене)



class Storage:
    def __init__(self):
        self.__items = []  # private атрибут

    def add_item(self, item):
        self.__items.append(item)

    @property
    def items(self):
        return self.__items.copy()  # само за четене (връща копие)