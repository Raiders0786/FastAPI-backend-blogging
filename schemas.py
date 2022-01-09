from typing import List
from pydantic import BaseModel

from db.models import DbArticle

#just to display the Article details once the user calls 
class Article(BaseModel):
    title: str
    content: str
    published : bool
    class Config():
        orm_mode=True

#User Inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str
    class Config():
        orm_mode=True
   
class UserBase(BaseModel):
    username: str
    email: str
    password : str

# to display the email & username without password , we need to convert the database model into the other display model
# which can be done automatically using orm_mode=True in Config() class as follow below.

class DisplayUser(BaseModel):
    username: str
    email: str
    items: List[Article] = []
    class Config():
        orm_mode=True 

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int

class DisplayArticle(BaseModel):
    title: str
    content: str
    published: bool
    user: User
    class Config():
        orm_mode=True

class DbArticleNew(BaseModel):
    title: str
    content: str
    published: bool
    user: User
    class Config():
        orm_mode=True


class addDisplay(BaseModel):
    data: DbArticleNew
    current_user: User
    class Config():
        orm_mode=True