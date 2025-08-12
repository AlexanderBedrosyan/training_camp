# access.py:
# Клас AdminMixin с метод reset_password(obj, new_pw), който използва name mangling за достъп.

class AdminMixin:
    def __init__(self, obj, new_pw):
