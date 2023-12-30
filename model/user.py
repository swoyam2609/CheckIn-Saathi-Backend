from pydantic import BaseModel

class User(BaseModel):
    username: str
    name: str
    email: str
    phone: str
    password: str