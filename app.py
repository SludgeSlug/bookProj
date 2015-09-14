import os
from pymongo import MongoClient
from flask import Flask, render_template, send_from_directory, request, make_response
from app.quoteGenerator import QuoteGenerator
from app.bookMaker import BookMaker
from app import config

def primeDb():
    connection = MongoClient(config.dbServer(), config.dbPort()) #Connect to mongodb
    db = connection[config.dbName()]
    db.authenticate(config.username(), config.password())
    return db

app = Flask(__name__)
db = primeDb()

@app.route('/scripts/<path:path>')
def send_js(path):
    return send_from_directory('client/scripts', path)
    
@app.route('/views/<path:path>')
def send_view(path):
    return send_from_directory('client/views', path)
    
@app.route('/style/<path:path>')
def send_style(path):
    return send_from_directory('client/style', path)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/api/book', methods=['POST'])
def downloadBook():
    bookMaker = BookMaker(request.form['data'])
    response = make_response(bookMaker.getZipStream())
    response.headers["Content-Disposition"] = "attachment; filename=book.epub"
    return response
    
@app.route('/api/quote')
def quote():
    quoteGenerator = QuoteGenerator(request.args.get('replacementWords'), db)
    return quoteGenerator.getQuote(request.args.get('index'))

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)