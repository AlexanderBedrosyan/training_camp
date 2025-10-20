from pdf_exporter import PDFExporter
from word_exporter import WordExporter
from text_exporter import TextExporter

exporters = [PDFExporter(), WordExporter(), TextExporter()]
for e in exporters:
    print(e.export("Hello World"))