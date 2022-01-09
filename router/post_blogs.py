from typing import Optional, List
from fastapi import APIRouter, Query 
from fastapi.param_functions import Body, Path
from pydantic import BaseModel
from pydantic.utils import all_identical

router = APIRouter(prefix='/blog' , tags=['blog'])

class Image(BaseModel):
    url: str 
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    nb_comment: int
    published: Optional[bool]
    tags: List[str] = None
    image: Optional[Image] = None

@router.post('/new/{id}')
def create_blog(blog: BlogModel , id: int , version : int =1):
    return {
        'id' : id,
        'data': blog,
        'version':version
        }

@router.post('/new/{id}/comment/{comment_id}')
def create_comment( blog: BlogModel ,id : int ,
        comment_title: str = Query(None , title='Title of Comment', description='Description of Comment_Title', 
        alias='commentTitle' ,deprecated=True ) , 
        content: str = Body(..., min_length=10 , max_length=30 , regex='^[a-z\s]*$') #making it mandatory by adding (... or Ellipsis)
        ,v: Optional[List[str]]= Query(['1.0','1.1','2.0']),
        comment_id: int = Path(None, gt=5 , le=10)
    ):
    return {'blog_id':id,'data' : blog,'metatdata':comment_title , 'content' : content,'version':v,'comment_id':comment_id}
