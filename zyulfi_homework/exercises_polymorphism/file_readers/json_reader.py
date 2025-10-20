# JSONReader: връща "Reading JSON file {file}"
from exercises_polymorphism.file_readers.reader import Reader


class JSONReader(Reader):
    def read(self, file):
        return f"Reading JSON file {file}"