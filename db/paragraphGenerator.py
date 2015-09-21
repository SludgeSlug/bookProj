import os, re, zipfile, sys
import config
from pymongo import MongoClient

def deleteCollection():
    collection = getParagraphsCollection()
    collection.drop()

def writeParagraphsToDb(bookId, fileName):
    paragraphDocuments = []
    for paragraph in getMergedParagraphs(fileName):
        paragraphDocuments.append({
                "paragraph":paragraph,
                "bookId": bookId
            })
    collection = getParagraphsCollection()
    collection.insert_many(paragraphDocuments)
    
def getParagraphsCollection():
    connection = MongoClient(config.dbServer(), config.dbPort()) #Connect to mongodb
    db = connection[config.dbName()]
    db.authenticate(config.username(), config.password())
    return db['paragraphs']

def getMergedParagraphs(fileName):
    paragraphs = []
    previousParagraph = ''
    for paragraph in getAllParagraphs(fileName) :
        if previousParagraph != '':
            paragraph = previousParagraph + ' ' + paragraph
            previousParagraph = ''
            
        if len(paragraph) > 250:
            paragraphs.append(paragraph)
        else :
            previousParagraph = paragraph
    return paragraphs
                        
def getAllParagraphs(fileName):
    regex = re.compile(r'.*<p>((.|\n)*?)<\/p>', re.MULTILINE)
    
    with zipfile.ZipFile(fileName, 'r') as originalBook:
        for fileEntryName in originalBook.namelist():
            with originalBook.open(fileEntryName) as fileEntry:
                if "main" in fileEntryName and fileEntryName.endswith('.xml'):
                    iterator = regex.finditer(fileEntry.read())
                    for match in iterator:
                        yield match.group(1)