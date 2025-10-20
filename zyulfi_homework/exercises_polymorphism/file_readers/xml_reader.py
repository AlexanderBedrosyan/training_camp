# XMLReader: връща "Reading XML file {file}"
from exercises_polymorphism.file_readers.reader import Reader


class XMLReader(Reader):
    def read(self, file):
        return f"Reading XML file {file}"