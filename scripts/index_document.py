from app.services.factory import get_document_indexer

indexer = get_document_indexer()

count = indexer.index(
    document_id=1,
    version=1,
    file_path="data/LPU.pdf",
    filename="lpu.pdf",
)

print(f"Indexed {count} chunks")