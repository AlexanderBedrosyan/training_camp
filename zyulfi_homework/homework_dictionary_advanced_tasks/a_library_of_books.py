#  Задача 10: Библиотека от книги

# library = {
#     "1984": {"author": "Orwell", "pages": 328},
#     "Dune": {"author": "Herbert", "pages": 412},
#     "It": {"author": "King", "pages": 1138}
# }
# Изисквания:
# Изчисли средния брой страници.
# Изведи книгата с най-много страници.
# Създай речник само с книги над средния брой страници.

class Library:
    def __init__(self, curr_library):
        self.curr_library = curr_library

    def average_pages(self):
        average = 0
        for pages in self.curr_library.values():
            average += list(pages.values())[1]
        return average / len(self.curr_library)

    def most_pages(self):
        book_most_pages = None
        most_pages = 0
        for key_library, value_library in self.curr_library.items():
            if most_pages <= list(value_library.values())[1]:
                most_pages = list(value_library.values())[1]
                book_most_pages = key_library
        return book_most_pages

    def an_above_average_book(self):
        new_dict = {}
        for key_library, value_library in self.curr_library.items():
            if list(value_library.values())[1] >= self.average_pages():
                new_dict[key_library] = value_library
        return new_dict

library = {
    "1984": {"author": "Orwell", "pages": 328},
    "Dune": {"author": "Herbert", "pages": 412},
    "It": {"author": "King", "pages": 1138}
}

lib = Library(library)
print(lib.average_pages())
print(lib.most_pages())
print(lib.an_above_average_book())