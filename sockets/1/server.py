import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from base_server import Server

def calculate_salary(message):
    data = json.loads(message) # obter dados
    role = data['role']
    salary = data['salary']
    newSalary = 0
    
    # calculcar novo salário baseado no cargo
    if role == 'p':
        newSalary = salary + (salary * 0.18)
    elif role == 'o':
        newSalary = salary + (salary * 0.20)

    print('Calculado novo salário')

    return str(newSalary) # retornar novo salário (mensagem a ser enviada de volta para o cliente)

# iniciar servidor
server = Server(5000, 1024)
server.start_server(calculate_salary)