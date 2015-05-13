import os
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper

APP_DIR = os.path.dirname(os.path.abspath(__file__))

def index(request):
    return HttpResponse("Hello, world!")
    
def getBook(request):
    fileName = os.path.join(APP_DIR, '../files/greatGatsby.epub')
    wrapper = FileWrapper(file(fileName))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Length'] = os.path.getsize(fileName)
    return response
    