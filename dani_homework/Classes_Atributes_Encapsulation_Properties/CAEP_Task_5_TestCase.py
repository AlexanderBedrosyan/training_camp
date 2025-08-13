# Създай клас с:
# protected атрибут _name
# private атрибут __status (по подразбиране "Not Run")
# метод run() – променя __status на "Passed"
# @property за status
# Примерен вход:
# t = TestCase("Check sum")
# print(t.status)  # Not Run
# t.run()
# print(t.status)  # Passed
#--------------------------------------------------------

class TestCase:
    def __init__(self, name = str):
        self._name = name               # защитен атрибут
        self.__status = "Not Run"      # частен атрибут

    def run(self) -> None:
        """Променя състоянието на 'Passed'."""
        self.__status = "Passed"

    @property
    def status(self) -> str:
        """Връща текущото състояние."""
        return self.__status

# Употреба
t = TestCase("Check sum")
print(t.status)  # Not Run
t.run()
print(t.status)  # Passed
