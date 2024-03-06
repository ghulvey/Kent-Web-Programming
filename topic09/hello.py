from flask import Flask, jsonify, send_from_directory, render_template, request, redirect
from mongita import MongitaClientDisk


app = Flask(__name__)

@app.route('/', methods=["GET"])
def get_hello():
    name = request.args.get('name', None)
    password = request.args.get('password', None)
    print(f'Name: {name}, Password: {password}')
    data = {
        'name': name,
        'password': password
    }
    return render_template('index.html', data=data)

@app.route("/", methods=["POST"])
def post_hello():
    name = request.form.get('name', None)
    password = request.form.get('password', None)
    print(f'Name: {name}, Password: {password}')
    data = {
        'name': name,
        'password': password
    }
    return render_template('index.html', data=data)
    #usually do a redirect here