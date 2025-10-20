# Задача 12: Търсене на книги по ключова дума
# Условие:
# find_book(library, keyword) приема library = {заглавие: автор} и връща списък от заглавия,
# които съдържат keyword (case-insensitive).

def find_book(library, keyword):
    list_of_title = []
    for title in library.keys():
        if keyword in title:
            list_of_title.append(title)
    return list_of_title


library = {"Python Basics":"John", "Learning C":"Anna", "Advanced Python":"Maria"}
print(find_book(library, "Python"))

# Очакван изход:
# ['Python Basics', 'Advanced Python']