from storage import Storage
from manager import RemoveMixin

class Inventory(Storage, RemoveMixin):
    pass

inv = Inventory()
inv.add_item("apple")
inv.add_item("banana")
inv.remove_item("apple")
print(inv.items)  # ['banana']