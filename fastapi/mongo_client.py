from pymongo import MongoClient
import os

# MongoDB Configuration
mongo_uri = os.environ["MONGO_URI"]
db_name = os.environ["MONGO_DB_NAME"]

# Initialize the MongoDB client
client = MongoClient(mongo_uri)
db = client[db_name]


# Get messages from db
def db_get_messages():
    messages = list(db.messages.find({}, {"_id": 0}))
    return messages
