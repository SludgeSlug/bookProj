class Books:
    def __init__(self, db):
        self.db = db
    
    def get(self):
        ret = []
        books = self.db['books'].find({})
        for book in books:
            ret.append({'id': book['_id'], 'title': book['title']})
        return ret