import sys
import time
import xmlrpc.client

role = None
interval = None

roleInput = input('Tipo (p/produtor ou c/consumidor): ')
if roleInput == 'p' or roleInput == 'produtor':
    role = 'p'
elif roleInput == 'c' or roleInput == 'consumidor':
    role = 'c'
else:
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

host = '127.0.0.1'
port = 4000
proxy = xmlrpc.client.ServerProxy(f'http://{host}:{port}')

while True:
    time.sleep(interval)
    if roleInput == 'p':
        qty = proxy.colocar()
        print('Colocado; Qtd. atual no depósito: ' + qty)
    elif roleInput == 'c':
        qty = proxy.retirar()
        print('Retirado; Qtd. atual no depósito: ' + qty)