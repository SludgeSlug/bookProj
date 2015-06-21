import os
from flask import Flask, render_template, send_from_directory, request, make_response
from app.quoteGenerator import QuoteGenerator
from app.bookMaker import BookMaker

app = Flask(__name__)

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
    quoteGenerator = QuoteGenerator(request.args.get('replacementWords'))
    return quoteGenerator.getQuote(request.args.get('index'))

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)