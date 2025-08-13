from data import DataObject

d = DataObject(
    {"name": "Anna", "Gargamel": 123}
)
print(d.get("name"))     # Anna
print(d.get("Gargamel"))     # Anna
print(d.to_json())       # {"name": "Anna"}