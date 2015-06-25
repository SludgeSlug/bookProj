import os, re, zipfile, sys
import config
from pymongo import MongoClient

APP_DIR = os.path.dirname(os.path.abspath(__file__))

def deleteCollection():
    collection = getParagraphsCollection()
    collection.drop()

def writeParagraphsToDb():
    paragraphDocuments = []
    paragraphNumber = 0
    for paragraph in getMergedParagraphs():
        paragraphNumber += 1
        paragraphDocuments.append({
                "_id" : paragraphNumber,
                "paragraph":paragraph 
            })
    collection = getParagraphsCollection()
    collection.insert_many(paragraphDocuments)
    
def getParagraphsCollection():
    connection = MongoClient(config.dbServer(), config.dbPort()) #Connect to mongodb
    db = connection[config.dbName()]
    db.authenticate(config.username(), config.password())
    return db['paragraphs']

def getMergedParagraphs():
    paragraphs = []
    previousParagraph = ''
    for paragraph in getAllParagraphs() :
        if previousParagraph != '':
            paragraph = previousParagraph + ' ' + paragraph
            previousParagraph = ''
            
        if len(paragraph) > 250:
            paragraphs.append(paragraph)
        else :
            previousParagraph = paragraph
    return paragraphs
                        
def getAllParagraphs():
    fileName = os.path.join(APP_DIR, '../files/greatGatsby.epub')
    regex = re.compile(r'.*<p>((.|\n)*?)<\/p>', re.MULTILINE)
    
    with zipfile.ZipFile(fileName, 'r') as originalBook:
        for fileEntryName in originalBook.namelist():
            with originalBook.open(fileEntryName) as fileEntry:
                if "main" in fileEntryName and fileEntryName.endswith('.xml'):
                    iterator = regex.finditer(fileEntry.read())
                    for match in iterator:
                        yield match.group(1)
                        
if __name__ == '__main__':
    deleteCollection()
    writeParagraphsToDb()