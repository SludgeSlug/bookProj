import os, cStringIO, zipfile
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper

APP_DIR = os.path.dirname(os.path.abspath(__file__))

def index(request):
    return HttpResponse("Hello, world!")
    
def getBook(request):
    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = 'filename="book.epub"'
    fileName = os.path.join(APP_DIR, '../files/greatGatsby.epub')
    
    buffer = cStringIO.StringIO()
    zip = zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED)
    
    with zipfile.ZipFile(fileName, 'r') as originalBook:
        for fileEntryName in originalBook.namelist():
            with originalBook.open(fileEntryName) as fileEntry:
                if "main" in fileEntryName:
                    zip.writestr(fileEntryName, fileEntry.read().replace("Gatsby", "Phil"))
                else:
                    zip.writestr(fileEntryName, fileEntry.read())
    
    zip.close()
    buffer.flush()

    ret_zip = buffer.getvalue()
    buffer.close()
    response.write(ret_zip)
    return response
    