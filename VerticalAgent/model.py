import sqlalchemy as db 
from sqlalchemy import Column, Integer, String, JSON
from Meta.database.database import engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import session , sessionmaker


Base = declarative_base()



class businessdomain(Base):
    __tablename__ = "new_metadata"
    id = Column(Integer, primary_key=True, autoincrement=True)
    domain_name = Column(String)
    domain_description = Column(String)
    keywords = Column(String)
    confidence_score = Column(Integer)
    embiding = VectorType()
    


Base.metadata.create_all(engine)