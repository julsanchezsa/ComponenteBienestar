from pydantic import BaseModel
from datetime import datetime

class Publication(BaseModel):
    title: str
    content_publication: str
    author_publication: str
    publication_date: datetime
    image: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Titulo de prueba",
                "content_publication": "Texto de prueba",
                "author_publication": "21312312412",
                "publication_date": "2022-05-01T10:00:00.000Z",
                "image": "https://example.com/image.jpg"
            }
        }