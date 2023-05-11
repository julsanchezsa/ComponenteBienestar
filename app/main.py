from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from models.publication import Publication
from middlewares.error_handler import ErrorHandler
from routers.publications import publication_router


app = FastAPI()
app.title = "Componente Bienestar"

app.add_middleware(ErrorHandler)
app.include_router(publication_router, prefix="/api/bienestar")

Base.metadata.create_all(bind=engine)

