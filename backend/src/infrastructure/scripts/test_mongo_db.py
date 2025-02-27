from infrastructure.database.mongo import get_mongo_client

client = get_mongo_client()
db = client["test"]
collection = db["users"]

data = [
    {"name": "Frank", "age": 25},
    {"name": "Anna", "age": 30},
]

collection.insert_many(data)
print("Данные добавлены")
