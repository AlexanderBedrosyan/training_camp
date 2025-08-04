# Създай клас Vault със secret code, който е private.
# Напиши метод __verify(code), който връща True ако кодът е верен.
# Извикай метода чрез name mangling.
# ------------------------------------------------------------

class Vault:
    def __init__(self, secret_code):
        self.__secret_code = secret_code    # private атрибут

    def __verify(self, code):               # private метод
        return code == self.__secret_code


# инстанция на класа
vault = Vault("1234")

# викаме __verify чрез name mangling; преобразуваме името в _ИмеНаКласа__ИмеНаМетода
result = vault._Vault__verify("1234")

print("Достъп позволен:" if result else "Грешен код.")
