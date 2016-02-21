from pymongo import MongoClient

client = MongoClient()
ixion_db = client.ixion
items_collection = ixion_db.items
items_collection.delete_many({})

item1 = {"name": "plain_javelin", "attk": "9", "def": "0", "cost": "10"}

# NAME,ATTK,DEF,COST
# PLAIN_JAVELIN,9,0,10
# PLAIN_SWORD,10,0,11
# PLAIN_CROSSBOW,8,0,9
# PLAIN_AXE,12,0,12
# PLAIN_ROD,1,0,9
# SILVER_JAVELIN,18,0,30
# SILVER_SWORD,20,0,30
# SILVER_CROSSBOW,16,0,30
# SILVER_AXE,24,0,30
# SILVER_ROD,5,0,30
# POTION,0,0,5
# LARGE_POTION,0,0,15
