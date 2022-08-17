import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from base_server import Server

def is_adult(message):
    data = json.loads(message) # obter dados
    name = data['name']
    sex = data['sex']
    age = data['age']
    adult = False
    
    # verificar se é adulto(a)
    if sex == 'm' and age >= 18:
        adult = True
    elif sex == 'f' and age >= 21:
        adult = True

    print('Calculado maioridade')

    if (adult):
        return name + ' atingiu a maioridade.'
    else:
        return name + ' não atingiu a maioridade.'

# iniciar servidor
server = Server(5000, 1024)
server.start_server(is_adult)