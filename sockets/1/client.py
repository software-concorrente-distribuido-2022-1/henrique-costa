import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from base_client import Client

client = Client(5000, 1024)
role = None
salary = None

roleInput = input('Cargo (o/operador ou p/programador): ')
if roleInput == 'p' or roleInput == 'programador':
    role = 'p'
elif roleInput == 'o' or roleInput == 'operador':
    role = 'o'
else:
    client.close_connection()
    print('Cargo inválido')
    sys.exit()

salaryInput = input('Salário: ')
try:
    salary = float(salaryInput)
    if salary <= 0:
        salary = None
        client.close_connection()
        print('Salário inválido')
        sys.exit()
except ValueError:
    client.close_connection()
    print('Salário inválido')
    sys.exit()

if role and salary:

    data = {
        'role': role,
        'salary': salary
    }

    message = json.dumps(data)

    result = client.send_message(message)

    print('Novo salário: R$', result)

client.close_connection()