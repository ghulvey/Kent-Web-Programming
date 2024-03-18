from flask import Flask, jsonify, send_from_directory, render_template, request, redirect, make_response
from mongita import MongitaClientDisk
import uuid

session_key = uuid.uuid4()

app = Flask(__name__)

client = MongitaClientDisk()
db = client.quotes_db
collection = db.quotes

def logged_in():
    session_id = request.cookies.get('session_id', None)
    if session_id is None:
        return False
    return True

@app.route('/', methods=["GET"])
@app.route('/quotes', methods=["GET"])
def get_quotes():
    visits = int(request.cookies.get('visits', 1))

    if not logged_in():
        return "You are not logged in. Please <a href='./login'>log in</a> to view the quotes."

    page= request.args.get('page', 1)
    data = list(collection.find({}))
    data = data[(int(page)-1)*5:int(page)*5]
    count = collection.count_documents({})
    maxPages = int(count/5)+1
    if (int(page) > maxPages) or (int(page) < 1):
        return redirect('/')

    response = make_response(render_template('quotes.html', quotes=data, count=count, page=int(page), maxPages=maxPages, visits=visits))
    response.set_cookie('visits', str(int(visits)+1))
    return response

@app.route('/delete/<id>', methods=["GET"])
def delete_quote(id=None):
    if not logged_in():
        return "You are not logged in. Please <a href='./login'>log in</a> to view the quotes."
    collection.delete_one({"_id": id})

    return redirect('/')

@app.route('/create', methods=["GET"])
def create_quote():
    if not logged_in():
        return "You are not logged in. Please <a href='./login'>log in</a> to view the quotes."
    return render_template('newQuote.html')

@app.route('/create', methods=["POST"])
def add_quote():
    if not logged_in():
        return "You are not logged in. Please <a href='./login'>log in</a> to view the quotes."
    quote = request.form.get('quote', None)
    author = request.form.get('author', None)
    collection.insert_one({"text": quote, "author": author})
    return redirect('/')

@app.route('/edit/<id>', methods=["GET"])
def edit_quote(id=None):
    if not logged_in():
        return "You are not logged in. Please <a href='./login'>log in</a> to view the quotes."
    item = collection.find_one({"_id": id})
    return render_template('editQuote.html', quote=item)


@app.route('/edit/<id>', methods=["POST"])
def post_edit_quote(id=None):
    if not logged_in():
        return "You are not logged in. Please <a href='./login'>log in</a> to view the quotes."
    quote = request.form.get('quote', None)
    author = request.form.get('author', None)
    collection.delete_one({"_id": id})
    collection.insert_one({"text": quote, "author": author})
    # collection.update_one({ "_id": id }, {'$set': {"text": quote, "author": author}})
    return redirect('/')

@app.route('/signin')
@app.route('/login')
def login():
    session_id = str(uuid.uuid4())
    response = make_response(redirect('/'))
    response.set_cookie('session_id', session_id)
    return response

@app.route('/signout')
@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('session_id')
    return response