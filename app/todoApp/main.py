from fastapi import FastAPI
from .database import connecnt_db
app = FastAPI()

@app.get("/db")
async def read_root():
  return await connecnt_db()