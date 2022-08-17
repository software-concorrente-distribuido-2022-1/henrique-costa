from faker import Faker
import random

class Crud:
    faker = Faker()

    def __init__(self, db, logging, consoleLog):
        self.db = db
        self.logging = logging
        self.consoleLog = consoleLog

    # Criar
    def create(self, user):
        # Criar item
        itemId = self.db.table('items').insert_get_id({
            'name': ' '.join(self.faker.words(2)),
            'value': self.faker.random_int()
        })

        # Criar log
        self.logging.log('Criado novo Item', 'create', user['id'], itemId)

        # Exibir no console
        if self.consoleLog:
            print(f"[CREATE] Usuário {user['username'].strip()} criou novo Item")

    # Obter
    def retrieve(self, user, itemId):
        # Obter item
        item = self.db.table('items').where('id', itemId).first()

        # Se encontrou o item
        if item != None:
            # Criar log
            self.logging.log('Obtido um Item', 'retrieve', user['id'], item['id'])

            # Exibir no console
            if self.consoleLog:
                print(f"[RETRIEVE] Usuário {user['username'].strip()} obteve um Item")

        # Se não encontrou o item
        else:
            # Criar log
            self.logging.log('Tentado obter um Item, mas o item não existe', 'retrieve', user['id'], itemId)

            # Exibir no console
            if self.consoleLog:
                print(f"[RETRIEVE] Usuário {user['username'].strip()} tentou obeter um Item(ID: {itemId}), mas o item não existe")

    # Atualizar
    def update(self, user, itemId):
        # Obter item
        item = self.db.table('items').where('id', itemId).first()

        # Se encontrou o item
        if item != None:

            column = None
            oldValue = None
            newValue = None

            if random.randint(0, 1):
                column = 'name'
                oldValue = item['name']
                newValue = ' '.join(self.faker.words(2))
            else:
                column = 'value'
                oldValue = str(item['value'])
                newValue = str(self.faker.random_int())

            self.db.table('items').where('id', itemId).update({
                column: newValue
            })

            # Criar log
            self.logging.log(f'Atualizado um Item. "{column.strip()}" de "{oldValue.strip()}" para "{newValue.strip()}"', 'update', user['id'], item['id'])

            # Exibir no console
            if self.consoleLog:
                print(f"[UPDATE] Usuário {user['username'].strip()} atualizar um Item. \"{column.strip()}\" de \"{oldValue.strip()}\" para \"{newValue.strip()}\"")

        # Se não encontrou o item
        else:
            # Criar log
            self.logging.log('Tentado atualizar um Item, mas o item não existe', 'update', user['id'], itemId)

            # Exibir no console
            if self.consoleLog:
                print(f"[UPDATE] Usuário {user['username'].strip()} tentou atualizar um Item(ID: {itemId}), mas o item não existe")

    # Deletar
    def delete(self, user, itemId):
        # Obter item
        item = self.db.table('items').where('id', itemId).first()

        # Se encontrou o item
        if item != None:
            #deletar
            self.db.table('items').where('id', itemId).delete()

            # Criar log
            self.logging.log('Deletado um Item', 'delete', user['id'], item['id'])

            # Exibir no console
            if self.consoleLog:
                print(f"[DELETE] Usuário {user['username'].strip()} deletou um Item")

        # Se não encontrou o item
        else:
            # Criar log
            self.logging.log('Tentado deletar um Item, mas o item não existe', 'delete', user['id'], itemId)

            # Exibir no console
            if self.consoleLog:
                print(f"[DELETE] Usuário {user['username'].strip()} tentou deletar um Item(ID: {itemId}), mas o item não existe")