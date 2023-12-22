from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin123@sypmin.k5vmzeq.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db

collection_name = db["todo_db"]

