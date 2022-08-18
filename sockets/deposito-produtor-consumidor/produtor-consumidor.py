import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
from base_client import Client

client = Client(5000, 1024)
role = None
interval = None

roleInput = input('Tipo (p/produtor ou c/consumidor): ')
if roleInput == 'p' or roleInput == 'produtor':
    role = 'p'
elif roleInput == 'c' or roleInput == 'consumidor':
    role = 'c'
else:
    client.close_connection()
    print('Tipo inválido')
    sys.exit()

intervalInput = input('Intervalo (segundos): ')
try:
    interval = float(intervalInput)
    if interval <= 0:
        interval = None
        print('Intervalo inválido, usando valor padrão')
except ValueError:
    print('Intervalo inválido, usando valor padrão')

if not interval:
    interval = 2

while True:
    time.sleep(interval)
    if roleInput == 'p':
        client.send_message('colocar')
        print('Colocado')
    elif roleInput == 'c':
        client.send_message('retirar')
        print('Retirado')