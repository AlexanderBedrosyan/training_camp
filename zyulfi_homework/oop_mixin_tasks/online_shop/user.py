# User
# Атрибути: username, private __cart
# Методи: get_cart()

from cart import Cart

class User:
    def __init__(self, username=str):
        self.username = username
        self.__cart = Cart()

    def add_cart(self, curr_cart) -> None:
        self.__cart = curr_cart

    def get_cart(self):
        return self.__cart

