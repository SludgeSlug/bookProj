import os, zipfile, re, json, urllib
import wordReplacer, config
from pymongo import MongoClient

APP_DIR = os.path.dirname(os.path.abspath(__file__))

class QuoteGenerator:
    
    def __init__(self, replacementWords):
        self.replacementWords = replacementWords
        
    def getQuote(self, index):
        paragraphCount = {}
        db = getdb()
        for replaceEntry in json.loads(self.replacementWords):
            word =  replaceEntry['replace'].encode("ascii")
            wordId = db['words'].find_one({'word':word.lower()})['_id']
            for count in db['word_paragraph_count'].find({'wordId': wordId}):
                self.updateCountDictionary(paragraphCount, count['paragraphId'], count['count'])
        paragraphCount = sorted(paragraphCount, key=paragraphCount.get, reverse=True)
        paragraphId = paragraphCount[int(index)]
        paragraph = db['paragraphs'].find_one({'_id' : paragraphId})['paragraph']
        paragraph = wordReplacer.replaceWords(paragraph, self.replacementWords)
        return paragraph
        
    def updateCountDictionary(self, dictionary, paragraphId, count):
        if paragraphId in dictionary.keys() :
            dictionary[paragraphId] += count
        else :
            dictionary[paragraphId] = count
    
def getdb() :
    uri = "mongodb://" + config.username() + ":" + config.password() + "@" + config.dbServer() + ":" + str(config.dbPort()) + "/" + config.dbName()
    client = MongoClient(uri)
    db = client.get_default_database()
    return db