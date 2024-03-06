from flask import Flask, jsonify, send_from_directory, render_template
from mongita import MongitaClientDisk


app = Flask(__name__)

client = MongitaClientDisk()
movies_db = client.movies_db
movies_collection = movies_db.movies_collection 

@app.route('/')
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name="World"):
    return render_template('index.html', name=name, items=["apple", "banana", "cherry"])

@app.route('/movies')
@app.route('/movies/<keyword>')
def movies(keyword=None):
    movies = list(movies_collection.find({}))
    for movie in movies:
        del movie['_id']
    if keyword:
        filtered_movies = []
        for movie in movies:
            if keyword in movie['plot']:
                filtered_movies.append(movie)
        movies = filtered_movies
    return render_template('movies.html', movies=movies)
