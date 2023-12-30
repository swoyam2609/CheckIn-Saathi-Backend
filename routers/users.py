from fastapi import APIRouter
from model import user
from dependencies import mongo, email_auth, pass_jwt
from fastapi.responses import JSONResponse

router = APIRouter()

async def signup(user : user.User):
    newuser = {
        "username": user.username,
        "name": user.name,
        "email": user.email,
        "phone": user.phone,
        "password": pass_jwt.create_hashed_password(user.password)
    }
    mongo.db.users.insert_one(newuser)
    return {"message": "User created successfully"}

@router.post("/users/signup", tags=["User"])
async def signup_user(user : user.User):
    if mongo.db.users.find_one({"email": user.email}):
        return JSONResponse(content={"message": "Email already exists"}, status_code=400)
    elif mongo.db.users.find_one({"phone": user.phone}):
        return JSONResponse(content={"message": "Phone already exists"}, status_code=400)
    elif mongo.db.users.find_one({"username": user.username}):
        return JSONResponse(content={"message": "Username already exists"}, status_code=400)
    else:
        email_auth.send_otp(user.email)
        return JSONResponse(content={"message": "OTP sent successfully"}, status_code=200)

@router.post("/users/verify", tags=["User"])
async def verify_user(user : user.User, otp: str):
    response = email_auth.verify_otp(user.email, otp)
    if response == True:
        return await signup(user)
    else:
        return response

@router.get("/users/login", tags=["User"])
async def login_user(username: str, password: str):
    user = mongo.db.users.find_one({"username": username})
    if user:
        if pass_jwt.verify_password(password, user["password"]):
            jwt_token = pass_jwt.create_jwt_token({"username": user["username"]})
            return {"message": "Login successful", "token": jwt_token, "token_type": "bearer"}
        else:
            return JSONResponse(content={"message": "Password is incorrect"}, status_code=400)
    else:
        return JSONResponse(content={"message": "Username not found"}, status_code=400)