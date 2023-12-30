from pydantic import BaseModel

class Event(BaseModel):
    unique_id: str
    title: str
    description: str
    date: str
    time: str
    location: str
    creator: str = None