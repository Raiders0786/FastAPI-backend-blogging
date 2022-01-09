from db.models import DbArticle
from exceptions import StoryException
from schemas import ArticleBase
from sqlalchemy.orm.session import Session
from fastapi import HTTPException , status , Depends
from auth.ouath2 import get_current_user, oauth2_scheme

def create_article(db: Session , request: ArticleBase):
    if request.content.startswith('Once Upon a Time'):
        raise StoryException('No Stories Plaease')
    new_article = DbArticle(
        title = request.title,
        content = request.content,
        published = request.published,
        user_id = request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

def get_all_articles(id: int , db: Session ):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    # handle Errors
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , 
        detail=f'Article with id {id} Not Found')

    return article