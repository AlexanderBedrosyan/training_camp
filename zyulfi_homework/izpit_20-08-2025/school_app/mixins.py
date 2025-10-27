# клас InfoMixin
# InfoMixin: метод show_info().
# InfoMixin: show_info() извиква get_info().
from person import Person

class InfoMixin:
    def show_info(self):
        print(self.get_info())



