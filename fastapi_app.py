from fastapi import FastAPI
from database import db_get_messages


def create_app():
    app = FastAPI()

    # API endpoint to get all messages
    @app.get("/messages")
    async def get_messages():
        return db_get_messages()

    return app
