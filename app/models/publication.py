from config.database import Base
from sqlalchemy import Column, String, Text, TIMESTAMP

class Publication(Base):
    __tablename__ = 'publications'
    publication_id = Column(String(50), primary_key=True,
                    unique=True, nullable=False)
    title = Column(String(50), nullable=False)
    author_publication = Column(String(50), nullable=False)
    content_publication = Column(Text(), nullable=False)
    publication_date = Column(TIMESTAMP(timezone=True), nullable=False)
    image = Column(String(100))