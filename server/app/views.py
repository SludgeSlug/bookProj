from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from bookMaker import BookMaker

def getBook(request):
    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = 'filename="book.epub"'
    bookMaker = BookMaker(request.body)
    ret_zip = bookMaker.getZipStream()
    response.write(ret_zip)
    return response
    