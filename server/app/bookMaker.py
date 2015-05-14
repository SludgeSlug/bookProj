import os, cStringIO, zipfile

APP_DIR = os.path.dirname(os.path.abspath(__file__))

class BookMaker:
    
    @staticmethod
    def getZipStream(json):
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
        
        return ret_zip