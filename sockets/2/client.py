import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from base_client import Client

client = Client(5000, 1024)
name = None
sex = None
age = None

nameInput = input('Nome: ')
if nameInput:
    name = nameInput
else:
    client.close_connection()
    print('Nome inválido')
    sys.exit()

sexInput = input('Sexo (m/f): ')
if sexInput == 'p' or sexInput == 'm':
    sex = sexInput
else:
    client.close_connection()
    print('Sexo inválido')
    sys.exit()

ageInput = input('Idade: ')
try:
    age = int(ageInput)
    if age <= 0:
        age = None
        client.close_connection()
        print('Idade inválida')
        sys.exit()
except ValueError:
    client.close_connection()
    print('Idade inválida')
    sys.exit()

if name and sex and age:

    data = {
        'name': name,
        'sex': sex,
        'age': age
    }

    message = json.dumps(data)

    result = client.send_message(message)

    print(result)

client.close_connection()