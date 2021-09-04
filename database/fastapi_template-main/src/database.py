import os
from os.path import dirname, join

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


user_name = os.environ.get('DB_USER_NAME')
password = os.environ.get('DB_PASSWORD')
host = os.environ.get('DB_HOST')
database_name = os.environ.get('DB_NAME')

DATABASE = f'mysql+mysqlconnector://{user_name}:{password}@{host}/{database_name}?charset=utf8'

ENGINE = create_engine(
    DATABASE,
    encoding='utf-8',
    echo=True
)

session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
)

Base = declarative_base()
Base.query = session.query_property()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()