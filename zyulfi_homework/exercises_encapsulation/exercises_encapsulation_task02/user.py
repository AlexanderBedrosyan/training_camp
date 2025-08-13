# Клас User с:
# private атрибут __password
# метод check_password(pw)

class User:
    def __init__(self, password):
        self.__password = password

    def check_password