# import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://vishnuprasadvbhat:p5OafHBJZQc3vZ3A@amazonreview.3kiqf.mongodb.net/?retryWrites=true&w=majority&appName=AmazonReview")

db = cluster['Amazon']
collections = db['User']

data = {"UserId" : 1, "Name": "Vishnuprasad", "Password": 1234, "Address" : "Mangalore", "Phone No": 123456789}


collections.insert_one(data)


