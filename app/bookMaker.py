import os, io, zipfile, json

APP_DIR = os.path.dirname(os.path.abspath(__file__))

#TEST JSON = '[ { "replace": "Gatsby", "with": "Phil" }, { "replace": "man", "with": "fish" } ]'

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
                    if "main" in fileEntryName:
                        zip.writestr(fileEntryName, self.getFileContents(fileEntry.read()))
                    else:
                        contents = fileEntry.read()
                        zip.writestr(fileEntryName, contents)

        zip.close()
        buffer.flush()

        ret_zip = buffer.getvalue()
        buffer.close()

        return ret_zip

    def getFileContents(self, fileContents):
        replWords = self.replacementWords.decode("utf-8")
        newFileContents = fileContents
        for replaceEntry in json.loads(replWords):
            newFileContents = newFileContents.replace(replaceEntry['replace'].encode("ascii"), replaceEntry['with'].encode("ascii"))
        return newFileContents