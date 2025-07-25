# Създай клас Book, който има атрибути title и author.
# Създай обект и принтирай двете стойности.

class Book:
    def __init__(self, title, author):
        self.title = title  # атрибут заглавие
        self.author = author    # атрибут автор

    def print_book(self):
        print(f" Title: {self.title}, author: {self.author}")

# Създаване на обекти
book1 = Book('"Абатството Нортангър"', "Джейн Остин")
book2 = Book('"Анна Каренина"', "Лев Толстой")
book3 = Book('"Алената буква"', "Натаниъл Хоторн")

book1.print_book()  #
book2.print_book()  #
book3.print_book()  #