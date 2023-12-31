from fastapi.routing import APIRouter
from model import registration, event
from fastapi import Depends
import csv
from fastapi.responses import JSONResponse, FileResponse
from dependencies import pass_jwt, mongo
import random

router = APIRouter()

@router.post("/events/register", tags=["Registration"])
async def register_event(event_id: str, atendee: registration.Atendee, username: str = Depends(pass_jwt.get_current_user)):
    temp = mongo.db.atendees.find_one({"email": atendee.email})
    if temp:
        return JSONResponse(content={"message": "Email already exists"}, status_code=400)
    temp = mongo.db.events.find_one({"unique_id": event_id})
    if temp["organizer"] != username:
        return JSONResponse(content={"message": "You are not the organizer of this event"}, status_code=400)
    elif temp["organizer"] == username:
        event_id = temp["unique_id"]
        randreg = random.randint(1, 99999999999)
        atendee_id = event_id + str(randreg)
        newatendee = {
            "unique_id": atendee_id,
            "name": atendee.name,
            "email": atendee.email,
            "phone": atendee.phone,
            "event_id": event_id,
            "checkin": False,
            "organizer": temp["organizer"]
        }
        mongo.db.atendees.insert_one(newatendee)
        return JSONResponse(content={"message": "Atendee registered successfully"}, status_code=200)
    else:
        return JSONResponse(content={"message": "Event id not found"}, status_code=400)
    
@router.get("/events/get/registered", tags=["Registration"])
async def get_registered_events(event_id: str, username: str = Depends(pass_jwt.get_current_user)):
    temp = mongo.db.events.find_one({"unique_id": event_id})
    if temp["organizer"] == username:
        atendees = []
        for atendee in mongo.db.atendees.find({"event_id": event_id}):
            atendee["_id"] = str(atendee["_id"])
            atendees.append(atendee)
        return atendees
    else:
        return JSONResponse(content={"message": "You are not the organizer of this event"}, status_code=400)
    
@router.get("/events/get/registered/conditional", tags=["Registration"])
async def get_registered_events(event_id: str, username: str = Depends(pass_jwt.get_current_user), checkin: bool = False):
    temp = mongo.db.events.find_one({"unique_id": event_id, "checkin": checkin})
    if temp["organizer"] == username:
        atendees = []
        for atendee in mongo.db.atendees.find({"event_id": event_id}):
            atendee["_id"] = str(atendee["_id"])
            atendees.append(atendee)
        return atendees
    else:
        return JSONResponse(content={"message": "You are not the organizer of this event"}, status_code=400)
    
@router.put("/events/users/checkin", tags=["Registration"])
async def checkin_user(atendee_id: str, username: str = Depends(pass_jwt.get_current_user)):
    temp = mongo.db.atendees.find_one({"unique_id": atendee_id})
    if temp:
        if temp["organizer"] == username:
            mongo.db.atendees.update_one({"unique_id": atendee_id}, {"$set": {"checkin": True}})
            return JSONResponse(content={"message": "Atendee checked in successfully"}, status_code=200)
        else:
            return JSONResponse(content={"message": "You are not the organizer of this event"}, status_code=400)
    else:
        return JSONResponse(content={"message": "Atendee id not found"}, status_code=400)

@router.get("/events/users/download", tags=["Registration"])
async def get_all_users(event_id: str, username: str = Depends(pass_jwt.get_current_user)):
    temp = mongo.db.events.find_one({"unique_id": event_id})
    if temp["organizer"] == username:
        atendees = []
        for atendee in mongo.db.atendees.find({"event_id": event_id}):
            atendee["_id"] = str(atendee["_id"])
            with open("atendees.csv", "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=atendee.keys())
                writer.writeheader()
                writer.writerow(atendee)
        return FileResponse("atendees.csv", media_type="application/octet-stream", filename="atendees.csv")
    else:
        return JSONResponse(content={"message": "You are not the organizer of this event"}, status_code=400)