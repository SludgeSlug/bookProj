import re
import paragraphGenerator, config
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

def deleteCollection() :
    collection = getWordsCollection()
    collection.drop()

def writeWordsToDb(bookId, fileName):
    wordsToSave = {}
    for paragraph in paragraphGenerator.getMergedParagraphs(fileName):
        words = re.split(r"[^a-zA-Z']+", paragraph)
        for word in words:
            if word != '' :
                updateDictionary(wordsToSave, word)
    wordDocuments = []
    for k, v in wordsToSave.iteritems() :
        wordDocuments.append({
                "word": k,
                "bookId": bookId,
                "count": v
            })
    collection = getWordsCollection()
    collection.insert_many(wordDocuments)
    collection.ensure_index("word")
    
            
def updateDictionary(words, word) :
    word = word.lower()
    if word in words.keys() :
        words[word] += 1
    else :
        words[word] = 1

def getWordsCollection():
    connection = MongoClient(config.dbServer(), config.dbPort()) #Connect to mongodb
    db = connection[config.dbName()]
    db.authenticate(config.username(), config.password())
    return db['words']