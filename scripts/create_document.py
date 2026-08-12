from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.document import Document


engine = create_engine(settings.DATABASE_URL)


with Session(engine) as session:

    document = Document(
        filename="lpu.pdf",
        file_path="data/LPU.pdf",
        status="UPLOADED",
        version=1,
    )

    session.add(document)
    session.commit()

    session.refresh(document)

    print("Document ID:", document.id)