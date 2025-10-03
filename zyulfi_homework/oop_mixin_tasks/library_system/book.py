# - **Book**
#   - Атрибути: `title`, `author`, private `__available=True`
#   - Методи: `is_available()`, `set_unavailable()`, `set_available()`

class Book:
    def __init__(self, title=str, author=str):
        self.title = title
        self.author = author
        self.__available = True

    def is_available(self) -> bool:
        return self.__available

    def set_unavailable(self) -> None:
        self.__available = False

    def set_available(self) -> None:
        self.__available = True