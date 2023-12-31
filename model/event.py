from pydantic import BaseModel

class Event(BaseModel):
    unique_id: str
    name: str
    description: str
    start_date: str
    end_date: str
    start_time: str
    end_time: str
    location: str
    organizer: str = None
    organizer_email: str = None
    organizer_phone: str = None
