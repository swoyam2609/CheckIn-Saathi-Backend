from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from dependencies import pass_jwt
from models import event
from dependencies import mongo, config

router = APIRouter()

@router.post("/events/create", tags=["Event"])
async def create_event(event: event.Event, token: str = Depends(config.oauth2_scheme)):
    temp = mongo.db.events.find_one({"unique_id": event.unique_id})
    if temp:
        return JSONResponse(content={"message": "Event already exists"}, status_code=400)
    try:
        username = pass_jwt.get_username_from_token(token)
        event.creator = username
        mongo.db.events.insert_one(event.dict())
        return JSONResponse(content={"message": "Event created successfully"}, status_code=200)
    except:
        return JSONResponse(content={"message": "Invalid token"}, status_code=400)
