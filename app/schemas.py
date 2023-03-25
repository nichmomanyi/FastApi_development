from pydantic import BaseModel, EmailStr
from datetime import datetime


class PostBase (BaseModel):
    title: str
    content: str 
    published: bool=True


class PostCreate (PostBase):
    pass

#Response
#N/B you can send back any column that you want
class Post(PostBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode=True

class UserCreate(BaseModel):
    email: EmailStr
    password:str
    
class UserOut (BaseModel):
    id:int
    email: EmailStr
    created_at:datetime
    
    class Config:
        orm_mode=True