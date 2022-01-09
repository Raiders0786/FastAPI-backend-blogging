
from fastapi import APIRouter, Depends , HTTPException , status
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import DbArticle
from schemas import ArticleBase, DbArticleNew, DisplayArticle, addDisplay
from db import db_article
from auth.ouath2 import get_current_user
from schemas import UserBase

router=APIRouter(prefix='/article',tags=['article'])

@router.post('/', response_model=DisplayArticle)
def create_articles( request : ArticleBase ,db: Session = Depends(get_db)):
    return db_article.create_article(db,request)

@router.get('/{id}', response_model=addDisplay)#
def display_user_by_id(id: int ,db : Session = Depends(get_db) , current_user : UserBase = Depends(get_current_user)):
    if not current_user.username :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail='Pleae Validate from Ouath'
        )
    return {
        'data':db_article.get_all_articles( id , db ),
        'current_user': current_user
    }
    # return db_article.get_all_articles( id , db)