#
# ## 📌 Задача 1: Library System
#
# **Структура:**
# library_system/
# ├── book.py
# ├── member.py
# ├── borrow_mixin.py
# ├── library_system.py
# └── main.py
#
# markdown
# Always show details
#
# Copy code
#
# **Описание:**
#
# - **Book**
#   - Атрибути: `title`, `author`, private `__available=True`
#   - Методи: `is_available()`, `set_unavailable()`, `set_available()`
#
# - **BorrowMixin**
#   - Методи: `borrow(book)`, `return_book(book)`
#
# - **Member (BorrowMixin)**
#   - Атрибути: `name`, private `__borrowed_books`
#   - Методи: `list_books()`
#
# - **Library**
#   - Атрибути: private `__books`
#   - Методи: `add_book()`, `available_books()`, `find_book(title)`
#
# **main.py**
# ```python
# from book import Book
# from member import Member
# from library_system import Library
#
# b1 = Book("1984", "George Orwell")
# b2 = Book("Dune", "Frank Herbert")
#
# lib = Library()
# lib.add_book(b1); lib.add_book(b2)
#
# m = Member("Ivan")
# m.borrow(b1)
# print([book.title for book in m.list_books()])  # ['1984']
# print([book.title for book in lib.available_books()])  # ['Dune']
# m.return_book(b1)
# print(b1.is_available())  # True
# ```