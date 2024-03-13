import json
from mongita import MongitaClientDisk

# Create a new MongitaClientDisk instance

quotes = [
        {
            "text": "Hello, World!",
            "author": "Anonymous"
        },
        {
            "text": "This is a quote",
            "author": "Anonymous"
        },
        {
            "text": "This is another quote",
            "author": "Anonymous"
        }
    ]

client = MongitaClientDisk()
db = client.quotes_db
collection = db.quotes

# Insert the quotes into the collection
for quote in quotes:
    collection.insert_one(quote)
