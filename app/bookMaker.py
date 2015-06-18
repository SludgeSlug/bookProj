import os, io, zipfile, json, urllib

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
                        zip.writestr(fileEntryName, self.getFileContents(fileEntry.read()))
                    else:
                        zip.writestr(fileEntryName, fileEntry.read())

        zip.close()
        buffer.flush()

        ret_zip = buffer.getvalue()
        buffer.close()

        return ret_zip

    def getFileContents(self, fileContents):
        if self.replacementWords == '':
            return fileContents
        for replaceEntry in json.loads(self.replacementWords):
            fileContents = fileContents.replace(replaceEntry['replace'].encode("ascii"), replaceEntry['with'].encode("ascii"))
        return fileContents