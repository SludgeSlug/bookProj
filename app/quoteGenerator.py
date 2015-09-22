import os, zipfile, re, json, urllib
import wordReplacer

APP_DIR = os.path.dirname(os.path.abspath(__file__))

class QuoteGenerator:
    
    def __init__(self, replacementWords, db):
        self.replacementWords = replacementWords
        self.db = db
        
    def getQuote(self, index):
        paragraphCount = {}
        bookId = 1
        for replaceEntry in json.loads(self.replacementWords):
            word =  replaceEntry['replace'].encode("ascii")
            wordId = self.db['words'].find_one({'word':word.lower(), 'bookId': bookId})['_id']
            for count in self.db['word_paragraph_count'].find({'wordId': wordId}):
                self.updateCountDictionary(paragraphCount, count['paragraphId'], count['count'])
        paragraphCount = sorted(paragraphCount, key=paragraphCount.get, reverse=True)
        paragraphId = paragraphCount[int(index)]
        paragraph = self.db['paragraphs'].find_one({'_id' : paragraphId, 'bookId':bookId})['paragraph']
        paragraph = wordReplacer.replaceWords(paragraph, self.replacementWords)
        return paragraph
        
    def updateCountDictionary(self, dictionary, paragraphId, count):
        if paragraphId in dictionary.keys() :
            dictionary[paragraphId] += count
        else :
            dictionary[paragraphId] = count