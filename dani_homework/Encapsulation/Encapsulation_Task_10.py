# Създай клас Session с __token (private),
# и методи get_token() и __refresh_token().
# Извикай метода чрез name mangling и демонстрирай капсулация
# ------------------------------------------------------------

import uuid

"""
стандартния модул uuid, позволява създаване на UUID стойности
    uuid.uuid4() – създава напълно случаен UUID (версия 4)
    uuid.uuid1() – базиран на текущо време + хардуерен адрес (MAC)
    uuid.uuid3() и uuid.uuid5() – базирани на хеш от име и namespace
"""

class Session:
    def __init__(self) -> None:
        self.__token: str = self.__generate_token()  # private атрибут

    def get_token(self) -> str:
        """Връща текущия токен (public метод)"""
        return self.__token

    def __refresh_token(self) -> str:
        """Генерира и записва нов токен (private метод)"""
        self.__token = self.__generate_token()
        return self.__token

    def __generate_token(self) -> str:
        """Генерира случаен UUID токен (private помощен метод)"""
        return str(uuid.uuid4())


# инициализираме сесия
s = Session()

# капсулация: get_token() е публичен
print("Текущ токен:", s.get_token())  # -> str

# __token и __refresh_token са частни:
# Следното би дало грешка: s.__refresh_token()

# викаме __refresh_token чрез name mangling:
new_token = s._Session__refresh_token()  # -> str

print("Нов токен:", new_token)
print("Проверка чрез get_token():", s.get_token())
