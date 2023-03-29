from fastapi import APIRouter, Depends, status, HTTPException, Response, FastAPI
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
router=APIRouter(tags=["Authentication"])
from ..database import get_db
from .. import schemas, models, utils, oauth2


@router.post('/login', response_model=schemas.Token)
def login (user_credentials: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(get_db)):
    
    #It wil grab be default a dictionary with username and password. Does not really matter if the user signed in with email, or number
    user=db.query(models.User).filter(models.User.email==user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    #create token
    #return token
    access_token=oauth2.create_access_token(data={"user_id":user.id})
    
    return {"access_token":access_token, "token_type": "bearer"}