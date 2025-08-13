# Създай клас с: private атрибут __seconds
# @property minutes – връща времето в минути
# @minutes.setter – приема минути и преизчислява __seconds
# Примерен вход:
# t = Timer()
# t.minutes = 2
# print(t.minutes)  # 2
# print(t._Timer__seconds)  # 120
#--------------------------------------------------------------

class Timer:
    def __init__(self) -> None:
        self.__seconds: int = 0     # частен атрибут

    @property
    def minutes(self) -> int:
        """Връща минутите на базата на __seconds"""
        return self.__seconds // 60     # -> int

    @minutes.setter
    def minutes(self, mins = int) -> None:
        """Задава минути и преизчислява __seconds"""
        self.__seconds = mins * 60  # -> None


# Употреба:
t = Timer()
t.minutes = 7               # setter: приема int, връща None

print(t.minutes)            # -> int: 2
print(t._Timer__seconds)    # -> int: 120 (чрез name mangling)

