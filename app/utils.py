from passlib.context import CryptContext


pwd_context=CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash (password: str):
    return pwd_context.hash(password)

# Creating a function that verifies the passwords by comparing the hashes
def verify(plain_password, hash_password):
    return pwd_context.verify(plain_password, hash_password)
