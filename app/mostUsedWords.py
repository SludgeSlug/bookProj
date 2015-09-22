class MostUsedWords:
    def __init__(self, db):
        self.db = db
    
    def get(self, offset, limit, bookId):
        ret = []
        words = self.db['words'].find({'bookId': bookId}).sort('count', -1).skip(int(offset)).limit(int(limit))
        for word in words:
            ret.append({'word': word['word'], 'count': word['count']})
        return ret
        
    def numberOfWords(self, bookId):
        return self.db['words'].find({'bookId': bookId}).count()