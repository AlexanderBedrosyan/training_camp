# `Item` е базов клас с protected атрибут `_title`.
#I tem`: атрибути `_title`, `_year` + метод `get_info()`.
#•	Направи title property (getter/setter) в Item:
# o	Ако за title е подадено празно място, то да връща грешка:
# „Title cannot be an empty string”
# o	Ако не е празно място, то да си закача атрибута.
# •	Добави class атрибут library_name = "City Library" в Item


class Item:
    library_name = "City Library"

    def __init__(self, title, year):
        self._title = title
        self._year = year

    def get_info(self):
        return f"{self._title} ({self._year})"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value == "":
            raise ValueError("Title cannot be an empty string")
        else:
            self._title = value

