# Създай клас Safe, който съдържа:
# private атрибут __code – задава се при създаване
# метод unlock(code) – отпечатва "Unlocked" само ако кодът е верен
#
# Примерен вход:
# s = Safe("9876")
# s.unlock("1234")  # Nothing
# s.unlock("9876")  # Unlocked
#----------------------------------------------------------------------

class Safe:
    def __init__(self, code = str):
        self.__code = code  # частен  атрибут

    def unlock(self, code = str) -> None:
        """Отпечатва 'Unlocked', ако въведеният код съвпада с вътрешния."""
        if code == self.__code:
            print("Unlocked")

# Употреба:
s = Safe("9876")
s.unlock("1234")  # Нищо не се отпечатва
s.unlock("9876")  # Отпечатва: Unlocked
