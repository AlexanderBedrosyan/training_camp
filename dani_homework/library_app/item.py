# `Item` е базов клас с protected атрибут `_title`.

class Item:
    library_name = "City Library"

    def __init__(self, title, year):
        self._title = title
        self.year = year

    def get_info(self):
        pass

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value == "":
            raise ValueError("Title cannot be an empty string")
        self._title = value