import sys
import time
from CrudDatabase import CrudDatabase
from Logging import Logging
from Crud import Crud
from User import User

# Valores padrão
clearTables = False
consoleLog = True
qtyUsers = 100
qtyItems = 100

# Limpar tabelas ou não
clearTablesInput = input('Limpar as tabelas (padrão: não)? (s/n) ')
if clearTablesInput:
    clearTablesInput = clearTablesInput.lower()
    if clearTablesInput == 's':
        clearTables = True
    elif clearTablesInput == 'n':
        clearTables = False
if clearTables: 
    print('As tabelas serão limpadas.')
else:
    print('As tabelas não serão limpadas.')

# Exibir log ou não
consoleLogInput = input('Exibir o log no terminal (padrão: sim)? (s/n) ')
if consoleLogInput:
    consoleLogInput = consoleLogInput.lower()
    if consoleLogInput == 's':
        consoleLog = True
    elif consoleLogInput == 'n':
        consoleLog = False
if consoleLog: 
    print('O log será exibido no terminal.')
else:
    print('O log não será exibido no terminal.')

# Quantidade de usuários a serem usados
qtyUsersInput = input('Quantidade de usuários (padrão: 100): ')
if qtyUsersInput:
    try:
        qtyUsersInput = int(qtyUsersInput)
        if qtyUsersInput > 0 and qtyUsersInput < 10000:
            qtyUsers = qtyUsersInput
        else:
            print('Valor inválido, utilizando valor padrão.')
    except ValueError:
        print('O valor inserido não é inteiro, utilizando valor padrão.')
print('Serão utilizados '+str(qtyUsers)+' usuários')

# Quantidade de itens iniciais
qtyItemsInput = input('Quantidade de itens iniciais (padrão: 100): ')
if qtyItemsInput:
    try:
        qtyItemsInput = int(qtyItemsInput)
        if qtyItemsInput > 0 and qtyItemsInput < 10000:
            qtyItems = qtyItemsInput
        else:
            print('Valor inválido, utilizando valor padrão.')
    except ValueError:
        print('O valor inserido não é inteiro, utilizando valor padrão.')
print('Serão utilizados '+str(qtyItems)+' itens iniciais')

print('Iniciando em 2 segundos')
time.sleep(2)

# Inicializar objetos e variáveis
crudDb = CrudDatabase()
db = crudDb.db
logging = Logging(db)
crud = Crud(db, logging, consoleLog)
users = []

# Limpar tabelas
if clearTables:
    crudDb.dropTables()

# Criar tabelas se não existirem
crudDb.createTables()
# Criar usuários se não existirem
crudDb.createUsers(qtyUsers)
# Criar itens se não existirem
crudDb.createItems(qtyItems)

# Criar usuários (threads)
for i in range(1, (qtyUsers+1)):
    u = User(i, crudDb, crud)
    u.daemon = True
    users.append(u)

# Iniciar os usuários (threads)
for u in users:
    u.start()

#esta parte do código só serve para parar as threads ao interromper com o teclado (se não é preciso matar o terminal)
try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    sys.exit()