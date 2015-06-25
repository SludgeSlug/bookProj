import re
import config
from pymongo import MongoClient

def deleteCollection() :
    getCollection('word_paragraph_count').drop()

def writeToDb() :
    paragraphs = getCollection('paragraphs').find()
    words = getWords()
    documents = []
    documentId = 0
    for paragraph in paragraphs :
        wordCounts = getWordCounts(paragraph['paragraph'])
        for k, v in wordCounts.iteritems() :
            wordId = getWordId(words, k)
            if wordId is not None:
                documentId += 1
                documents.append({
                        '_id': documentId,
                        'wordId': wordId,
                        'paragraphId': paragraph['_id'],
                        'count': v
                    })
    getCollection('word_paragraph_count').insert_many(documents)
    
def getWords() :
    wordCollection = getCollection('words').find()
    words = []
    for word in wordCollection :
        words.append(word)
    return words
            
def getWordId(words, word):
    wordCount = 0
    for w in words :
        wordCount += 1
        if w['word'] == word :
            return w['_id']
    return None
    
def getWordCounts(paragraph) :
    wordCounts = {}
    words = re.split(r"[^a-zA-Z']+", paragraph)
    for word in words:
        if word != '' :
            updateWordsDictionary(wordCounts, word)
    return wordCounts
    
def updateWordsDictionary(words, word) :
    word = word.lower()
    if word in words.keys() :
        words[word] += 1
    else :
        words[word] = 1
    

def getCollection(collectionName) :
    connection = MongoClient(config.dbServer(), config.dbPort()) #Connect to mongodb
    db = connection[config.dbName()]
    db.authenticate(config.username(), config.password())
    return db[collectionName]

if __name__ == '__main__':
    deleteCollection()
    writeToDb()