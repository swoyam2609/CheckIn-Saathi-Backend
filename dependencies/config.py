from fastapi.security import OAuth2PasswordBearer

mongourl = "mongodb+srv://swoyamsiddharthnayak:swoyamsiddharthnayak@cluster1.jar6lr0.mongodb.net/"
SECRET_KEY = "checkinsaathi"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")