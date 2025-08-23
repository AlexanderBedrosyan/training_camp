# LibraryItem с атрибути title,
# _available и метод checkout(),
# return_item()

class LibraryItem:
    def __init__(self, title=str):
        self.title = title
        self._available = True

    def is_available(self):
        return self._available

    def checkout(self):
        if self._available:
            self._available = False
            print(f"This item is available")
        else:
            print(f"This item is NOT available")

    def return_item(self):
        if not self._available:
            self._available = True
            print(f"Thank you for bring us back the item")
        else:
            print(f"You are late with")