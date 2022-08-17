import threading

class Logging:
    lock = threading.Lock()

    def __init__(self, db):
        self.db = db

    def log(self, log, crudType, userId, itemId):
        self.lock.acquire()

        self.db.table('logs').insert({
            'log': log,
            'type': crudType,
            'user_id': userId,
            'item_id': itemId
        })

        self.lock.release()