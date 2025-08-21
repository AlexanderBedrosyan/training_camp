# User: private __password, метод check_password()

class User:
    def __init__(self, username=str, password=str)-> None:
        self.username = username
        self.__password = password


    def check_password(self, password=str)->bool:
        return self.__password == password


