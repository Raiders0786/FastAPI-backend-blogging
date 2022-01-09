from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
# from sqlalchemy.sql.functions import percent_rank
from sqlalchemy.sql.sqltypes import Boolean, Integer,String

from db.database import Base

class DbUser(Base):
    __tablename__= 'users'
    id=Column(Integer, primary_key=True,index=True)
    username=Column(String)
    email= Column(String)
    password= Column(String)
    items=relationship("DbArticle",back_populates='user')

class DbArticle(Base):
    __tablename__ = 'articles'
    id=Column(Integer, primary_key=True,index=True)
    title= Column(String)
    content = Column(String)
    published = Column(Boolean)
    user_id=Column(Integer, ForeignKey('users.id'))
    user=relationship("DbUser",back_populates='items')