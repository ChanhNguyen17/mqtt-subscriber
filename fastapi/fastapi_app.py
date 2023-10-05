from fastapi import FastAPI
from mongo_client import db_get_messages

# Create an instance of the FastAPI class
app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Welcome to MQTT subscriber app, please go to /messages"}


@app.get("/messages")
async def get_messages():
    return db_get_messages()
