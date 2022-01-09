# from _typeshed import SupportsLessThan
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas import DisplayUser, UserBase
from db import db_user

router=APIRouter(prefix='/user',tags=['user'])

# ALL Operations

# Create User
@router.post('/',response_model=DisplayUser)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db,request)


# Read all User

@router.get('/all',response_model=List[DisplayUser])
def get_all_users(db: Session = Depends(get_db) ):
    return db_user.get_all_users(db)

# Read user by Id
@router.get('/{id}',response_model=DisplayUser)
def get_users_by_id(id : int , db: Session = Depends(get_db)):
    return db_user.display_user_by_id(id,db)


# Update User
@router.post('/{id}/update')
def update_user(id: int ,request: UserBase,db: Session = Depends(get_db)):
    return db_user.update_user(db,id,request)

# Delete User
@router.get('/delete/{id}')
def delete_user(id: int ,db: Session=Depends(get_db)):
    return db_user.delete_user( id , db)