import threading
import random

class User(threading.Thread):
    user = None
    stopped = False

    def __init__(self, userId, crudDb, crud):
        threading.Thread.__init__(self)
        self.id = userId
        self.crudDb = crudDb
        self.db = crudDb.db
        self.crud = crud

    def login(self):
        self.user = self.db.table('users').where('id', self.id).first()

    def run(self):
        self.login()

        while True:
            randInt = random.randint(1, 4)
            itemId = 0

            # Obter item aleatório se a operação for retrieve, update ou delete
            if randInt > 1:
                itemId = self.crudDb.getRandomItemId()

            # Create
            if randInt == 1:
                self.crud.create(self.user)

            # Retrieve
            elif randInt == 2:
                self.crud.retrieve(self.user, itemId)

            # Update
            elif randInt == 3:
                self.crud.update(self.user, itemId)

            # Delete
            elif randInt == 4:
                self.crud.delete(self.user, itemId)

    def kill(self):
        self.stopped = True