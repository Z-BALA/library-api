from pymongo import MongoClient

MONGO_URL = "mongodb://mongo:27017"

client = MongoClient(MONGO_URL)

db = client["library_db"]

books_collection = db["books"]
