from sqlalchemy.orm import Session
from app.models.document import Document


class DocumentRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, document: Document):
        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)
        return document

    def get(self, document_id: int):
        return self.db.get(Document, document_id)

    def list(self):
        return self.db.query(Document).all()