# LibraryItem с атрибути title, _available и метод checkout(), return_item()

class LibraryItem:
    def __init__(self, title=str):
        self.title = title
        self._available = True

    def is_available(self):
        return self._available

    def checkout(self) -> None:
        if self._available:
            self._available = False
            print("This is Item is available.")
        else:
            print("This is Item is NOT available.")

    def return_item(self) -> None:
        if not self._available:
            self._available = True
            print("Thank you for returning the item on time.")
        else:
            print("Please return the item on time.")