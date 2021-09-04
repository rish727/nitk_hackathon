from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.dialects.mysql import TINYINT as Tinyint
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.sqltypes import BLOB

from src.database import Base

from sqlalchemy.orm import relationship


class Informations(Base):
    __tablename__ = 'informations'
    
    name = Column(String(32), primary_key=True)
    date = Column(Integer, index=True)
    information = Column(String(512), unique=False, index=True)
    url = Column(String(255), primary_key=True, unique=True)
    
