# Създай клас Book със:
# обикновени атрибути title, author, pages
# метод __str__() – връща "Title by Author"
# метод __len__() – връща pages
# използвай getattr() и setattr() за промяна на заглавието
# Примерен вход:
# b = Book("Clean Code", "Robert C. Martin", 464)
# print(str(b))      # Clean Code by Robert C. Martin
# print(len(b))      # 464
# setattr(b, "title", "Clean Architecture")
# print(getattr(b, "title"))  # Clean Architecture
#----------------------------------------------------------

class Book:
    def __init__(self, title = str, author = str, pages = int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"{self.title} by {self.author}" # str

    def __len__(self) -> int:
        return self.pages                       # int

# Употреба:
b = Book("Be Water My Friend", "Brus Lee", 272)

print(str(b))        # -> str: "Clean Code by Robert C. Martin"
print(len(b))        # -> int: 464

# променяме заглавието с setattr
setattr(b, "title", "Tao of Jeet Kune Do")   # None (функцията променя, но не връща стойност)

# С getattr достъпваме стойността
print(getattr(b, "title"))                  # -> str: "Clean Architecture"
