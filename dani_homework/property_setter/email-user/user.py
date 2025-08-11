# Клас User с:
# атрибут email
# @setter за валидация – съдържа ли '@', иначе грешка

class User:
    def __init__(self, email=str):
        self.email = email

    @property
    def email(self):
        return self._email  # protected !!! else cycle/recurs

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("This is not email")
        self._email = value   # protected !!!
