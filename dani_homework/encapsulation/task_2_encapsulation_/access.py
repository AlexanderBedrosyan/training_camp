# Клас AdminMixin с метод reset_password(obj,
# new_pw), който използва name mangling за достъп
# Създай клас Admin(User, AdminMixin)

from user import User

class AdminMixin:
    def reset_password(self, obj, new_password):
        obj._User__password = new_password

class Admin(User, AdminMixin):


    pass