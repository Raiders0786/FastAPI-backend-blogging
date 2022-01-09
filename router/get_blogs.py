from fastapi import APIRouter, status , Response
from enum import Enum
from typing import Optional

from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND


router= APIRouter(prefix='/blog', tags=['/blog'])

@router.get('/all')
def get_all_blogs():
    return {'message' : "All Blogs"}

# Predefined parameters
class BlogType(str,Enum):
    story= 'story'
    howto = 'howto'
    short= 'short'

@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {'message' : f'Blog type is {type}'}


@router.get('/{id}')
def get_blog(id: int):
    return {'message' : f'Blog with id {id}'}

# Query parameter  ---> Default & Optional Parameters
@router.get('/')
def get_all_blogs( page =1 , page_size: Optional[int]= None):
    return {'message' : f'{page_size} number of pages at page {page}'}

# Query + Path parameters to obtain the comment from a blog post 
# Status Code Added too

@router.get('/{id}/comments/{comment_id}' , status_code= status.HTTP_200_OK , tags=['comment'])
def get_comments(id: int, response : Response , comment_id: int , valid: bool = True , username : Optional[str] = None):
    
    if(id>5):
        response.status_code=HTTP_404_NOT_FOUND
        return {'error' : 'Blog {id} Not Found'}
    else:
        response.status_code=HTTP_200_OK
        return {'Message' : f'Blog with Blog_id {id} , comment_id {comment_id} , Valid {valid} & Username {username}'}