import json
import os
from mongita import MongitaClientDisk

f = open("movie-list.json")
movies = json.load(f)

client = MongitaClientDisk()
movies_db = client.movies_db

movies_collection = movies_db.movies_collection
movies_collection.delete_many({})

movies_collection.insert_many(movies)

print(f"added : {movies_collection.count_documents({})} movies")