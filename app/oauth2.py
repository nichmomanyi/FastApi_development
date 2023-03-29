from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

#SECRET KEY: special key that verifies the data integrity of token that resides on the server only
#Algorithm to be used(HS256)
# Expriation time of the token= prevents the user to be logged in forever

oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

#access token function
def create_access_token (data: dict):
    to_encode=data.copy()
    
    expire=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    
    return encoded_jwt

#function to verify the access token
def verify_access_token (token: str, credentials_exception):
    try: 
        payload=jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data=schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception 
    
    return token_data
    
#take token from from request, extract ID, verify if token is correct by
# calling the verify access token, extract ID and automatically fetch user from database and then add to path operation fxn
def get_current_user (token: str=Depends(oauth2_scheme)):
    credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                        detail="Could not validate credentials", headers={"WWW-Authenticate":"Bearer"})
    return verify_access_token(token, credentials_exception) 