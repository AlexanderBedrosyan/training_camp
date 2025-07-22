# Задача 2
# Създай клас Book, който има атрибути title и author. Създай обект и принтирай двете стойности.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

current_book = Book("Harry Potter", "Joanne Rowling")

print(f"The book is {current_book.title} whit author {current_book.author}")
