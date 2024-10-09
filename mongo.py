# import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://vishnuprasadvbhat:p5OafHBJZQc3vZ3A@amazonreview.3kiqf.mongodb.net/?retryWrites=true&w=majority&appName=AmazonReview")


db = cluster['product'] # this is the database 

# db.Counters.update_one(
#     {"_id": "2"},
#     {"$setOnInsert": {"seq_val": 0}},
#     upsert=True
# )

# db.Counters.update_one(
#     {"_id": "1"},
#     {"$setOnInsert": {"seq_val": 0}},
#     upsert=True
# )

# # Auto-increment function
# def auto_increment(sequence_id):
#     seq_doc = db.Counters.find_one_and_update(
#         {"_id": sequence_id},
#         {"$inc": {"seq_val": 1}},
#         return_document=True
#     )
    
#     if seq_doc is None:  # Handle the case where the document doesn't exist
#         return 0  # Or some other appropriate value

#     return seq_doc["seq_val"]

# # Get new IDs for both users
# new_id = auto_increment("1")
# new_id2 = auto_increment("2")

# # Insert multiple users with the auto-incremented IDs
# db.Users.insert_many([
#     { "_id": new_id, "username": "Vishnuprasad" },
#     { "_id": new_id2, "username": "Rahul" }
# ])

# # Print the Users collection to verify
# users = list(db.Users.find())
# for user in users:
#     print(user)

# users = list(db.Users.find())
# for user in users:
#     print(user)

import pandas as pd
