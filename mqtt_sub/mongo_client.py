from pymongo import MongoClient
import os

# MongoDB Configuration
mongo_uri = os.environ["MONGO_URI"]
db_name = os.environ["MONGO_DB_NAME"]

# Initialize the MongoDB client
client = MongoClient(mongo_uri)
db = client[db_name]


# Save a message to db
def db_save_message(payload, timestamp):
    message = {
        "payload": payload,
        "timestamp": timestamp
    }
    db.messages.insert_one(message)
