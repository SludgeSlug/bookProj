from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from app.bookMaker import BookMaker
from app.quoteGenerator import QuoteGenerator

def getBook(request):
    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = 'filename="book.epub"'
    
    requestData = request.body
    if requestData.startswith('data='):
        requestData = requestData[5:]
    
    bookMaker = BookMaker(requestData)
    ret_zip = bookMaker.getZipStream()
    response.write(ret_zip)
    return response
    
def getQuote(request):
    quoteGenerator = QuoteGenerator(request.GET['replacementWords'])
    return HttpResponse(quoteGenerator.getQuote(request.GET['index']))