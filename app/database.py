from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#postgress
import psycopg2  
from psycopg2.extras import RealDictCursor
import time

# SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<hostname>/<database_name>"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:nichdee254@localhost/fastapi"

engine=create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Database initialization
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        

# # The code is nolonger in use but good for referencing incase I want to Connect to database Incase i want to run 
# # raw SQL directly using postgres library (psycopg) rather than using 

# # CONNECTING TO OUR DATABASE
# while True:
#     try: 
#         conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='nichdee254',cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print('Database connection was successful !!')
#         break
    
#     except Exception as error:
#         print("Connecting to database failed")   
#         print("Error: ", error)
#         time.sleep(2)
    
