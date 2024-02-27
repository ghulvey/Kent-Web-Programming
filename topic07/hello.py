from flask import Flask, jsonify, send_from_directory
from mongita import MongitaClientDisk

app = Flask(__name__)

client = MongitaClientDisk()
movies_db = client.movies_db
movies_collection = movies_db.movies_collection 

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/movies')
def movies():
    movies = list(movies_collection.find({}))

    for movie in movies:
        del movie['_id']
    return jsonify(movies)
