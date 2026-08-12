from app.services.chunking import ChunkingService
from app.services.document_indexer import DocumentIndexer
from app.services.document_parser import PDFParser
from app.services.embeddings import get_embedding_service
from app.services.qdrant_service import QdrantService


def get_document_indexer():

    return DocumentIndexer(
        parser=PDFParser(),
        chunker=ChunkingService(),
        embedding_service=get_embedding_service(),
        qdrant_service=QdrantService(),
    )