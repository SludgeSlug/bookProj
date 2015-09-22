class Books:
    def __init__(self, db):
        self.db = db
    
    def get(self):
        ret = []
        books = self.db['books'].find({})
        for book in books:
            ret.append({'id': book['_id'], 'title': book['title']})
        return ret
        
    def getTitle(self, bookId):
        book = self.db['books'].find_one({'_id': bookId})
        return book['title']