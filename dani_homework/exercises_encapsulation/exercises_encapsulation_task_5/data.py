# Клас DataObject със:
# private атрибут __data
# метод get(key)

from json_helper import JsonMixin

class DataObject(JsonMixin):
    def __init__(self, data):
        self.data = data

    def get(self, key):
        return self.data[f"{key}"]

