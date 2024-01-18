from fastapi import FastAPI
from routers import users, event, registration
from dependencies.config import origins
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
app.include_router(users.router)
app.include_router(event.router)
app.include_router(registration.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"connection": True}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
