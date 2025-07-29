# Задача 2
# Създай клас User с private метод __display(), който принтира "Hello". Извикай метода чрез name mangling.

class User:
    def __display(self) -> None:
        print("Hello")

current_user = User()

current_user._User__display()