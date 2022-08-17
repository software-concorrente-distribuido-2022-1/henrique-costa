from orator import DatabaseManager, Schema
from faker import Faker

class CrudDatabase:
    faker = Faker()
    db = DatabaseManager({
        'postgresql': {
            'driver': 'postgres',
            'host': 'localhost',
            'database': 'concurrent_crud',
            'user': 'postgres',
            'password': 'postgres'
        }
    })

    def getDb(self):
        return self.db

    # Cria as tabelas se não já existirem
    def createTables(self):
        db = self.db
        schema = Schema(db)

        if not schema.has_table('users'):
            with schema.create('users') as table:
                table.increments('id')
                table.char('name', 50)
                table.char('username', 50)
                table.char('email', 100)
                table.char('password', 64)

            print('Criada tabela de usuários')

        if not schema.has_table('items'):
            with schema.create('items') as table:
                table.increments('id')
                table.char('name', 50)
                table.integer('value')

            print('Criada tabela de itens')

        if not schema.has_table('logs'):
            with schema.create('logs') as table:
                table.increments('id')
                table.char('type', 10)
                table.integer('user_id').unsigned()
                table.foreign('user_id').references('id').on('users')
                table.integer('item_id').unsigned().nullable()
                table.text('log')

            print('Criada tabela de logs')

    # Apagar as tabelas se existirem
    def dropTables(self):
        db = self.db
        schema = Schema(db)

        schema.drop_if_exists('logs')
        schema.drop_if_exists('users')
        schema.drop_if_exists('items')

        print('Tabelas apagadas')

    # Criar a quantidade determinada de usuários se não já existirem
    def createUsers(self, qty):
        db = self.db
        countUsers = db.table('users').count()

        if qty > countUsers:
            qtyCreate = qty - countUsers
            print('Criando %d usuários' % qtyCreate)
            faker = Faker()

            for i in range(qtyCreate):
                profile = faker.simple_profile()
                db.table('users').insert({
                    'name': profile['name'],
                    'username': profile['username'],
                    'email': profile['mail'],
                    'password': faker.sha256()
                })

    # Criar a quantidade determinada de itens se não já existirem
    def createItems(self, qty):
        db = self.db
        countItems = db.table('items').count()

        if qty > countItems:
            qtyCreate = qty - countItems
            print('Criando %d itens' % qtyCreate)
            faker = Faker()

            for i in range(qtyCreate):
                db.table('items').insert({
                    'name': ' '.join(self.faker.words(2)),
                    'value': self.faker.random_int()
                })

    def getRandomItemId(self):
        item = self.db.select('select id from items order by random() limit 1')
        if item:
            return item[0]['id']
        else:
            return 0