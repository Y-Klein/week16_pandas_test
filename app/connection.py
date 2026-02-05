from pymongo import MongoClient
from os import getenv



mongo_uri = getenv("MONGO_URI", "mongodb+srv://yklain:vW6pAW0dB6958k5P@mycluster.rd922r5.mongodb.net")
mongo_db = getenv("MONGO_DB", "testdb")
mongo_collection = getenv("MONGO_COLLECTION", "testcollection")

client = MongoClient(mongo_uri)
db = client[mongo_db]
collection = db[mongo_collection]
db.command("ping")


