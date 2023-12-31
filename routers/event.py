from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from model import event
from dependencies import mongo, pass_jwt

router = APIRouter()

@router.post("/events/create", tags=["Event"])
async def create_event(event: event.Event, username: str = Depends(pass_jwt.get_current_user)):
    temp = mongo.db.events.find_one({"unique_id": event.unique_id})
    if temp:
        return JSONResponse(content={"message": "Event id already exists"}, status_code=400)
    else:
        user = mongo.db.users.find_one({"username": username})
        newevent = {
            "unique_id": event.unique_id,
            "name": event.name,
            "description": event.description,
            "start_date": event.start_date,
            "end_date": event.end_date,
            "start_time": event.start_time,
            "end_time": event.end_time,
            "location": event.location,
            "organizer": username,
            "organizer_email": user["email"],
            "organizer_phone": user["phone"]
        }
    mongo.db.events.insert_one(newevent)
    return {"message": "Event created successfully"}

@router.put("/events/update", tags=["Event"])
async def update_event(event: event.Event, username: str = Depends(pass_jwt.get_current_user)):
    temp = mongo.db.events.find_one({"unique_id": event.unique_id})
    if temp:
        if temp["organizer"] == username:
            mongo.db.events.update_one({"unique_id": event.unique_id}, {"$set": {"name": event.name, "description": event.description, "start_date": event.start_date, "end_date": event.end_date, "start_time": event.start_time, "end_time": event.end_time, "location": event.location}})
            return {"message": "Event updated successfully"}
        else:
            return JSONResponse(content={"message": "You are not the organizer of this event"}, status_code=400)
    else:
        return JSONResponse(content={"message": "Event id not found"}, status_code=400)
    
@router.delete("/events/delete", tags=["Event"])
async def delete_event(unique_id: str, username: str = Depends(pass_jwt.get_current_user)):
    temp = mongo.db.events.find_one({"unique_id": unique_id})
    if temp:
        if temp["organizer"] == username:
            mongo.db.events.delete_one({"unique_id": unique_id})
            return {"message": "Event deleted successfully"}
        else:
            return JSONResponse(content={"message": "You are not the organizer of this event"}, status_code=400)
    else:
        return JSONResponse(content={"message": "Event id not found"}, status_code=400)
    
@router.get("/events/get", tags=["Event"])
async def get_event(unique_id: str):
    temp = mongo.db.events.find_one({"unique_id": unique_id})
    if temp:
        return temp
    else:
        return JSONResponse(content={"message": "Event id not found"}, status_code=400)
    
@router.get("/events/get/all", tags=["Event"])
async def get_all_events(username: str = Depends(pass_jwt.get_current_user)):
    temp = mongo.db.events.find({"organizer": username})
    if temp:
        return list(temp)
    else:
        return JSONResponse(content={"message": "No events found"}, status_code=400)