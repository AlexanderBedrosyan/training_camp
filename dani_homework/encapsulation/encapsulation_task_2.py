# Създай клас User с private метод __display(), който принтира "Hello".
# Извикай метода чрез name mangling.
# -----------------------------------------------------------------------

class User:
    def __display(self):
        print("Hello")      # не връща стойност, само отпечатва "Hello"

u = User()                  # Създаваме обект

# Викаме метод чрез name mangling
result = u._User__display()  # Това ще отпечата "Hello"

print(f'"Резултатът от извикването е:", {result}')
