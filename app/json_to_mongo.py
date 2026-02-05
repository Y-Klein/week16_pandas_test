import json
from pymongo import MongoClient
from os import getenv


mongo_uri = getenv("MONGO_URI", "mongodb+srv://yklain:vW6pAW0dB6958k5P@mycluster.rd922r5.mongodb.net")
mongo_db = getenv("MONGO_DB", "testdb")
mongo_collection = getenv("MONGO_COLLECTION", "testcollection")
file_path = './data/employee_data_advanced.json'

# Making Connection
myclient = MongoClient(mongo_uri)

# database
db = myclient[mongo_db]

# Created or Switched to collection
# names: GeeksForGeeks
Collection = db[mongo_collection]

# Loading or Opening the json file
with open(file_path) as file:
    file_data = json.load(file)

# Inserting the loaded data in the Collection
ins_result = Collection.insert_many(file_data)
print(f"Data inserted to MongoDB. Documents inserted: {len(ins_result.inserted_ids)}")