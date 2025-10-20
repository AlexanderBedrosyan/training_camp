# User: private __password, метод check_password()

class User:
    def __init__(self, password):
        self.__password = password

    def check_password(self, current_password=str) -> bool:
        if current_password == self.__password:
            return True
        else:
            return False


