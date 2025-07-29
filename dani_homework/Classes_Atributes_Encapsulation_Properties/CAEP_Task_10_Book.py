# Създай клас Book със:
#
# обикновени атрибути title, author, pages
# метод __str__() – връща "Title by Author"
# метод __len__() – връща pages
# използвай getattr() и setattr() за промяна на заглавието
# Примерен вход:
#
# b = Book("Clean Code", "Robert C. Martin", 464)
# print(str(b))      # Clean Code by Robert C. Martin
# print(len(b))      # 464
# setattr(b, "title", "Clean Architecture")
# print(getattr(b, "title"))  # Clean Architecture
#----------------------------------------------------------