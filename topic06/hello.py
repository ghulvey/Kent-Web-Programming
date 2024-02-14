from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    me = "Gavin"
    return f'<p>Hello, {me}!</p>'

@app.route('/hello')
def hello():
    me = "Gavin"
    return f'<p>Hello, {me}!</p>'


@app.route('/goodbye')
def goodbye():
    me = "Gavin"
    return f'<p>Goodbye, {me}!</p>'

@app.route('/data')
def data():
    data = [
        {'name': 'Suzzy', 'type': 'dog'},
        {'name': 'Mittens', 'type': 'cat'},
        {'name': 'Goldie', 'type': 'fish'},
    ]
    return jsonify(data)

@app.route('/api/status')
def status():
    return jsonify([
        {'name': 'Suzzy', 'status': 'good'},
        {'name': 'Mittens', 'status': 'bad'},
        {'name': 'Goldie', 'status': 'ugly'},
    ])

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
