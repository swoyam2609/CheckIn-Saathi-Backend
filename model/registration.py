from pydantic import BaseModel

class Atendee(BaseModel):
    unique_id: str = None
    name: str
    email: str
    phone: str
    status: bool = False
    event_id: str = None
    organizer: str = None