from pymongo import MongoClient

client = MongoClient()
db = client.ixion
collection = db.npc
for doc in collection.find():
    print doc

test_npc = {"name": "jane", "dialogue": "Hi! You look like you could use this...", "gift": "POTION+"}
collection.insert_one(test_npc)

collection.delete_one({"name": "jane"})
