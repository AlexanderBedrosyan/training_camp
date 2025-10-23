# WordExporter: връща "Exporting {content} to Word"
from exercises_polymorphism.document_export.document import DocumentExporter


class WordExporter(DocumentExporter):
    def export(self, content):
        return f"Exporting {content} to Word"