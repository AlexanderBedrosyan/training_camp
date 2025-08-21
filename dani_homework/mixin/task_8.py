# Създай Mixin WriteMixin с метод write() връщащ "Writing...".
# Създай клас Author, който използва този миксин и има атрибут books.
# Тествай метода write() за Author
# ----------------------------------------------------------------

class WriteMixin:
    def write(self):
        return "Writing ..."

class Author(WriteMixin):
    def __init__(self, books):
        self.books = books


author = Author("")
print(author.write())