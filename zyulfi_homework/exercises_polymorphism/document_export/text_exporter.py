# TextExporter: връща "Exporting {content} to TXT"
from exercises_polymorphism.document_export.document import DocumentExporter


class TextExporter(DocumentExporter):
    def export(self, content):
        return f"Exporting {content} to TXT"