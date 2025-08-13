# 🔹 Задача 13
# Създай клас LibraryItem с атрибути title и year.
# Създай класове Book и Magazine, които наследяват LibraryItem.
# Book има атрибут author, а Magazine – issue_number.
# Създай клас DigitalMagazine, наследяващ Magazine, с метод download() връщащ "Downloading {title} issue {issue_number}".

class LibraryItem:

    def __init__(self, title=str, year=int):
        self.title = title
        self.year = year

class Book(LibraryItem):
    def __init__(self, title=str, year=int, author=str):
        super().__init__(title, year)
        self.author = author

class Magazine(LibraryItem):
    def __init__(self, title=str, year=int, issue_number=int):
        super().__init__(title, year)
        self.issue_number = issue_number

class DigitalMagazine(Magazine):

    def download(self) -> str:
        return f"Downloading {self.title} issue {self.issue_number}"

digital_magazine = DigitalMagazine("Rolling Stone", 1996, 1926)
print(digital_magazine.download())

book = Book("Harry Potter", 2006, "Georgi")
print(book.title)
print(book.year)
print(book.author)