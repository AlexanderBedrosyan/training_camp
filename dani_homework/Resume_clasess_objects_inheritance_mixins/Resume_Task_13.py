# Създай клас LibraryItem с атрибути title и year.
# Създай класове Book и Magazine, които наследяват LibraryItem.
# Book има атрибут author, а Magazine – issue_number.
# Създай клас DigitalMagazine, наследяващ Magazine,
# с метод download() връщащ "Downloading {title} issue {issue_number}".
# --------------------------------------------------------------------

class LibraryItem:
    def __init__(self, title, year):
        self.title = title
        self.year = year

class Book(LibraryItem):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

class Magazine(LibraryItem):
    def __init__(self, title, year, issue_id):
        super().__init__(title, year)
        self.issue_id = issue_id

class DigitalMagazine(Magazine):
    def download(self):
        return f'Downloading "{self.title}", year:{self.year}, issue: {self.issue_id}'

dm = DigitalMagazine("Perfect Magazine", 2025, 777777 )
print(dm.download())

