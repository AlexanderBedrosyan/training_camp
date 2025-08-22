# Създай клас Book с атрибути title и author.
# Добави метод get_info(), който връща: "{title} by {author}".
# Създай обект и извикай метода.
# -----------------------------------------------------

class Book:
    def __init__(self, title: str, author: str)->None:
        self.title: str = title
        self.author: str = author

    def get_info(self)-> str:
        return f"'{self.title}' by {self.author}"


b1 = Book("Малкия принц", "Антоан дьо Сент-Екзюпери") #създава обект
print(b1.get_info())                                             # ринтира резултата от извикания метод

