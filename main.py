from os import name
from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from fastapi.responses import PlainTextResponse
from db.database import engine
from exceptions import StoryException
from router import get_blogs , post_blogs ,user ,articles,product,file
from db import models
from fastapi.middleware.cors import CORSMiddleware
from auth import authentication
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.include_router(get_blogs.router )
app.include_router(file.router)
app.include_router( post_blogs.router)
app.include_router(user.router)
app.include_router(articles.router)
app.include_router(product.router)
app.include_router(authentication.router)
#path parameters
@app.get('/')
def index():
    return {'message':'Hello World !'}

# handling Execptions
@app.exception_handler(StoryException)
def story_exception_handler(request: Request , exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail': exc.name}
    )

#HTTP Exception Response handler
@app.exception_handler(HTTPException)
def custom_handler(request: Request , exc: StoryException):
    return PlainTextResponse(str(exc),status_code=400)
    
#creating the database
models.Base.metadata.create_all(engine)

# allowing CORS Request to the API
#we can add as many of the origins we want to be allowed, we are allowing this for our reactjs frontend app
origins = [ 'http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods =["*"] ,
    allow_headers = ['*']
)

#making files static available 
app.mount('/file',StaticFiles(directory='file'),name='file')

