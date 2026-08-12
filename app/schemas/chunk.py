from dataclasses import dataclass


@dataclass
class DocumentChunk:

    text: str
    page: int
    chunk_index: int