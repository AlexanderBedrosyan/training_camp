from csv_reader import CSVReader
from json_reader import JSONReader
from xml_reader import XMLReader

files = [CSVReader(), JSONReader(), XMLReader()]
for f in files:
    print(f.read("data"))