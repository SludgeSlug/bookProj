class MostUsedWords:
    def __init__(self, db):
        self.db = db
    
    def get(self, offset, limit):
        ret = []
        words = self.db['words'].find({}).sort('count', -1).skip(int(offset)).limit(int(limit))
        for word in words:
            ret.append(word)
        return ret