import os
from pydantic import BaseSettings 


class Settings(BaseSettings): # list of environment variables
    DATABASE_HOSTNAME: str 
    DATABASE_PORT: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_USERNAME: str
    SECRET_KEY: str
    ALGORITHM: str 
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    class Config:
        env_file=".env"
    
settings = Settings()    

#Working with environment variables after setting it in a 
# file rather than setting in terminal or in GUI for windows to do it 