import os, zipfile, re, json, urllib
import wordReplacer

APP_DIR = os.path.dirname(os.path.abspath(__file__))

class QuoteGenerator:
    
    def __init__(self, replacementWords):
        self.replacementWords = replacementWords
    
    def getQuote(self, index):
        quotes = self.getMergedParagraphs()
        matches = []
        
        for quote in quotes:
            matches.append([self.getNumberOfMatches(quote),quotes.index(quote)])

        matches = sorted(matches, key=lambda tup: tup[0], reverse=True)
        #second int in matches element is index of quote
        return wordReplacer.replaceWords(quotes[matches[int(index)][1]], self.replacementWords);

    def getNumberOfMatches(self, originalString):
        numberOfMatches = 0
        if self.replacementWords == '':
            return numberOfMatches
        for replaceEntry in json.loads(self.replacementWords):
            numberOfMatches += originalString.count(replaceEntry['replace'].encode("ascii"))
        return numberOfMatches
        
        
    def getMergedParagraphs(self):
        paragraphs = []
        previousParagraph = ''
        for paragraph in self.getAllParagraphs() :
            if previousParagraph != '':
                paragraph = previousParagraph + ' ' + paragraph
                previousParagraph = ''
                
            if len(paragraph) > 250:
                paragraphs.append(paragraph)
            else :
                previousParagraph = paragraph
        return paragraphs
                            
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