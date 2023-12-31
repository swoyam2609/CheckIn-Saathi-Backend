from fastapi import FastAPI
from routers import users, event, registration

app = FastAPI()
app.include_router(users.router)
app.include_router(event.router)
app.include_router(registration.router)


@app.get("/")
async def root():
    return {"connection": True}