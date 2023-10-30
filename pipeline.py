#pipeline para extrair infos das páginas web do regimento do vestibular unicamp 2024
'''
Installing external dependencies

Todas essas dependências estão presentes em "requirements.txt"

'''

from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import PDFToTextConverter

def init_document_store(document):
    doc_store = InMemoryDocumentStore(use_bm25 = True)
    doc_store.write_documents(document)

    return doc_store


def convert_pdf_to_text(path: str):
    """
    returns a document
    """
    conversor = PDFToTextConverter()

    documento_text = conversor.convert(file_path = path)

    return documento_text
