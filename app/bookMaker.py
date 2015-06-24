import os, io, zipfile, json, urllib
import wordReplacer

APP_DIR = os.path.dirname(os.path.abspath(__file__))

class BookMaker:

    def __init__(self, replacementWords):
        self.replacementWords = replacementWords

    def getZipStream(self):
        fileName = os.path.join(APP_DIR, '../files/greatGatsby.epub')

        buffer = io.BytesIO()
        zip = zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED)

        with zipfile.ZipFile(fileName, 'r') as originalBook:
            for fileEntryName in originalBook.namelist():
                with originalBook.open(fileEntryName) as fileEntry:
                    if "main" in fileEntryName and fileEntryName.endswith('.xml'):
                        fileContents = wordReplacer.replaceWords(fileEntry.read(), self.replacementWords)
                        zip.writestr(fileEntryName, fileContents)
                    else:
                        zip.writestr(fileEntryName, fileEntry.read())

        zip.close()
        buffer.flush()

        ret_zip = buffer.getvalue()
        buffer.close()

        return ret_zip