from models.publication import Publication as PublicationsModel
from schemas.publication import Publication as PublicationsSchema
import uuid
from datetime import datetime

def generate_uuid():
    return uuid.uuid4().hex

class PublicationsService():

    def __init__(self, db):
        self.db = db

    def get_publications(self):
        result = self.db.query(PublicationsModel).all()
        return result
    
    def get_publications_id(self, id:str):
        result = self.db.query(PublicationsModel).filter(PublicationsModel.publication_id == id).first()
        return result

    def post_publications(self, publications: PublicationsSchema):
        new_publications = PublicationsModel(
            publication_id = generate_uuid(),
            title = publications.title,
            author_publication = publications.author_publication,
            content_publication = publications.content_publication,
            publication_date =  datetime.now(),
            image = publications.image
        )
        self.db.add(new_publications)
        self.db.commit()
        return

    def update_publications(self, id: str, publications: PublicationsSchema):
        publication = self.get_publications_id(id)
        publication.title = publications.title
        publication.content_publication = publications.content_publication + " (Editado) "
        publication.image = publications.image
        self.db.commit()
        return

    def delete_publications(self, id: str):
        self.db.query(PublicationsModel).filter(PublicationsModel.publication_id == id).delete()
        self.db.commit()
        return