from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    # hash the password - user.password
    hashed_password = pwd_context.hash(password)
    return hashed_password