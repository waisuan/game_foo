from pymongo import MongoClient

client = MongoClient()
ixion_db = client.ixion
npc_collection = ixion_db.npc
npc_collection.delete_many({})

npc1 = {"name": "jane", "dialogue": ["Hi! You look like you could use this..."], "gift": "POTION+"}
npc_collection.insert_one(npc1)
npc2 = {"name": "bob", "dialogue": ["Ever since RISE happened, people have been afraid of change. How sad..."],
        "gift": ""}
npc_collection.insert_one(npc2)
npc3 = {"name": "jackson", "dialogue": ["*grumble* What da hell do you want?!",
                                        ["What's the matter?", "Your life", "Nothing,"],
                                        ["GET OUTTA MY HOUSE!", "GO TO HELL!", "THEN, GET OUTTA MY HOUSE!"]],
        "gift": ""}
npc_collection.insert_one(npc3)
