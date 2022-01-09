from fastapi import FastAPI , status , Response
from enum import Enum
from typing import Optional

from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

app = FastAPI()

#path parameters
@app.get('/' )
def index():
    return {'message':'Hello World !'}

@app.get('/blog/all' ,tags=['blog'])
def get_all_blogs():
    return {'message' : "All Blogs"}

# Predefined parameters
class BlogType(str,Enum):
    story= 'story'
    howto = 'howto'
    short= 'short'

@app.get('/blog/type/{type}',tags=['blog'])
def get_blog_type(type: BlogType):
    return {'message' : f'Blog type is {type}'}


@app.get('/blog/{id}',tags=['blog'])
def get_blog(id: int):
    return {'message' : f'Blog with id {id}'}

# Query parameter  ---> Default & Optional Parameters
@app.get('/blog',tags=['blog'])
def get_all_blogs( page =1 , page_size: Optional[int]= None):
    return {'message' : f'{page_size} number of pages at page {page}'}

# Query + Path parameters to obtain the comment from a blog post 
# Status Code Added too

@app.get('/blog/{id}/comments/{comment_id}' , status_code= status.HTTP_200_OK ,tags=['blog','comment'])
def get_comments(id: int, response : Response , comment_id: int , valid: bool = True , username : Optional[str] = None):
    
    if(id>5):
        response.status_code=HTTP_404_NOT_FOUND
        return {'error' : 'Blog {id} Not Found'}
    else:
        response.status_code=HTTP_200_OK
        return {'Message' : f'Blog with Blog_id {id} , comment_id {comment_id} , Valid {valid} & Username {username}'}