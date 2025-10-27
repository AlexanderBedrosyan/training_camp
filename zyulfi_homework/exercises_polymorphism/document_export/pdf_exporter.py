# PDFExporter: връща "Exporting {content} to PDF"
from exercises_polymorphism.document_export.document import DocumentExporter


class PDFExporter(DocumentExporter):
    def export(self, content):
        return f"Exporting {content} to PDF"

    