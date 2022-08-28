import sys
import time

import Pyro4

deposito = Pyro4.Proxy('PYRONAME:scp.deposito')

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

while True:
    time.sleep(interval)
    if roleInput == 'p':
        qty = deposito.colocar()
        print('Colocado; Qtd. atual no depósito: ' + qty)
    elif roleInput == 'c':
        qty = deposito.retirar()
        print('Retirado; Qtd. atual no depósito: ' + qty)