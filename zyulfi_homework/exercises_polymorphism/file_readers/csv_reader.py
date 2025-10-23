# CSVReader: връща "Reading CSV file {file}"
from exercises_polymorphism.file_readers.reader import Reader


class CSVReader(Reader):
    def read(self, file):
        return f"Reading CSV file {file}"