# 🔹 Задача 1
# Създай клас Book с атрибути title и author. Добави метод get_info(), който връща:
# "{title} by {author}". Създай обект и извикай метода.

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"{self.title} by {self.author}"

book = Book("Na iztok ot raya", "Stainbek")
print(book.get_info())