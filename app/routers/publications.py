from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.publication import Publication
from config.database import Session
from services.publications import PublicationsService

publication_router = APIRouter()

@publication_router.get(
    path= '/publications',
    tags= ['Publications'],
    summary= "Get all publications"
    )
def get_all_publications():
    """
    Get all publications

    This path operation retrieves all publications from the database.

    Returns:
    - status_code 200: Successful operation
    - List[Publication]: List of Publication models
    """
    db = Session()
    result = PublicationsService(db).get_publications()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))   

@publication_router.get(
    path= '/publications/{id}',
    tags= ['Publications'],
    summary= "Get publication by ID"
    )
def get_publication_id(id: str):
    """
    Get publication by ID
    
    Retrieves a publication from the database by its ID.
    
    Parameters:
    - id (int): The unique identifier of the publication
    
    Returns:
    - Publication: The Publication model with the specified ID
    
    """
    db = Session()
    result = PublicationsService(db).get_publications_id(id)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))   


@publication_router.post(
    path= '/publications/new',
    tags= ['Publications'],
    summary= "Create a publication"
    )
def post_publication(publication: Publication):
    """
    Create publication

    This path operation creates a publication in the app and saves the information in the database
    
    Parameters:
    - Request Body parameter:
        - **publication: Publication** -> A publication model with the necessary fields
        
    Return a JSON response with status 201 and a message indicating the publication was created.
    """
    db = Session()
    PublicationsService(db).post_publications(publication)
    return JSONResponse(status_code=201, content={"message": "Se ha creado la publicacion"})

@publication_router.put(
    path='/publications/update/{id}',
    tags= ['Publications'],
    summary= "Update publication by id"
    )
def update_publication(id: str, publication: Publication):
    """
    Update publication by id
    
    This path operation updates a publication in the app by the provided id and saves the modified 
    information in the database.
    
    Parameters:
    - Path parameter:
        - **id: str** -> The id of the publication to be updated
    - Request Body parameter:
        - **publication: Publication** -> A publication model with the fields to be modified
    
    Returns a JSON response with status code 200 and a message indicating that the publication was updated.
    If the publication with the provided id is not found in the database, returns a JSON response with 
    status code 404 and a message indicating that the publication was not found.
    """
    db = Session()
    result = PublicationsService(db).get_publications_id(id)
    if not result:
       return JSONResponse(status_code=404, content={'message': "No se ha encontrado la publicacion"})

    PublicationsService(db).update_publications(id,publication)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la publicacion"})

@publication_router.delete(
    path='/publications/delete/{id}',
    tags= ['Publications'],
    summary= "Update publication by id"
    )
def delete_publication(id: str):
    """
    Delete publication

    This path operation deletes a publication in the app and removes the information from the database
    
    Parameters:
    - Path parameter:
        - **id: str** -> The id of the publication to be deleted
        
    Return a JSON response with status 200 and a message indicating the publication was deleted.
    If the publication does not exist, return a JSON response with status 404 and a message indicating that it was not found.
    """
    db = Session()
    result = PublicationsService(db).get_publications_id(id)
    if not result:
       return JSONResponse(status_code=404, content={'message': "No se ha encontrado la publicacion"})
    
    PublicationsService(db).delete_publications(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la publicacion"})