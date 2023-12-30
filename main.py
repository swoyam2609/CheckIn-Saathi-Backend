from fastapi import FastAPI
from routers import user, event

app = FastAPI()
app.include_router(user.router)
app.include_router(event.router)

@app.get("/")
async def root():
    return {"connection": True}