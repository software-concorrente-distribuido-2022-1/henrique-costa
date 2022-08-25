import sys
import xmlrpc.client

host = '127.0.0.1'
port = 4000
proxy = xmlrpc.client.ServerProxy(f'http://{host}:{port}')

name = None
sex = None
age = None

nameInput = input('Nome: ')
if nameInput:
    name = nameInput
else:
    print('Nome inválido')
    sys.exit()

sexInput = input('Sexo (m/f): ')
if sexInput == 'p' or sexInput == 'm':
    sex = sexInput
else:
    print('Sexo inválido')
    sys.exit()

ageInput = input('Idade: ')
try:
    age = int(ageInput)
    if age <= 0:
        age = None
        print('Idade inválida')
        sys.exit()
except ValueError:
    print('Idade inválida')
    sys.exit()

if name and sex and age:
    response = proxy.is_adult(name, sex, age)
    print(response)