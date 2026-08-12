import uuid
from qdrant_client.models import PointStruct
from app.schemas.chunk import DocumentChunk


class DocumentIndexer:

    def __init__(
        self,
        parser,
        chunker,
        embedding_service,
        qdrant_service,
    ):
        self.parser = parser
        self.chunker = chunker
        self.embedding_service = embedding_service
        self.qdrant_service = qdrant_service

    def index(
        self,
        document_id: int,
        version: int,
        file_path: str,
        filename: str,
    ) -> int:

        pages = self.parser.extract_pages(
            file_path
        )

        print(f"Extracted {len(pages)} pages from {filename}")

        chunks: list[DocumentChunk] = []

        chunk_index = 0

        for page in pages:
            page_chunks = self.chunker.split(
                page["text"]
            )
            for chunk_text in page_chunks:
                chunks.append(
                    DocumentChunk(
                        text=chunk_text,
                        page=page["page"],
                        chunk_index=chunk_index,
                    )
                )
                chunk_index += 1
        if not chunks:
            return 0

        BATCH_SIZE = 100
        total_indexed = 0

        for start in range(
            0,
            len(chunks),
            BATCH_SIZE,
        ):

            batch = chunks[
                start:start + BATCH_SIZE
            ]

            texts = [
                chunk.text
                for chunk in batch
            ]

            embeddings = (
                self.embedding_service
                .embed_documents(texts)
            )

            points = []

            if len(chunks) != len(embeddings):
                raise RuntimeError(
                    "Chunk and embedding count mismatch"
                )

            for chunk, embedding in zip(
                chunks,
                embeddings,
            ):
                chunk_id = str(
                    uuid.uuid5(
                        uuid.NAMESPACE_URL,
                        (
                            f"{document_id}:"
                            f"{version}:"
                            f"{chunk.chunk_index}"
                        ),
                    )
                )

                points.append(
                    PointStruct(
                        id=chunk_id,
                        vector=embedding,
                        payload={
                            "document_id": document_id,
                            "version": version,
                            "filename": filename,
                            "page": chunk.page,
                            "chunk_index": chunk.chunk_index,
                            "text": chunk.text,
                        },
                    )
                )

            self.qdrant_service.upsert_points(
                points
            )

            total_indexed += len(points)

        return total_indexed
