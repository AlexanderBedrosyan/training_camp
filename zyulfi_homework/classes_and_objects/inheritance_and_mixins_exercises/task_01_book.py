# Задача 1
# Създай клас Book с атрибути title и author. Добави метод get_info(), който връща:
# "{title} by {author}". Създай обект и извикай метода.

class Book:
    def __init__(self, title=str, author=str):
        self.title = title
        self.author = author

    def get_info(self) -> str:
        return f"{self.title} by {self.author}"

current_book = Book("Harry Potter", "Joan Rowling")
current_book2 = Book("Война и мир", "Лев Толстой")

print(current_book.get_info())
print(current_book2.get_info())