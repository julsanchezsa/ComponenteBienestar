import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config
from dotenv import dotenv_values, load_dotenv
# print(config('DB_USER'))

load_dotenv()


#Database os.configuration
DB_DIALECT = config("DB_DIALECT")
DB_USER = config("DB_USER")
DB_PASS = config("DB_PASS")
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT")
DB_SCHEMA = config("DB_SCHEMA")

SQLALCHEMY_DATABASE_URL = f"{DB_DIALECT}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_SCHEMA}"

# DB_URL = os.getenv('POSTGRESS_URL')

# SQLALCHEMY_DATABASE_URL = DB_URL


engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SessionLocal = SessionLocal()

Base = declarative_base()

