# клас PrintableMixin
# PrintableMixin` съдържа метод `print_info()`, който ще се използва по-късно.
#`PrintableMixin`: метод `print_info()` → извежда `get_info()` на конзолата.

class PrintableMixin:
    def print_info(self):
        print(self.get_info())
