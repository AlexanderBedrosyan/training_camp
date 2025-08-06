# Клас SecureData с:
# private атрибут __value
# метод access(password) – ако е вярна, връща стойността


class SecureData:
    def __init__(self, value, password):
        self.__value = value       # private атрибут
        self.__password = password  # също private (по желание)

    def access(self, password):
        if password == self.__password:
            return self.__value
        return None