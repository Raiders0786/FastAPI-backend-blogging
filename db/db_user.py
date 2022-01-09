

from fastapi import status , HTTPException
from db import Hash
from sqlalchemy.orm.session import Session
from db.models import DbUser 
from schemas import UserBase
from db.Hash import Hash

# creation of user in the database
def create_user(db: Session ,request: UserBase ):
    new_user = DbUser(
        username= request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    #adding new user to the database
    db.add(new_user)
    #commiting the data into the database
    db.commit() 
    # refreshing is necessary to sync the data & id's properly to the new user other than the default data's
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
     # Handle Any Exceptions
    user = db.query(DbUser).all()
    if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
          detail='User Cant be Fetched')
    return user

def display_user_by_id(id: int, db : Session):
    return db.query(DbUser).filter(DbUser.id == id).first()

def display_user_by_username(username: str, db : Session):
    user= db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
          detail=f'User with Username {user} doesnot exist !')
    return user

def update_user(db: Session ,id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
     # Handle Any Exceptions
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
          detail=f'User with id {id} doesnot exist !')

    user.update({
        DbUser.username : request.username,
        DbUser.email : request.email ,
        DbUser.password : Hash.bcrypt(request.password) }
    )
    db.commit()
    #db.refresh(user)
    return "Ok"


def delete_user(id: int ,db: Session ):
    user= db.query(DbUser).filter(DbUser.id == id ).first()
    # Handle Any Exceptions
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
          detail=f'User with id {id} doesnot exist !')
    db.delete(user)
    db.commit()
    return "Deleted"
