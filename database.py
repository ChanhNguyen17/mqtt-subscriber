from pymongo import MongoClient

# MongoDB Configuration
mongo_uri = "mongodb://localhost:27017/"
db_name = "mqtt_messages"

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


# Get messages from db
def db_get_messages():
    messages = list(db.messages.find({}, {"_id": 0}))
    return messages
