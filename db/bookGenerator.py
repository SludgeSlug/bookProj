import os, re, zipfile, sys
import config
import xml.etree.ElementTree as ET
from pymongo import MongoClient

APP_DIR = os.path.dirname(os.path.abspath(__file__))

def deleteCollection():
    collection = getBooksCollection()
    collection.drop()
    
def writeBookToDb(bookId, fileName):
    bookTitle = getBookTitle(fileName)
    entry = {"_id": bookId, "title": bookTitle}
    getBooksCollection().insert(entry)
    
def getBookTitle(fileName):
    with zipfile.ZipFile(fileName, 'r') as originalBook:
        for fileEntryName in originalBook.namelist():
            if fileEntryName.endswith('metadata.xml') :
                xml = originalBook.read(fileEntryName)
                root = ET.fromstring(xml)
                return root.find('{http://www.w3.org/2005/Atom}title').text
    
def getBooksCollection():
    connection = MongoClient(config.dbServer(), config.dbPort()) #Connect to mongodb
    db = connection[config.dbName()]
    db.authenticate(config.username(), config.password())
    return db['books']