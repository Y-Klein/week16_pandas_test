from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv

load_dotenv()


mongo_uri = getenv("MONGO_URI")
mongo_db = getenv("MONGO_DB", "testdb")
mongo_collection = getenv("MONGO_COLLECTION", "testcollection")

client = MongoClient(mongo_uri)
db = client[mongo_db]
collection = db[mongo_collection]
db.command("ping")


