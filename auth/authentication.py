from fastapi import APIRouter , HTTPException , status
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from db.database import get_db
from db.models import DbUser
from db.Hash import Hash
from auth import ouath2


router = APIRouter(tags=['Authentication'])

# we need to pass same token url name as in Ouath token url param name i..e token in the routers request

@router.post('/token')

def authenticate_user(request: OAuth2PasswordRequestForm = Depends() , db: Session =Depends(get_db)):

    user = db.query(DbUser).filter(DbUser.username == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Invalid Crendentials")
    if not Hash.verfiy(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid password")
    access_token = ouath2.create_access_token(data={'sub': user.username})
    return {
    'access_token':access_token,
    'token_type': 'bearer',
    'user_id': user.id,
    'username' : user.username
}