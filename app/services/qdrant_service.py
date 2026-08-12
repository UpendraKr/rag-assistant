from qdrant_client.models import PointStruct

from app.core.config import settings
from app.db.qdrant import client


class QdrantService:

    def __init__(self):
        self.client = client
        self.collection_name = settings.QDRANT_COLLECTION

    def upsert_points(
        self,
        points: list[PointStruct],
    ) -> None:

        if not points:
            return

        self.client.upsert(
            collection_name=self.collection_name,
            points=points,
            wait=True,
        )

    def search(
        self,
        vector: list[float],
        limit: int = 5,
        query_filter=None,
    ):

        return self.client.query_points(
            collection_name=self.collection_name,
            query=vector,
            query_filter=query_filter,
            limit=limit,
        ).points

    def delete_by_document(
        self,
        document_id: int,
    ) -> None:

        self.client.delete(
            collection_name=self.collection_name,
            points_selector={
                "filter": {
                    "must": [
                        {
                            "key": "document_id",
                            "match": {
                                "value": document_id
                            }
                        }
                    ]
                }
            },
            wait=True,
        )