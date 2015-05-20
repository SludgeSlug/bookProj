import os, zipfile, re

APP_DIR = os.path.dirname(os.path.abspath(__file__))

class QuoteGenerator:
    
    def getQuote(self):
        
        quotes = self.getMergedParagraphs()
        
        for quote in quotes:
            print quote
        
        
    def getMergedParagraphs(self):
        previousQuote = ''
        for quote in self.getAllParagraphs() :
            if previousQuote != '':
                quote = previousQuote + ' ' + quote
                previousQuote = ''
                
            if len(quote) > 250:
                yield quote
            else :
                previousQuote = quote
                            
    def getAllParagraphs(self):
        
        fileName = os.path.join(APP_DIR, '../files/greatGatsby.epub')
        regex = re.compile(r'.*<p>((.|\n)*?)<\/p>', re.MULTILINE)
        
        with zipfile.ZipFile(fileName, 'r') as originalBook:
            for fileEntryName in originalBook.namelist():
                with originalBook.open(fileEntryName) as fileEntry:
                    if "main" in fileEntryName and fileEntryName.endswith('.xml'):
                        iterator = regex.finditer(fileEntry.read())
                        for match in iterator:
                            yield match.group(1)

if __name__ == "__main__":
    bm = QuoteGenerator()
    bm.getQuote()