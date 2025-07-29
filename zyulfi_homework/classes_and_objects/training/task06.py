# Задача 6
# Създай клас Vault със secret code, който е private. Напиши метод __verify(code),
# който връща True ако кодът е верен. Извикай метода чрез name mangling.

class Vault:
    def __init__(self, secret_code=int):
        self.__secret_code = secret_code

    def __verify(self, code=int) -> bool:
        if self.__secret_code == code:
            return True
        return False

current_vault = Vault(1236)
current_code = int(input("Enter password:"))

print(current_vault._Vault__verify(current_code))



