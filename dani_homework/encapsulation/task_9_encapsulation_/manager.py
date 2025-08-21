# Mixin RemoveMixin с метод remove_item(item)
# Създай Inventory(Storage, RemoveMixin)

class RemoveMixin:
    def remove_item(self, item):
        if item in self._Storage__items:
            self._Storage__items.remove(item)

