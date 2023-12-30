from passlib.context import CryptContext
from jose import JWTError, jwt
from dependencies.config import SECRET_KEY, ALGORITHM
from datetime import timedelta, datetime


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_hashed_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_jwt_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt