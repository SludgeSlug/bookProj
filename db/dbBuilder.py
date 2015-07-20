import paragraphGenerator, wordGenerator, word_paragraphCountUpdater

def clearCollections() :
    paragraphGenerator.deleteCollection()
    wordGenerator.deleteCollection()
    word_paragraphCountUpdater.deleteCollection()
    
def loadData() :
    paragraphGenerator.writeParagraphsToDb()
    wordGenerator.writeWordsToDb()
    word_paragraphCountUpdater.writeToDb()
    
if __name__ == '__main__':
    clearCollections()
    loadData()