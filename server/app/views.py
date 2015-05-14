import os, cStringIO, zipfile
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from bookMaker import BookMaker

JSON = '[ { "replace": "Gatsby", "with": "Phil" }, { "replace": "man", "with": "fish" } ]'


def index(request):
    return HttpResponse("Hello, world!")
    
def getBook(request):
    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = 'filename="book.epub"'
    bookMaker = BookMaker(JSON)
    ret_zip = bookMaker.getZipStream()
    response.write(ret_zip)
    return response
    