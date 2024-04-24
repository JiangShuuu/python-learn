import uvicorn
from fastapi import FastAPI
from database import create_tables

app = FastAPI()

async def startup():
    await create_tables()

app.router.add_event_handler("startup", startup)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
