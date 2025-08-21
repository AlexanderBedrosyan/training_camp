from data import DataObject

d = DataObject({"name": "Anna"})
print(d.get("name"))     # Anna
print(d.to_json())       # {"name": "Anna"}