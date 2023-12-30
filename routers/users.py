from fastapi import APIRouter

from dependencies import usermongo


router = APIRouter()

@router.get("/users", tags=["User"])
async def get_users():
    return [{"name": "Harry"}, {"name": "Ron"}]

@router.post("/users/signup", tags=["User"])
async def signup():
    