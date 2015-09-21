import paragraphGenerator, wordGenerator, word_paragraphCountUpdater, bookGenerator
import os, zipfile, glob

APP_DIR = os.path.dirname(os.path.abspath(__file__))

def clearCollections() :
    paragraphGenerator.deleteCollection()
    wordGenerator.deleteCollection()
    word_paragraphCountUpdater.deleteCollection()
    bookGenerator.deleteCollection()
    
def loadData() :
    bookId = 0
    for fileName in glob.glob("../files/*.epub"):
        bookId = bookId + 1
        bookGenerator.writeBookToDb(bookId, fileName)
        paragraphGenerator.writeParagraphsToDb(bookId, fileName)
        wordGenerator.writeWordsToDb(bookId, fileName)
        word_paragraphCountUpdater.writeToDb(bookId)
    
if __name__ == '__main__':
    clearCollections()
    loadData()