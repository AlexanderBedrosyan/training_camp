# ЗАДАЧА 6: Каталог с книги и оценки
# ---------------------------------------------------------------
# История:
# Онлайн библиотека събира оценки на книги. Трябва да се покажат
# само най-добрите книги.
#
# ratings = {"Dune":[5,5,4,5],"1984":[4,3],"It":[5,5,5,5,5]} print(top_books(ratings, 3))
#

# class BookCatalog:
#     def __init__(self, curr_ratings):
#         self.curr_ratings = curr_ratings
#
#     def book_ratings(self):
#         book_ratings_dict = {}
#         for name, grades in self.curr_ratings.items():
#             book_ratings_dict[name] = sum(grades) / len(grades)
#         return book_ratings_dict
#
#     def best_book(self):
#         return dict(sorted(self.book_ratings().items(), key=lambda item: -item[1]))
#
#     def top_books(self, num_book):
#         new_dict = {}
#         for name, grades in self.best_book().items():
#             if len(new_dict) < num_book:
#                 new_dict[name] = grades
#         return new_dict


class BookCatalog:
    def __init__(self, curr_ratings):
        self.curr_ratings = curr_ratings

    def top_books(self, curr_rating):
        ratings_dict = {}
        for name, grades in self.curr_ratings.items():
            if len(grades) >= curr_rating:
                ratings_dict[name] = round(sum(grades) / len(grades), 2)
        return ratings_dict

    def sorted_book(self, curr_rating):
        return dict(list(sorted(self.top_books(curr_rating).items(), key=lambda item: -item[1]))[0:2])



ratings = {"Dune":[5,5,4,5],"1984":[4,3,0],"It":[5,5,5,5,5]}

book = BookCatalog(ratings)
# print(book.book_ratings())
# print(book.best_book())
print(book.top_books(3))
print(book.sorted_book(3))

# print(top_books(ratings, 3))

# Очакван изход: {'Dune': 4.75, 'It': 5.0}