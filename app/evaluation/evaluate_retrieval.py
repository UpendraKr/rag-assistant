import json

from app.services.embeddings import get_embedding_service
from app.services.qdrant_service import QdrantService
from app.services.retriever import Retriever


def recall_at_k(
    retrieved_ids,
    relevant_ids,
):

    retrieved = set(retrieved_ids)
    relevant = set(relevant_ids)

    if not relevant:
        return 0.0

    return len(
        retrieved & relevant
    ) / len(relevant)


def precision_at_k(
    retrieved_ids,
    relevant_ids,
):

    if not retrieved_ids:
        return 0.0

    retrieved = set(retrieved_ids)
    relevant = set(relevant_ids)

    return len(
        retrieved & relevant
    ) / len(retrieved)


def reciprocal_rank(
    retrieved_ids,
    relevant_ids,
):

    relevant = set(relevant_ids)

    for rank, chunk_id in enumerate(
        retrieved_ids,
        start=1,
    ):

        if chunk_id in relevant:
            return 1 / rank

    return 0.0